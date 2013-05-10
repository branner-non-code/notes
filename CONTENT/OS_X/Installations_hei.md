# Installations hei

## Removed MacPorts (20130510)
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

## Installed HomeBrew (20130510)

 1. Installation, following http://mxcl.github.io/homebrew/

 ```
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

 1. Initial run of `brew doctor` found permissions issues on two man files; fixed. 
 1. Initial run of `brew doctor` found outdated version of `Git`. Version 1.7.5.4 deleted.

## Installations

 1. `git` `bash-completion` `ssh-copy-id` `wget` (20130510)
 1. `gcc47` `gfortran` `eigen` (20130510) Needed for `numpy` and `scipy`. 
  * Note: `gcc-4.7` works with gfortran as of 20130331.

 ```
brew tap homebrew/versions
brew install gcc47 gfortran eigen
brew link gfortran
```

 * `zlib` `openssl` `gnupg` `gnupg2`
