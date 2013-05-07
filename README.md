# Notes

## Search Form
[Search markdown files here](http://htmlpreview.github.io/?https://github.com/brannerchinese/notes/blob/master/tester.html)

A simple indexer for Markdown files stored in a GitHub repository. No server-side support or database is needed, although an index must be generated using Python (not on GitHub).


## To Use
Index markdown files are indexed in your local repo using `index_git.py`, which runs under Python v. 2.7 (in order to make use of the NLTK library). There is no database or server-side support. The index is stored as two large JavaScript objects in the `JS/` directory.

When your local repo is pushed to GitHub, the link "Search markdown files here" will open a new page with a search form, from which searches of the .md file titles, directories, and headers can be done.

## The Notes on This Site
The notes on this site are for my own use and may be of little interest. Most involve either syntax or solutions to problems.

The earliest material in this collection was composed in LaTeX but converted to Markdown using [PanDoc](http://johnmacfarlane.net/pandoc). Most material since then has been written from scratch or converted from [MoinMoin markdown](http://moinmo.in/ParserMarket/Markdown).

[end]
