## Check-in week ending 20130830

### **DONE**

   1. Mandarin dictionary project

     1. Converted record-modeling in the `Lookup` tools for my dictionary to `namedtuple` from unrelated variables. The field-names are contained in a list as a class attribute and the namedtuple is also instantiated as a class attribute.
     1. Began `add_entry` function, to be used at the command line.
     1. For `add_entry` function, found a way to update fields dynamically: https://github.com/brannerchinese/notes/blob/master/CONTENT/Python/Update_dynamically_chosen_field-names_in_database_record_modeled_as_namedtuple.md
     1. Added another Kivy tutorial video (Ben Rousch, looks very good) to list at https://github.com/brannerchinese/notes/blob/master/CONTENT/Kivy/Kivy_tutorials.md; have not yet watched.

   1. Ipython

     1. Had been having problems with Ipython under Python 2.7, and began wondering if they and the Kivy problems might not be related. So I reinstalled the OS, to which the Python 2.7 installation belongs, and now both Ipython and Kivy seem to be working. Now thinking again that Kivy may be a good tool for app-building, after all.
     1. Joined Ipython discussion list and pinned down my `autoreload` problem as deriving from the use of `PYTHONDONTWRITEBYTECODE`. Also found `nose` tests in the `iptest` suite that fail if XCode command-line tools have not been installed. 
     1. Wrote to Ipython maintainer about contributing to open source project; he suggested a fix to the cause of the `PYTHONDONTWRITEBYTECODE` problem. I've printed the `autoreload` code but am not yet sure how to proceed.
 
   1. Sinology

     1. Sketched out simple POS-tagging and mark-up system for Classical Chinese and began applying it to two late fifth-century texts (one *pyanwen* by Ren Faang, one *fuh*). I will try to do a little of this every day. Created new private repo for the prosody project.
     1. Collected material for other Ren Faang, Lii Sy, Tzou Yang works, convenient for tagging manually on subway.
     1. Doing a little of character-structure dictionary every day. No repo yet; need to get existing FMP database rationalized as SQL; waiting till tools are ripe for Mandarin dictionary project, clone afterwards. 
     1. [Neglected to mention last week: Prepared _Yuhlaan shy_ content (initially collated in May, right after Hacker School) for incorporation into database. Created new private repo for this project.]
     1. [Neglected to mention last week: Answered question about missing rime-names for student who is collating rhyming records for me.]

   1. Advising

     1. Contacted undergraduate student; he has not yet made any commits to the private repo I set up for his thesis content, so I don't know what use he may have made of the LaTeX template I constructed for him or the 20 comment-files I pushed. He is promising commits soon, however.
     1. Gave the Undergraduate Directors read-only access to the repo; to date they have not signed in.
     
   1. Math
   
     1. Vectors: Two hours reviewing Calc III vector material from 2012; had been thinking of registering for a course, but would be insanity this term.
     2. Linear Algebra: Began Philip Klein's Coursera course "Coding the Matrix- Linear Algebra through Computer Science Applications" (Coursera 2013 July). Late, but still of interest and useful for exercise. Finished the `functions` unit on 20130829. Began flashcards on `functions` unit and posted one question to discussion group.

### **TO DO**

   1. Need to write new script to generate LaTeX version for collaborator. Pīnyīn-separator tool will be useful for Pīnyīn index for this.
   1. Need to write `update_record` function for dictionary — this is the most important and complicated remaining task.
   1. Need to get started with Kivy, pronto.

[end]
