#! /usr/bin/env python
# find_large_file_py3.py
# Based on http://stackoverflow.com/a/10099633/621762

"""Report all files in git commit history over a given size."""

import sys
if sys.version_info[0] < 3:
    sys.stdout.write('Python 3 required; exiting.')
    sys.exit()
import os

def main(argv):
    if len(argv) != 2:
        size_limit = 100000000 # Current GitHub maximum file size.
    else:
        size_limit = int(argv[1])
    commits = os.popen('git rev-list HEAD').read().split()
    files = set()
    for commit in commits:
        tree_list = os.popen('git ls-tree -rl {}'.
                format(commit)).read().split('\n')
        for item in tree_list:
            if item:
                data, path = tuple(item.split('\t'))
                _, _, commit, size = data.split()
                if size == '-':
                    continue
                size = int(size)
                if size > size_limit:
                    files.add('size:{} commit: {}\npath: {}'.
                            format(size, commit, path))
    files = sorted(files, reverse=True)
    for f in files:
        print(f, end='\n\n')

if __name__ == '__main__':
    main(sys.argv)
