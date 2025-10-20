Vagrant.configure("2") do |config|
  config.hostmanager.enabled = true 
  config.hostmanager.manage_host = true
  config.disksize.size = "100GB"

### Mon LLM Local vm  ####
  config.vm.define "llm" do |llm|
    llm.vm.box = "bento/ubuntu-22.04"
    llm.vm.hostname = "llm-local"
    llm.vm.network "private_network", ip: "192.168.56.75"
    llm.vm.provider "virtualbox" do |vb|
      vb.gui = false
      # vb.allowlist_verified = true
      vb.cpus = 4
      # vb.memory = 16384
      vb.memory = 8192 # Adjusted for testing
    end
    llm.vm.provision "shell", path: "llm_provision.sh"
  end
end
