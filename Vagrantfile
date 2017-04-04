# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
$init = <<SCRIPT
sudo apt-get -y update
sudo apt-get -y install python-dev
# python-pip
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo ln -s /usr/bin/pip /usr/local/bin/pip
# git, git-review
sudo apt-get -y install git
sudo apt-get -y install git-review
# rabbitmq
sudo apt-get -y install rabbitmq-server
sudo rabbitmqctl add_user openstack password
sudo rabbitmqctl set_permissions openstack ".*" ".*" ".*"
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
  end
  
  config.vm.define "server" do |v|
    v.vm.box = "ubuntu/trusty64"
    v.vm.hostname = "server"
    v.vm.network "private_network", ip: "192.168.33.77"
    v.ssh.forward_agent = true
    v.vm.provision :shell, :inline => $init
  end
end

