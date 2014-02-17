## VisualHostKey - ASCII visual pattern when using SSH

Place

~~~

VisualHostKey=yes

~~~

into `~/.ssh/config`

This will lead to the display of an abstract ASCII design representing the host key fingerprint of any host being connected to over SSH. The idea is that such patterns are easier for the human eye to recognize than strings of hex.

[end]
