## Compiling Alpine

Locking not an issue for me. Managing messages on an individual basis more important — they sometimes get saved into an mbox folder 

See the [specification](http://cr.yp.to/proto/maildir.html).

### Installation

Installing from source in order to support Maildir and other patches and special configuration changes. Patches are distributed from [Eduardo Chappa's site](http://patches.freeiz.com/alpine), and there is fairly thorough documentation [on the same site](http://patches.freeiz.com/alpine/alpine-info/).

I installed on Ubuntu 14.04.2 LTS (Trusty).

 1. Dependencies: 
 
    2. `build-essential`: C compiler
    2. `libncurses5-dev`: termcap (Terminal Capability database)
    2. `libssl-dev`: support for later version of `openssl`
    2. `libpam-dev`: support for `PAM` (Pluggable Authentication Modules library)

    ```bash
    sudo apt-get install build-essential libncurses5-dev libssl-dev libpam-dev
    ```

 1. Get sourcecode; check MD5; untar, and enter directory before patching and building.

    ```bash
    wget patches.freeiz.com/alpine/release/src/alpine-2.20.tar.xz
    # Check MD5 hash. (omitted)
    tar -Jxf alpine-2.20.tar.xz
    cd alpine-2.20
    ```

 1. Prepare and install Maildir patch

    ```bash
    wget patches.freeiz.com/alpine/patches/alpine-2.20/maildir.patch.gz
    gunzip maildir.patch.gz
    patch -p 1 < maildir.patch
    ```
    
    Note that this requires a special setting for `folder-collections` in `.alpinerc`; see http://patches.freeiz.com/alpine/info/maildir.html for details.

 1. Prepare and install other patches. Do these one at a time so as be able to read the output of each `patch` call.
 
    ```bash
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/status.patch.gz
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/reply.patch.gz
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/delpassword.patch.gz
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/count.patch.gz
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/tome.patch.gz
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/outgoing.patch.gz
    wget http://patches.freeiz.com/alpine/patches/alpine-2.20/rules.patch.gz

    gunzip status.patch.gz reply.patch.gz delpassword.patch.gz count.patch.gz tome.patch.gz outgoing.patch.gz rules.patch.gz

    patch -p 1 < status.patch
    patch -p 1 < reply.patch
    patch -p 1 < delpassword.patch
    patch -p 1 < count.patch
    patch -p 1 < tome.patch
    patch -p 1 < outgoing.patch
    patch -p 1 < rules.patch
    ```
    
    Read about each patch at http://patches.freeiz.com/pine/info/.

 1. Follow instructions in `alpine-2.20/README`. Configure and make.

    ```bash
    ./configure --without-ipv6 --enable-quotas --with-passfile=<passfile>
    sudo make install
    ```

[end]