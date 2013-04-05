Indexing
========

From command line
-----------------

Following http://tex.stackexchange.com/a/27299, accessed 20120723

To confirm that `makeindex` can be run from the command line, use

    which makeindex

which should return `/usr/texbin/makeindex`. If it doesn't, and returns nothing, then your TeX binaries aren't being found. (They are found by TeXShop because it sets its own path for all commands.)

Echoing the $PATH variable should show that it includes `/usr/texbin`

> As egreg notes, for multiple indices the package `imakeidx` is 
> useful, as it automates the run of `makeindex`.

Marking indexed text
--------------------

Following http://tex.stackexchange.com/a/64345/3935

~~~
\documentclass{article}
\makeindex
\makeatletter
\newcommand{\@theindexentry}[1]{%
  \smash{%
    \rlap{\rule{.4pt}{.8\baselineskip}}% Vertical rule
    \begin{lrbox}{\@tempboxa}\tiny\ttfamily#1\end{lrbox}% Box index entry
    \rlap{\raisebox{.6\baselineskip}{\usebox{\@tempboxa} }}% key
  }%
}
\def\@wrindex#1{%
  \protected@write\@indexfile{}%
    {\string\indexentry{#1}{\thepage}}%
  \endgroup
  \@esphack%
  \@theindexentry{#1}%
}
\def\@index#1{\endgroup\@esphack\@theindexentry{#1}}
\makeatother
\begin{document}
Lorem\index{Alpha} ipsum dolor sit amet, consectetur\index{alpha} adipiscing elit. 
Proin ullamcorper\index{gnat} quam magna, quis convallis\index{gnus!good} sapien. Donec 
at ligula vel dolor varius\index{bites!vegetable} lobortis id ut orci\index{gnat!size of}. Maecenas 
commodo fringilla elit\index{Alphabet}, et pellentesque purus ornare vitae. 
Aenean non metus ipsum. Lorem\index{gnat!anatomy} ipsum dolor sit amet, consectetur 
adipiscing\index{alphas} elit. Ut mauris lorem, accumsan a sagittis ut, 
rutrum fringilla arcu. Cras ullamcorper faucibus\index{alpha bet} quam id molestie.

Nunc et\index{alphabet} sem et turpis semper adipiscing et id nibh. In nibh 
mauris, placerat sed consequat placerat, dignissim ut\index{at!bat|see {bat, at}} arcu. 
Aenean eleifend justo volutpat lectus\index{gnus!bad} interdum pellentesque. 
Etiam cursus varius\index{twenty@xx} tellus, non pretium nibh tempus sit amet. 
Suspendisse sed mauris nisl. Cum sociis natoque penatibus et 
magnis dis parturient montes, nascetur\index{alpha@$\alpha$} ridiculus mus. Nullam 
at feugiat nisi\index{bites!animal!gnats}.
\end{document}
~~~

The writer continues:

> It prints, for every `\index`, a vertical rule showing the point of 
> reference, as well as the key used (minus `{` or `}`, for simplicity) 
> in `\tiny\ttfamily`. Using xcolor one could make the appearance less 
> intrusive by printing in `black!30` (say):

> `\@theindexentry` prints the index-related content. \smash takes care 
> of any vertical adjustment, while the entire index entry is set inside >
a zero-width `\rlap to remove any horizontal adjustment.

> The definition of `\@wrindex` (in the presence of `\makeindex`) and 
> `\@index` was taken directly from latex.ltx.
