## VirtualBox set-up of Ubuntu guest on Mac OS X

Below describes using Ubuntu v. 14.04 LTS on VirtualBox v. 4.3.12.

 1. Platform: https://www.virtualbox.org/wiki/Downloads
 1. VirtualBox Extension Pack (same site). Running VirtualBox will install it.
 1. Guest Additions: Find appropriate version at http://download.virtualbox.org/virtualbox/ and install through running VirtualBox VM (Devices menu).
 1. VirtualBox: choose virtual machine and go to Settings => Network =>
   2. Adapter 1: NAT; under "advanced", click "Port Forwarding" and set the Host and Guest Ports to a port of your choosing, and also set the Host IP. These numbers will be used again below. 
   2. Adapter 2: Bridged Adapter, name: en1 USB Ethernet
 1. Start virtual machine, then on Guest make backup of `sshd_config` and change the copy that is left in place:

        sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original
        sudo chmod a-w /etc/ssh/sshd_config.original
        sudo vim /etc/ssh/sshd_config


   and set `Port `... to whatever non-standard port you assigned to the NAT adapter above. Then
   
        sudo restart ssh

   and make sure you can log into the Guest from the Host with your password:

        ssh <user>@<IP> -p <port>

   Then log out of the Guest.

 1. Make sure there is an ssh key on the Host and use `ssh-copy-id` to register it with the Guest. Then on the Guest: 

        sudo vim /etc/ssh/sshd_config

   and only then set `PasswordAuthentication no`, and finally

        sudo restart ssh

   Password-login is now disabled in favor of ssh-key login, and login is permitted on the specified port only.

[end]
