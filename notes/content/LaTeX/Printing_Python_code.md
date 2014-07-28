Printing Python code with LaTeX
===============================

Use the `listings` package:

        \usepackage{color}
        \definecolor{dark-green}{rgb}{0.2, 0.8, 0.2}
        \usepackage{listings}
        \lstset{language=Python,basicstyle=\ttfamily\footnotesize,frame=lines,captionpos=b,tabsize=4,keywordstyle=\color{blue},commentstyle=\color{dark-green},stringstyle=\color{red},numbers=left,numberstyle=\tiny,numbersep=5pt,breaklines=true,showstringspaces=false}

The environment is simply `lstlisting`.

[end]
