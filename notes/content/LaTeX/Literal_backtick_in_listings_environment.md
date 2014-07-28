## Literal backtick in `listings` environment

To prevent a backtick character from being typeset as a curly open single quote, use

    \usepackage{upquote}			% preserves backticks in verbatim environments
    \usepackage{listings}			% allows good verbatim text for code (only)
    \lstset{upquote=true,breaklines=true}

However, in the presence of `\usepackage{mathspec}` seems to disable this functionality. I have resorted to `verbatim` rather than `listings` in such places.

[end]
