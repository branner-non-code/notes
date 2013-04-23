GitHub-flavored Markdown (GFMD)
===============================

General
-------

1.  ​20130225. GitHub has its own version of Markdown, called “GitHub
    Flavored Markdown” (GFM,
    <https://help.github.com/articles/github-flavored-markdown>), which
    differs from the standard version.

2.  ​20130227. I’ve asked whether they supply a real-time viewer
    comparable to <http://daringfireball.net/projects/markdown/dingus>.
    20130304. Brian Levine replied:

    > While we don’t have a live tool, per se, a lot of our editing
    > features include a preview function. So if you push a README.md
    > file that doesn’t look exactly the way you wanted, you could edit
    > it right there on GitHub. When you’re in edit mode, you can switch
    > back and forth between writing and previewing to make sure you
    > have it all polished up before committing your change. In fact,
    > that’s exactly what I do when writing and updating READMEs and
    > other non-code files here at GitHub.

3.  ​20130402. Python and other support for rednering GFMD: [http://stackoverflow.com/questions/7694887/]

Code blocks within lists
------------------------

2. The original Markdown specification explains this correctly:
    > To put a code block within a list item, the code block needs to be indented twice — 8 spaces or two tabs. (http://daringfireball.net/projects/markdown/syntax, accessed 20130423)

1. Github's site suggests incorrectly that only four spaces are necessary. (https://help.github.com/articles/github-flavored-markdown#fenced-code-blocks, accessed 20130423) But wrapping the code block in <CODE>```</CODE> top and bottom is effective.
