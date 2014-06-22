## Prevent ssh connection from dying

Add

~~~
Host *                    
    ServerAliveInterval 60                                                      
~~~

to `~/.ssh/config`.

[end]
