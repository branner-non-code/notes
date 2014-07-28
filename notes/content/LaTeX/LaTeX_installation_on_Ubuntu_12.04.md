## LaTeX installation on Ubuntu 12.04

 1. Following https://help.ubuntu.com/community/LaTeX, can do regular install from TeXLive site; "If you don't have big space constraints and want the latest version of TeX Live, you can install it directly from the TeX Live website (this does not interfere with the packages in Ubuntu)."

 2. Following http://www.tug.org/texlive/quickinstall.html:

  * Download install-tl-unx.tar.gz:

  ~~~
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xf install-tl-unx.tar.gz
cd install-tl-20130207
sudo ./install-tl
~~~
  * Choose letter paper and install.

  * tlmgr won't run if texlive belongs to root, so change to owner to user:

  ~~~
sudo chown -R dpb /usr/local/texlive
~~~

 But perhaps it is not necessary to run `./install-tl` as root in the first place.

  * Changes to PATH added to .bashrc /etc/profile.d/zzz-texlive.sh

  ~~~
PATH=/usr/local/texlive/2012/bin/x86_64-linux:$PATH
MANPATH=/usr/local/texlive/2012/texmf/doc/man:$MANPATH
INFOPATH=:/usr/local/texlive/2012/texmf/doc/info$INFOPATH
unset TEXINPUTS
unset TEXMFCONFIG
~~~

## Note on docs:
  > See
  >    /usr/local/texlive/2012/index.html
  >  for links to documentation.  The TeX Live web site
  >  contains updates and corrections: http://tug.org/texlive.

## Note on directories:

  >  <D> directories:
  >    TEXDIR (the main TeX directory):
  >      !! default location: /usr/local/texlive/2012
  >      !! is not writable, please select a different one!
  >    TEXMFLOCAL (directory for site-wide local files):
  >      /usr/local/texlive/texmf-local
  >    TEXMFSYSVAR (directory for variable and automatically generated data):
  >      /usr/local/texlive/2012/texmf-var
  >    TEXMFSYSCONFIG (directory for local config):
  >      /usr/local/texlive/2012/texmf-config
  >    TEXMFVAR (personal directory for variable and automatically generated data):
  >      ~/.texlive2012/texmf-var
  >    TEXMFCONFIG (personal directory for local config):
  >      ~/.texlive2012/texmf-config
  >    TEXMFHOME (directory for user-specific files):
  >      ~/texmf

[end]
