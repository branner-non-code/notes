In a default WordPress blog template, intended for posting of simple text alone, the `<code>` tags work, but some HTML and CSS tools are helpful for improving the appearance.

1. `&nbsp;` is needed for each space before the first ASCII character at the start of the line. Otherwise the ASCII will appear at the left margin. For displaying Python this is unhelpful.

1. Line- and paragraph-spacing is better suited to text than to code. I have been using the HTML content

```
<code style="font-size:small;">
<p style="line-height:100%;">
```

with reasonable effects in the Quintus template.

[end]
