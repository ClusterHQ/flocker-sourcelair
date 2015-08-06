def install_ssh_keys()
    $script = <<SCRIPT
cat /vagrant/insecure_public_key >> /root/.ssh/authorized_keys
SCRIPT
    return $script
end