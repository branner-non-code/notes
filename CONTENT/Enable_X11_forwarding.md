## Enable X11 forwarding

I have used this between Ubuntu v. 14.04 remote and Mac OS 10.9 local machines.

 1. Enable X11 forwarding on the local machine. On Mac OS 10.9 use:

        sudo vim /private/etc/sshd_config

   and then uncomment `#X11Forwarding no` and set to `yes`, then save.

 1. Log into the remote server with option `-Y` for trusted X11 forwarding. An alternative using `-X` with `ForwardX11Trusted` set to `yes` in `sshd_config`.

 1. To test, use one of the following:
 
        xeyes &
        oclock &
        xclock &
        xmessage 'working' &
 
   etc.: available in package `x11-apps`.

[end]