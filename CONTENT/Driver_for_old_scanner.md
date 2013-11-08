## Driver for old scanner

For use with a vintage c. 2002 Canon scanner (CanoScan N1220U) on OS 10.8, no drivers are now available from Canon. I have installed SANE from http://www.sane-project.org and it works well from the command line, and can also be used to import (a tad clunkily) into OpenOffice.

I installed the Mac-specific versions from http://www.ellert.se/twain-sane/, rather than what is available via `homebrew`; `homebrew`'s version of `sane-backend` apparently did not include the most useful command-line tool, `scanimage`. Also `homebrew`'s version of `libusb` did not work as well as `libusbx`. 

The FAQ at http://www.ellert.se/twain-sane/faq.html was helpful in getting started. For my wife's use, I added aliases for the main configurations she is likely to use.

[end]
