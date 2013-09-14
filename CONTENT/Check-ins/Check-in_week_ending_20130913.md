## Check-in week ending 20130913

### Mandarin dictionary

 1. LaTeX output now fully working. 

### Review of technical matter

 Goal: implement various data structures and algorithms using simple Python structures.

 1. Sorting
   1. `mergesort` working.
   1. `quicksort` working.
   1. `insertionsort` working. Timing the sorting of lists of integers, ascending and descending, shows different time complexities, as described on the README page.
 1. Hash tables
   1. Using built-in `hash()`, but since it produces negative numbers, add `sys.maxsize` to its output, so that every hash is positive, without increasing collision rate.
   1. Tried implementing direct hash table using class attributes instead of array. However, this is cheating, since class attributes are stored in a dictionary internally. Must use array of some sort.
   1. Found useful discussions of Python dictionary implementation:
     * http://stackoverflow.com/a/8272643/621762
     * http://stackoverflow.com/a/9022664/621762
 
 
### To Do

#### Mandarin dictionary

 1. Refactor command-line output.
 1. Refactor genertic SQL commands — some can be combined as joins.
 1. 

#### Review of technical matter

 1. Hash tables — both direct and chained models. Must decide when to resize array, and by how much.
 1. Heaps.
 1. Binary search tree.
