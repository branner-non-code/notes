# Dates of filesystem files

1. `os.path` has three methods to return file dates in seconds (float):
 1. `os.path.getctime`: creation time
 1. `os.path.getmtime`: modification time
 1. `os.path.getatime`: last access time
1. All three of the above are reported in a single tuple by `os.stat()`, along with other file data associated with `stat` at the prompt.

[end]
