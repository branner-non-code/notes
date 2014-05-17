## JavaScript and jQuery things learned

 - Supply pre-set value for variable if it is undefined. `n = n || 10`. Compare Python
 
        if not n:
            n = 10
 
 - `<script>` line in HTML calling Bootstrap must come after the line calling jQuery, since the latter is a dependency.
 - One form can have multiple input elements. Calling `submit()` on the form will respond to a submit event on any of those elements.
 
 
 - Make table fill scrren, use `{width: 100%; table-layout: fixed;}`.
 - Combine input box and field with other content in form, but formatted differently smaller than headings: use `span` and make heading part of `<form id='form'>` but not part of `<span id='inputs'>`.
 - Ensure that lists of items within a single table cell are vertically aligned under headings: use `td {vertical-align: top;}`. Otherwise lists may be centered vertically.
 - Separation between table and browser-window edges, and between the two lists in the window: `table {border-spacing: 10px} td {padding: 10px}`.

[end]