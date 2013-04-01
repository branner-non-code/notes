Tmux
====

Screen multiplexer

    tmux

1.  `^b` followed by another command lists the key-bindings. Using
    question mark gives a list of all key-bindings, and then `return`

2.  `^b d` will “detach” the windows — returning you to the regular
    shell. At this stage, `tmux attach` will reattach to the tmux
    windows. The advantage of detaching is that processes can be left
    running

3.  `exit` will exit a specific window.

4.  `tmux list-windows` to show windows

5.  `^b c`: new window

[end]
