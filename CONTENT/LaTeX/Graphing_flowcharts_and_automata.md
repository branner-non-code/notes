## Graphing flowcharts and automata with Dot in LaTeX

The language Dot describes graphs in plain text. It is used with the Graphviz graphic application; both were originally developed at Bell Labs.

Below are a few notes on surprises I had when working with .dot and .svg (“Scalable Vector Graphics”, a standard XML-based format for graphs) files in Python:

 * For viewing .svg files, desktop installations of Ubuntu use the Gnome viewer “Eye of GNOME” (eog) by default.
 * Ubuntu’s (Lucid) server installation of graphviz does not include a viewer by default. You can display .svg files using Firefox; set the browser to about:config and confirm that you have the setting svg.smil.enabled;true and place an entry in your ~/.mailcap file:

 ```
image/svg+xml; firefox
```

 Of course, you can also install `eog` on your server.
 * The current Mac version of Graphviz (v. 2.28) has no trouble opening a .dot file, but apparently it cannot open .svg files.

For use within LaTeX documents, it is possible to do everything native packages or (more interestingly) to incorporate Graphviz output by converting it to a native format:

 * The native LaTeX tools for producing flowcharts and automata are the tikz and pstricks packages. TikZ, which has more comprehensive support, supplies a library called automata (see the TikZ manual for detailed instructions. There is also a third library, VauCanSon-G, but it appears to have less functionality.
 * There is a Python module, dot2tex by Kjell Magne Fauske, that converts .dot and other Graphviz formats to TikZ or pstricks.
 * Fauske has also written a LaTeX package, dot2texi, that allows .dot (etc.) graphical output to be embedded directly in a LaTeX document.

---

[This is transfered from a post on my blog at (http://brannerchinese.wordpress.com/2011/11/13/graphing-flowcharts-and-automata-in-latex/), dated 20111113.]
