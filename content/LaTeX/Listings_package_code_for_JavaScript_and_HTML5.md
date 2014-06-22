## Listings package code for JavaScript and HTML5

From Jonas Nyrup (http://tex.stackexchange.com/a/99607/3935, accessed 20130727):

~~~
\usepackage{color}
\usepackage{upquote}
\usepackage{listings}
\lstdefinelanguage{JavaScript}{
  morekeywords={var, function},
  morecomment=[s]{/*}{*/},%
  morecomment=[l]//,%
  morestring=[b]",%
  morestring=[b]'%
}

\lstdefinelanguage{HTML5}[]{HTML}{
    sensitive=false,
    morekeywords={canvas},
    tag=[s]
}

\lstset{%
    % Basic design
    basicstyle={\small\ttfamily},
    % Code design   
    keywordstyle=\color{blue}\bfseries,
    stringstyle=\color{red},
    % Code
    language=HTML5,
    tabsize=2,
    showtabs=false,
    showspaces=false,
    showstringspaces=false,
    extendedchars=true,
    breaklines=true
}
~~~

[end]
