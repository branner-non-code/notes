## Python: `subprocess` for command-line commands with pipes

In Python `subprocess`, don't use `Popen.check_output` if there are pipes; intead use `Popen.communicate`.

[end]
