Simple procedure to choose the correct typeface, depending on which of them actually contains the required characters — without manually changing the typeface.

Solution
--------

posted 20110420 by Leo Liu

~~~
\documentclass[nofonts]{ctexart}
\setCJKmainfont{SimSun}
\newfontfamily\songextb{SimSun-ExtB}
\def\CJKsymbol#1{%
  \iffontchar\font`#1%
    #1%
  \else
    {\songextb#1}%
  \fi}

\begin{document}
漢字源𣴑
\end{document}
~~~
