Templating and formatting
=========================

Escaping for LaTeX
------------------

1.  ​20130214. More efficient to use an ordered dictionary for this, as
    one only needs to add a single key-value pair rather than a whole
    new line, when a new case is added. Current code:

        import collections as C
        def escape_for_latex(a_string):
            """Perform simple text replacements for LaTeX compatibility."""
            # Using ordered dictionary in case order of replacement matters.
            # HTML forms probably rare in Beautiful Soup output, but retained in case.
            the_dict = C.OrderedDict([\
                    ('&amp;', '\\&'), \
                    ('&gt;', '>'), \
                    ('&lt;', '<'), \
                    ('&', '\\&'), \
                    ('$', '\\$'), \
                    ('%', '\\%'), \
                    ('#', '\\#'), \
                    (' "', ' ``'), \
                    (" '", " `"), \
                    ('"', "''"), \
                    ('\xa0', ' ')])
            # Next: add curly quotes to this list?
            for key in the_dict:
                a_string = a_string.replace(key, the_dict.get(key))
            return a_string

[end]
