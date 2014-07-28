# Notes

## [Search markdown files here](https://branner-non-code.github.io/notes/notes/searchPage.html)

A simple indexer for Markdown files stored in a GitHub repository. No server-side support or database is needed, although an index must be generated using Python (not on GitHub).

V. 0.3, 20140728.

## To Use
Index markdown files are indexed in your local repo using `index_git.py`, which runs under Python v. 2.7 (in order to make use of the NLTK library). There is no database or server-side support. The index is stored as two large JavaScript objects in the `js/` directory.

When your local repo is pushed to GitHub, the link "Search markdown files here" will open a new page with a search form, from which searches of the .md file titles, directories, and headers can be done.

  
## The Notes on This Site
The notes on this site are for my own use and may be of little interest. Most involve either syntax or solutions to problems.

The earliest material in this collection was composed in LaTeX but converted to Markdown using [PanDoc](http://johnmacfarlane.net/pandoc). Most material since then has been written from scratch or converted from [MoinMoin markdown](http://moinmo.in/ParserMarket/Markdown).

## Browser support
Works on 
 * Chrome (tested on v. 36.0.1985.125, 20140728)
 * Firefox (tested on v. 31.0, 20140728)
 * Safari (tested on v. 7.0.5 [9537.77.4], 20140728)

## Future tasks
 1. Names beginning with a dot should be indexed both with and without the dot.
 1. Search results should be better organized.
 1. Also search for left-substrings of search string.
 1. Ought also to be searching for individual words in pages.

## New this version
 1. JS revised after GitHub changes made `searchPage.html` non-functional in 2014 Spring. Errors fixed and IIFE and main loop added.
 1. Link revised from original [http://htmlpreview.github.io/?](http://htmlpreview.github.io/?) form, which no longer works. Now using `gh-pages`.
 1. Now works on Chrome.
 1. Whole project also moved to subdirectory `notes`.

## Previous versions
V. 0.2, 20130528

 1. Second search now works on Firefox.
 1. Replaced all `document.write()` with `innerHTML`.
 1. Did not work on Chrome (tested on v. 27.0.1453.93, 20130528; GitHub now serving JS from `raw.github.com` using MIME type `text/plain`. (see https://plus.google.com/+MikeWest/posts/28f8HS2M7cb). Consider solution discussed at https://github.com/mrdoob/three.js/issues/3292: explicitly call `.js` scripts from `rawgithub.com` so they aren't served from `raw.github.com`.

V. 0.1, 20130506 (original)

[end]
