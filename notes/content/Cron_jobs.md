## Cron Jobs

 1. Use `crontab -l` to write cron jobs
 1. Include full statements of the `SHELL` and `PATH` variables:

        SHELL=/bin/bash
        PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

 1. Include absolute rather than relative paths.
 1. Scripts must be executable in order to be run.

[end]
