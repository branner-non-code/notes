Virtualenv
==========

1. Zach Allaun suggests having a general Python3 environment for transient work, at `~` level, while also making a `v_env` subdirectory in any given Python-based project.

1. To ensure Python3 support, use
 ```
virtualenv v_env3 --python=python3
```

 or 

 ```
virtualenv v_env3 --python=python3.3
```

1. To determine the path of the original virtualenv directory, use

 ```
echo $VIRTUAL_ENV
```

[end]
