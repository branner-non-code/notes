## X11/XQuartz auto-quit

Set X11/XQuartz to auto-quit, after 3 seconds, when all windows are closed.

From `man quartz-wm`:

```bash
defaults write org.x.X11 wm_auto_quit -bool true
defaults write org.x.X11 wm_auto_quit_timeout -int 3
```

Tried 20161006 (Mac OS 10.9.5) and it didn't work.

[end]