## Check-in for week ending 20130906

 1. Mandarin Dictionary
 
   1. Last week I modularized a number of functions that were shared by different parts of my code. I put them all in a `dictionary_utils.py` module in a `Utils` directory and imported the module into each program where they were used. Although I found only a 5% difference in speed when I tested the basic principle (see https://github.com/brannerchinese/notes/blob/master/CONTENT/Python/Import_functions_on_object.md), the code to populate SQL databases from a FMP dump has gone from 50 seconds to 260 seconds, an unacceptable increase perhaps due to the many `execute` statements involved. I keep thinking that I've made some other mistake that has slowed everything down, but a careful reading this morning failed to find anything. So I am going to move the farmed-out functions back into their original calling programs.
   
[end]
