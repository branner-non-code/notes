## X2Go

Remote desktop software for the Linux GUI.

X2Go server runs on Linux; client runs on Mac, etc., securely tunneled over SSH.

Recommended by Norm Kabir 20160930 in order to have stable and easy-to-use Linux environments on a non-Linux machine.


### Installing new virtual machine

 * Memory size: 2048MB
 * Hard drive: Create a virtual hard drive now
 * Hard drive file type: VDI
 * Storage on physical hard drive: Dynamically allocated
 * File location and size: 8.00 GB

### Virtual machine settings

 * Adapter: bridged

### Installations on virtual machine

First, update and upgrade the basic installation.

Then add the `x2go` repository and install the needed software:

```bash
sudo add-apt-repository ppa:x2go/stable
sudo apt-get update
sudo apt-get install x2goserver x2goserver-xsession
```

### Choosing an IP address

(From Norm Kabir, 20161004.)

Start with your home network where you have a ready pool of DHCP addresses. Set your guest to bridged. Your workstation guest will be just another machine on your network with an IP on the same range as your laptop.

The IP address is assigned automatically when you used bridged networking--assuming your local network has a DHCP server (most people run routers that host DHCP).

Start with that.

Once you get that working, you can get fancy i.e. have your guest be invisible and use your Mac as its route to the outside world.

You won't need to reconfigure the `x2go` client until you go to another network. Your DHCP server generally reassigns the same IP to a given MAC address.

Again, this is to get it working first.

Once you get things working, you'll configure your guest with two network interfaces:

 * Host only (an IP assigned by your host, Macbook, that doesn't change)
 * NAT (to enable your guest to reach the internet)

But two network interfaces are harder to debug than one. So be sure to get bridged networking first.

> In setting up virtual machines with VirtualBox, I often want the following characteristics:
> 
>  * vm has a static ip
>  * host can access vm without port forwarding
>  * vm can access the internet
>  * I can move my laptop from network to network (e.g. from home to office to coffeeshop) without worrying about securing or reconfiguring the vm

http://askubuntu.com/questions/293816/in-virtualbox-how-do-i-set-up-host-only-
virtual-machines-that-can-access-the-in

---

At some point, the guest OS needs to be informed about its static ip:

http://coding4streetcred.com/blog/post/VirtualBox-Configuring-Static-IPs-for-VMs

But Virtualbox only presents a raw x86 interface so I'm not sure how it could be completely done on the Virtualbox side. But maybe they had a hack in the earlier version...


[end]