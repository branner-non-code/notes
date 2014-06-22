## VirtualBox set-up of Ubuntu guest on Mac OS X

Below describes using Ubuntu v. 14.04 LTS on VirtualBox v. 4.3.12.

 1. Platform: https://www.virtualbox.org/wiki/Downloads
 1. VirtualBox Extension Pack (same site). Running VirtualBox will install it.
 1. Guest Additions: Find appropriate version at http://download.virtualbox.org/virtualbox/ and install through running VirtualBox VM (Devices menu).
 1. VirtualBox: choose virtual machine and go to Settings => Network =>
   2. Adapter 1: NAT; under "advanced", click "Port Forwarding" and set the Host and Guest Ports to a port of your choosing, and also set the Host IP. These numbers will be used again below. 
   2. Adapter 2: Bridged Adapter, name: en1 USB Ethernet
 1. Start virtual machine, then make backup of `sshd_config` and change the copy that is left in place:

        sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original
        sudo chmod a-w /etc/ssh/sshd_config.original
        sudo vim /etc/ssh/sshd_config


   and set `Port `... to whatever non-standard port you desire. Then
   
        sudo restart ssh

   and make sure you can log in with your password:

        ssh <user>@<IP> -p <port>

 1. Make sure there is an ssh key on your host computer and use `ssh-copy-id` to register it with the guest. Then 

        sudo vim /etc/ssh/sshd_config

   and only then set `PasswordAuthentication no`, and finally

        sudo restart ssh

   Password-login is now disabled in favor of ssh-key login on the specified port only.

[end]
