# Notes

## [Search markdown files here](http://htmlpreview.github.io/?https://github.com/brannerchinese/notes/blob/master/searchPage.html)

A simple indexer for Markdown files stored in a GitHub repository. No server-side support or database is needed, although an index must be generated using Python (not on GitHub).

V. 0.1, 20130506


## To Use
Index markdown files are indexed in your local repo using `index_git.py`, which runs under Python v. 2.7 (in order to make use of the NLTK library). There is no database or server-side support. The index is stored as two large JavaScript objects in the `JS/` directory.

When your local repo is pushed to GitHub, the link "Search markdown files here" will open a new page with a search form, from which searches of the .md file titles, directories, and headers can be done.


---
  
## The Notes on This Site
The notes on this site are for my own use and may be of little interest. Most involve either syntax or solutions to problems.

The earliest material in this collection was composed in LaTeX but converted to Markdown using [PanDoc](http://johnmacfarlane.net/pandoc). Most material since then has been written from scratch or converted from [MoinMoin markdown](http://moinmo.in/ParserMarket/Markdown).

## Browser support
Works on 
 * Chrome (tested on v. 26.0.1410.65, 20130507)
 * Safari (tested on v. 6.0.4 [8536.29.13], 20130507)

Works imperfectly on 
 * Firefox (tested on v. 20.0, 20130507)


## Future tasks
1. Names beginning with a dot should be indexed both with and without the dot.
1. Second search does not work on Firefox; page never finishes reloading. Why?
2. `document.write()` is deprecated; can you translate to `innerHTML`?

[end]
