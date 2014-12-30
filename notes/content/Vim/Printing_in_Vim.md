## Printing in Vim

Set Vim to print on US Letter paper with appropriately small margins:
 
        au BufRead,BufNewFile *.py set printoptions=number:y,left:2pc,right:2pc,paper:letter

Printing is done with the

    :ha

command, assuming a printer has already been set up.

[end]
