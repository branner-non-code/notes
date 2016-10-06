## Spacemacs paste without auto-indent

The goal is to emulate Vim `:set paste`.

 * `c-toggle-syntactic-indentation` or else `clipboard-yank` and `clipboard-kill-region` (http://unix.stackexchange.com/questions/44594/emacs-paste-text-from-clipboard-without-formatting)
 * `electric-indent-local-mode` and `electric-indent-mode` (http://askubuntu.com/questions/670773/how-to-paste-into-emacs-no-window-system-without-auto-indent)

---

**The following doesn't work yet!**

The native EMACS way to do this is to switch to the `*scratch*` buffer, paste from the clipboard using your operating system's paste function, and then 

 * `SPC b s`: switch to the `*scratch*` buffer
 * (Paste from clipboard using your operating system's paste function.)
 * `SPC b d`: "kill" (cut) text and copy to "kill-ring" (EMACS clipboard)
 * `s v`: "yank" (paste) from kill-ring — **this doesn't work, either**

[end]