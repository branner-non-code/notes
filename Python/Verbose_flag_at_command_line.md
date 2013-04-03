verbose flag at command line
----------------------------

```
class Chinese_checker(object):
    def __init__(self, verbose):
        self.verbose = None

    def debug_print(self, *args, end='\n'):
        '''Print special debugging messages if -v flag is set at start-up.'''
        if self.verbose:
            print(*args, end='\n')

def main(verbose=False):
    # etc.

if __name__ == '__main__':
    main(verbose='-v' in sys.argv)
```
