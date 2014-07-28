## Prune VirtualBox Ubuntu installation

At boot, message

```
  => /boot is using 91.2% of 227MB
```

Attempts to update via `apt-get` fail, ending:

```
Setting up linux-libc-dev (3.2.0-44.69) ...
No apport report written because the error message indicates its a followup error from a previous failure.
                          No apport report written because the error message indicates its a followup error from a previous failure.
                                                    Errors were encountered while processing:
 linux-image-3.2.0-44-generic
 linux-image-server
 linux-server
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

Fixed following http://askubuntu.com/questions/223248/boot-low-on-disk-space: delete some old kernel image files:

```
$ aptitude search ~ilinux-image
i   linux-image-3.2.0-29-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-35-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-36-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-37-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-38-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-39-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-40-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-41-generic    - Linux kernel image for version 3.2.0 on 64
i   linux-image-3.2.0-43-generic    - Linux kernel image for version 3.2.0 on 64
C   linux-image-3.2.0-44-generic    - Linux kernel image for version 3.2.0 on 64
u   linux-image-server              - Linux kernel image on Server Equipment.   
$ sudo apt-get autoremove linux-image-3.2.0-29-generic linux-image-3.2.0-35-generic linux-image-3.2.0-36-generic linux-image-3.2.0-37-generic
```

`apt-get` updates now succeed and login messages about /boot quota cease.

[end]
