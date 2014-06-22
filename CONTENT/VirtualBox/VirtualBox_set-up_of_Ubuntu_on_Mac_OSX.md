## VirtualBox set-up of Ubuntu guest on Mac OS X

Below describes using Ubuntu v. 14.04 LTS on VirtualBox v. 4.3.12.

 1. Platform: https://www.virtualbox.org/wiki/Downloads
 1. VirtualBox Extension Pack (same site). Running VirtualBox will install it.
 1. Guest Additions: Find appropriate version at http://download.virtualbox.org/virtualbox/ and install through running VirtualBox VM (Devices menu).
 1. VirtualBox: choose virtual machine and go to Settings => Network =>
   2. Adapter 1: NAT
   2. Adapter 2: Bridged Adapter, name: en1 USB Ethernet
 1. Start machine, then make backup of `sshd_config` and change the copy that is left in place:

        sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original
        sudo chmod a-w /etc/ssh/sshd_config.original
        sudo vim /etc/ssh/sshd_config

   and set `PasswordAuthentication no`; then

        sudo restart ssh

 1. Make sure there is an ssh key on your host computer and use `ssh-copy-id` to register it with the guest.

[end]
