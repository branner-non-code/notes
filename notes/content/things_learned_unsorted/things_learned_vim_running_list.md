## Things Learned, Vim (running list)

 1. Iterate through past cursor positions: `^-o` to move back, `^-i` to move forward. History is lost when buffer is closed.

 1. If you want to convert text to lowercase, create a visual block and press u (or U to convert to uppercase).

 1. Use `^f` to make the Vim command line into a sub-buffer navigable with Vim itself.

 1. To replace in Vim with something repeated:

        :'<,'>s/^/\=repeat(' ', 8)/g

 1. For a list of functions like `repeat` use `:h function-list`:

        ```
        FUNCTIONS                                               *function-list*

        There are many functions.  We will mention them here, grouped by what they are
        used for.  You can find an alphabetical list here: |functions|.  Use CTRL-] on
        the function name to jump to detailed help on it.

        String manipulation:                                    *string-functions*
          nr2char()         get a character by its ASCII value
          char2nr()         get ASCII value of a character
          str2nr()          convert a string to a Number
          str2float()       convert a string to a Float
          printf()          format a string according to % items
          escape()          escape characters in a string with a '\'
          shellescape()     escape a string for use with a shell command
          fnameescape()     escape a file name for use with a Vim command
          tr()              translate characters from one set to another
          strtrans()        translate a string to make it printable
          tolower()         turn a string to lowercase
          toupper()         turn a string to uppercase
          match()           position where a pattern matches in a string
          matchend()        position where a pattern match ends in a string
          matchstr()        match of a pattern in a string
          matchlist()       like matchstr() and also return submatches
          stridx()          first index of a short string in a long string
          strridx()         last index of a short string in a long string
          strlen()          length of a string
          substitute()      substitute a pattern match with a string
          submatch()        get a specific match in a ":substitute"
          strpart()         get part of a string
          expand()          expand special keywords
          iconv()           convert text from one encoding to another
          byteidx()         byte index of a character in a string
          repeat()          repeat a string multiple times
          eval()            evaluate a string expression
        ```

 1. Set Python to use 4-column tabs instead of four spaces, in all indentation:

        au BufRead,BufNewFile *.py,*.pyw set tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab

 1. Set Vim to print on US Letter paper with appropriately small margins:

        au BufRead,BufNewFile *.py set printoptions=number:y,left:2pc,right:2pc,paper:letter

    But note that sometimes "letter" is not what the paper you want is called on your printer, and a different word is needed!

 1. In Sublime, can use Vim bindings with `Vintage`: change
 
    ```
    {
        "ignored_packages": ["Vintage"]
    }
    ```

    to

    ```
    {
        "ignored_packages": [""]
    }
    ```

 1. Close all buffers but this one:
 
    ```vim
    :on
    ```

 1. Close all buffers:
 
    ```vim
    :qa
    ```
    
    To save all dirty files:
    
    ```vim
    :xa
    ```

 1. Open temporary shell
 
    ```vim
    :sh
    ```

 1. Folding
 
    2. Unfold one level: `zm`
    2. Fold one level: `zr`
    2. Unfold all levels: `zM`
    2. Fold all levels: `zmR

---

### Already moved to Notes on line.

 1. Sort in Vim: `:<range>sort`; use option `u` to do Unix sort, removing duplicate lines.
 1. To find the name of the current file:

        :echo @%

 1. To count occurrences of a match without changing them:

        :%s/item//n

   The option `n` makes this a dry run.

 1. Create `.inputrc` file with `set editing-mode vi` and `set keymap vi`, in order to have vim key-commands in many command-line programs. (E.g., Ipython).
 1. Set Python to use 4-column tabs instead of four spaces, in all indentation:

        au BufRead,BufNewFile *.py,*.pyw set tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab

 1. Set Vim to print on US Letter paper with appropriately small margins:

        au BufRead,BufNewFile *.py set printoptions=number:y,left:2pc,right:2pc,paper:letter

[end]
