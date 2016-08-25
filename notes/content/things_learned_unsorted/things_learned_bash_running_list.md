## Things Learned, Bash (running list)

 1. Install `trash-put` to avoid risk of unintended deletions with `rm`. Following [trash-cli](https://github.com/andreafrancia/trash-cli) instructions:

        git clone https://github.com/andreafrancia/trash-cli.git
        sudo python setup.py install

    And add this alias to `.bash_profile`:

        alias rm='echo "This is not the command you are looking for."; false'

    To use plain `rm` enter it as `\rm`.

 1. To pipe output to a file without suppressing it at STDOUT, use `| tee <filename>`.

 1. To store OrderedDict, convert to JSON string rather than using `ast.literal_eval`; the latter changes order (though following http://stackoverflow.com/a/10498910 there is a workaround).

        # Make large OrderedDict
        d = collections.OrderedDict(sorted([(chr(i), i) for i in range(2000)]))
        # Convert to JSON string; we think order is retained.
        j = json.dumps(d)
        # Run long loop to ensure there is never a change in the order
        c = 0
        while True:
            assert j == json.dumps(d)
                c += 1
        # On ^c, printing `c` tells us number of loops tested.

    Tested 531271 rounds.

    Using `json.loads` to recover the string retrieves the elements in no obvious order. But as long as `d` itself was sorted, we can recover the sorted order by resorting:

        In [59]: collections.OrderedDict(
            sorted(
            [(item, json.loads(j)[item]) for item in json.loads(j)]
            )) == d
        Out[59]: True

 1. Save to particular directory with `wget` or `tar`:

        wget --directory-prefix=/target_directory/ [...]
        tar [...] -C /target_directory

 1. `dd` can specify block-size using `-bs=n`; can then be made comparable to `cat` in speed.
 
 1. `recv()` may return only 1 byte each time it returns because it is reading from network rather than a file.

 1. `ls` options:
 
    2. `-d`: list directories non-recursively
    2. `-t`: sort by time modified
    2. `-r`: reverse the sort
    2. `-T`: full time display
    2. `-S`: sort files by size
    2. `-h`: human-readable file sizes
    2. `-i`: include file serial number (inode)
    2. `-a`: include names beginning with `.`
    2. `-A`: include names beginning with `.` but omit plain `.` and `..`
    2. `-G`: use color (this may be Apple-specific)
    2. Himanish Kushary uses `-litr` regularly.
    2. I have been using `-al` since my graduate school days.
    2. Try to switch today to `-GAlth`.

 1. `echo` options
 
    2. `-n`: suppress final newline
    2. alternative: `printf`

### Already moved to Notes on line.

(None)

[end]
