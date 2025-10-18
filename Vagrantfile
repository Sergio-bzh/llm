Vagrant.configure("2") do |config|
  config.hostmanager.enabled = true 
  config.hostmanager.manage_host = true

### Mon LLM Local vm  ####
  config.vm.define "llm" do |llm|
    llm.vm.box = "bento/ubuntu-22.04"
    llm.vm.hostname = "llm-local"
    llm.vm.network "private_network", ip: "192.168.56.75"
    llm.vm.provider "vmware_fusion" do |v|
      v.gui = false
        v.allowlist_verified = true
        v.cpus = "4"
        v.memory = "8192"
      end
    llm.vm.provision "shell", path: "llm_provision.sh"
  end
end
