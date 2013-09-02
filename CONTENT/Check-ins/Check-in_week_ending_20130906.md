## Check-in for week ending 20130906

### Mandarin Dictionary
 
   1. Last week I modularized a number of functions that were shared by different parts of my code. I put them all in a `dictionary_utils.py` module in a `Utils` directory and imported the module into each program where they were used. Although I found only a 5% difference in speed when I tested the basic principle (see https://github.com/brannerchinese/notes/blob/master/CONTENT/Python/Import_functions_on_object.md), the code to populate SQL databases from a FMP dump has gone from 50 seconds to 260 seconds, an unacceptable increase perhaps due to the many `execute` statements involved. **UPDATE**:The steep slow-down was because in the `dictionary_utils.py` version of one function I changed `LIKE` to `=` in the SQL code. In fact, I need both `LIKE` and `=` in different situations, so I added a class attribute, `comparison`, which is set to `LIKE` if we are doing inexact (regex, wildcard) search and `=` if we are doing exact search. In the look-up program this is done by the `change_ndx_xact` function; in the dump-import program this is set once when the `Lookup` object is instantiated and left as is.
   2. As much shared material as possible is now being moved to `UTILS`.
   2. Began using `JOIN`s in some places where I was previously executing two consecutive SQL statements. This is not yet done in the generic SQL functions, however.
   3. From the command line, new functionality when adding an entry:
     * program retrieves the traditional and simplified forms of the desired character-expression;
     * if more than one traditional/simplified pair exists, user gets to choose which is desired;
     * user can set the POS of the entry, which is chosen from a fixed list.
   1. While creating a new entry, those fields that have tentatively been populated are shown with both the relevant record ID number and the actual intended content. On commit, only the former will be used. 

[end]
