## Installations 11

OS 10.8.3

### Removed MacPorts (20130527)
 1. Removed active ports, following http://guide.macports.org/chunked/installing.macports.uninstalling.html

 ```
sudo port -fp uninstall installed
```

 1. Removed other files, following http://guide.macports.org/chunked/installing.macports.uninstalling.html

 ```
sudo rm -rf \
    /opt/local \
    /Applications/DarwinPorts \
    /Applications/MacPorts \
    /Library/LaunchDaemons/org.macports.* \
    /Library/Receipts/DarwinPorts*.pkg \
    /Library/Receipts/MacPorts*.pkg \
    /Library/StartupItems/DarwinPortsStartup \
    /Library/Tcl/darwinports1.0 \
    /Library/Tcl/macports1.0 \
    ~/.macports
```

### Installed HomeBrew (20130527)

 1. Installation, following http://mxcl.github.io/homebrew/

 ```
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

 1. Initial run of `brew doctor` found permissions issues on two man files; fixed. 
 1. Initial run of `brew doctor` found various "unbrewed" `dylibs` and `.pc` files and static libraries; fixed. 
 1. Initial run of `brew doctor` found Xcode out of date; fixed. 
 1. Initial run of `brew doctor` found outdated version of `Git`. 
 1. Subsequent run of `brew doctor` found compilers out of date for current version of Xcode.

### Installations

 1. `git` `bash-completion` `ssh-copy-id` `wget` (20130527). 
 
 Caveat about `git` from installer:
 
 > The OS X keychain credential helper has been installed to:
 >   /usr/local/bin/git-credential-osxkeychain
 > 
 > The 'contrib' directory has been installed to:
 >   /usr/local/share/git-core/contrib
 > 
 > Bash completion has been installed to:
 >   /usr/local/etc/bash_completion.d
 > 
 > zsh completion has been installed to:
 >   /usr/local/share/zsh/site-functions
 
 Caveat about `bash-completion` from installer:
 
 > Add the following lines to your ~/.bash_profile:
 >  if [ -f $(brew --prefix)/etc/bash_completion ]; then
 >    . $(brew --prefix)/etc/bash_completion
 >  fi
 >
 >Homebrew's own bash completion script has been installed to
 >  /usr/local/etc/bash_completion.d
 >
 >Bash completion has been installed to:
 >  /usr/local/etc/bash_completion.d

 1. `lzlib` `openssl` `gnupg` `gnupg2` (20130510) Needed for `tarsnap`. Caveats abt `openssl` from installer:

 > To install updated CA certs from Mozilla.org:
 >
 >     brew install curl-ca-bundle
 >
 > This formula is keg-only: so it was not symlinked into /usr/local.
 > 
 > Mac OS X already provides this software and installing another version in
 > parallel can cause all kinds of trouble.
 > 
 > The OpenSSL provided by OS X is too old for some software.
 > 
 > Generally there are no consequences of this for you. If you build your
 > own software and it requires this formula, you'll need to add to your
 > build variables:
 > 
 >     LDFLAGS:  -L/usr/local/opt/openssl/lib
 >     CPPFLAGS: -I/usr/local/opt/openssl/include 
  * `brew doctor` now reports problems with PATH; fixed. All earlier changes to `~/.bash_profile` from MacPorts removed.
 
 1. `tarsnap` (previous installation)

 ```
wget --no-check-certificate https://www.tarsnap.com/download/tarsnap-autoconf-1.0.33.tgz
```
  * OS X automatically untars.
  * Confirm SHA 256 signature (following https://www.tarsnap.com/download.html)
  * CD into new directory
 
  ```
sudo ./configure
sudo make all install clean
```
 1. `curl-ca-bundle` 

 1. `gcc47` `gfortran` `eigen` (20130527). Multi-hour installation. Needed for `numpy` and `scipy`. 
  * Note: `gcc-4.7` works with gfortran as of 20130331.
  * `gcc47` is not normally supplied, but is available through `brew tap`, which adds formula repositories.

 ```
brew tap homebrew/versions
brew install gcc47 gfortran eigen
brew link gfortran
```
 
 Caveat for dependencies:
 
 > This formula is keg-only: so it was not symlinked into /usr/local.
 > 
 > Conflicts with gmp in main repository.
 > 
 > Generally there are no consequences of this for you. If you build your
 > own software and it requires this formula, you'll need to add to your
 > build variables:
 > 
 >     LDFLAGS:  -L/usr/local/opt/gmp4/lib
 >     CPPFLAGS: -I/usr/local/opt/gmp4/include
 >
 > This formula is keg-only: so it was not symlinked into /usr/local.
 > 
 > Conflicts with mpfr in main repository.
 > 
 > Generally there are no consequences of this for you. If you build your
 > own software and it requires this formula, you'll need to add to your
 > build variables:
 > 
 >     LDFLAGS:  -L/usr/local/opt/mpfr2/lib
 >     CPPFLAGS: -I/usr/local/opt/mpfr2/include
 > 
 > This formula is keg-only: so it was not symlinked into /usr/local.
 > 
 > Conflicts with libmpc in main repository.
 > 
 > Generally there are no consequences of this for you. If you build your
 > own software and it requires this formula, you'll need to add to your
 > build variables:
 > 
 >     LDFLAGS:  -L/usr/local/opt/libmpc08/lib
 >     CPPFLAGS: -I/usr/local/opt/libmpc08/include
 >
 >  This formula is keg-only: so it was not symlinked into /usr/local.
 > 
 > Conflicts with ppl in main repository.
 > 
 > Generally there are no consequences of this for you. If you build your
 > own software and it requires this formula, you'll need to add to your
 > build variables:
 > 
 >     LDFLAGS:  -L/usr/local/opt/ppl011/lib
 >     CPPFLAGS: -I/usr/local/opt/ppl011/include
 > 
 > This formula is keg-only: so it was not symlinked into /usr/local.
 > 
 > Conflicts with cloog in main repository.
 > 
 > Generally there are no consequences of this for you. If you build your
 > own software and it requires this formula, you'll need to add to your
 > build variables:
 > 
 >     LDFLAGS:  -L/usr/local/opt/cloog-ppl015/lib
 >     CPPFLAGS: -I/usr/local/opt/cloog-ppl015/include
 >
 > Brews that require a Fortran compiler should not use:
 >   depends_on 'gfortran'
 > 
 > The preferred method of declaring Fortran support is to use:
 >   def install
 >     ...
 >     ENV.fortran
 >     ...
 >   end


 1. `virtualenv` (20130527). Normally involves installation with `pip`, but we install `pip` only within `virtualenv` environments!
 
 ```
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz
tar xvfz virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1
sudo python setup.py install
```
  * Create alias:

  ```
alias virtualenv='/usr/local/bin/virtualenv'
```

 1. `python3` (20130527). The following caveat was generated:
 
  > Homebrew's Python3 framework
  >   /usr/local/Cellar/python3/3.3.1/Frameworks/Python.framework
  > 
  > Distribute and Pip have been installed. To update them
  >   pip3 install --upgrade distribute
  >   pip3 install --upgrade pip
  > 
  > To symlink "Idle 3" and the "Python Launcher 3" to ~/Applications
  >   `brew linkapps`
  > 
  > You can install Python packages with
  >   `pip3 install <your_favorite_package>`
  > 
  > They will install into the site-package directory
  >   /usr/local/lib/python3.3/site-packages
  > Executable python scripts will be put in:
  >   /usr/local/share/python3
  > so you may want to put "/usr/local/share/python3" in your PATH, too.
  > 
  > See: https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python
  > 
  > Apple's Tcl/Tk is not recommended for use with Python on Mac OS X 10.6.
  > For more information see: http://www.python.org/download/mac/tcltk/

 1. `python` v. 2.7. (20130510). Using `brew install python`. This makes `pip` (not `pip3`) available.
 
 1. `mercurial` for Python27. (20130510). Using `pip install --upgrade Mercurial`. Alias to `/usr/local/share/python/hg` placed in `~/.bash_profile`.

[end]
