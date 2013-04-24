An S-expression (sexp for short) is the name for balanced parentheses (and the text they enclose) in Lisp. In Emacs, this useful notion is available in most modes; it's especially useful for editing programming languages. The characters that Emacs recognizes as parens are usually regular parentheses (aka round brackets), square brackets, and braces (aka curly brackets), but it depends on the mode (for some languages, angle brackets may act as parens).

But sexps are more than just balanced parens: they're defined recursively. A word that doesn't contain any parens also counts as a sexp. In most programming language modes, quoted strings are sexps (using either single or double quotes, depending on the syntax of the language). The sexp commands move in terms of all these units.

These commands may seem confusing at first, but for editing most programming languages they're fantastic. Not only do they move you around quickly and accurately, but they help spot syntax errors while you're editing, because they'll generate an error if your parens or quotes are unbalanced. 

http://www2.lib.uchicago.edu/keith/tcl-course/emacs-tutorial.html

[end]
