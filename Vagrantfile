# Vagrantfile pour configurer une VM Ubuntu 22.04 pour un LLM local
# Dépendances requises :
# - Plugin Vagrant : vagrant-disksize (installer avec `vagrant plugin install vagrant-disksize`)
# - Plugin Vagrant : vagrant-hostmanager (installer avec `vagrant plugin install vagrant-hostmanager`)
# - Box : bento/ubuntu-22.04

Vagrant.configure("2") do |config|
  # Variables pour une configuration maintenable
  VM_NAME = "llm-local"
  IP_ADDRESS = "192.168.56.75"
  DISK_SIZE = "100GB"
  CPUS = 4
  MEMORY = 16384
  BOX = "bento/ubuntu-22.04"
  BOX_VERSION = "~> 202206.03.0" # Spécifie une version pour la reproductibilité

  # Configuration globale
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.disksize.size = DISK_SIZE

  ### Mon LLM Local VM ###
  config.vm.define "llm" do |llm|
    llm.vm.box = BOX
    llm.vm.box_version = BOX_VERSION
    llm.vm.hostname = VM_NAME
    llm.vm.network "private_network", ip: IP_ADDRESS

    # Configuration du provider VirtualBox
    llm.vm.provider "virtualbox" do |vb|
      vb.gui = true # Interface graphique activée (désactiver si inutile pour économiser des ressources)
      vb.cpus = CPUS
      vb.memory = MEMORY
      vb.name = VM_NAME
    end

    # Provisionnement pour étendre le disque LVM
    llm.vm.provision "shell", inline: <<-SHELL
      set -e # Arrêter en cas d'erreur
      echo "Mise à jour des paquets..."
      sudo apt update || { echo "Erreur lors de l'apt update"; exit 1; }
      sudo apt install -y cloud-guest-utils || { echo "Erreur lors de l'installation de cloud-guest-utils"; exit 1; }

      echo "Extension de la partition LVM..."
      sudo growpart /dev/sda 3 || { echo "Erreur lors de l'extension de la partition"; exit 1; }
      sudo pvresize /dev/sda3 || { echo "Erreur lors du redimensionnement du volume physique"; exit 1; }
      sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv || { echo "Erreur lors de l'extension du volume logique"; exit 1; }
      sudo resize2fs /dev/ubuntu-vg/ubuntu-lv || { echo "Erreur lors du redimensionnement du système de fichiers"; exit 1; }

      echo "Vérification de l'espace disque :"
      df -h / | tee /vagrant/disk_space.log # Sauvegarde du résultat dans un fichier pour analyse
    SHELL

    # Provisionnement supplémentaire via un script externe
    llm.vm.provision "shell", path: "llm_provision.sh"
  end
end