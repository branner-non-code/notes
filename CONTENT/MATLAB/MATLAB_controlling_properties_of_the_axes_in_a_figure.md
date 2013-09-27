## MATLAB - controlling properties of the axes in a figure


http://www.mathworks.com/support/solutions/en/data/1-15HXQ/ (20120128)

For XLim, XTick, or XTickLabel:
{{{
set(gca, 'XLim', array)
set(gca, 'XTick', array)
set(gca, 'XTickLabel', array)}}}

Note that {{{gca}}} is the handle of the axes in the current figure; use {{{gcf}}} for the current figure or {{{gco}}} for the current object (but then XLim, XTick, and XTickLabel are not involved).

In the case of XTickLabel, {{{array}}} must be either an array of strings (delimited by []) or a cell array of strings (delimited by {}).

Note that you can use XLim to show slightly past the boundaries of the array used in XTick; increase or decrease the values appropriately. GGG can this be automated? is there a setting for this?

"gca" stands for "get current axes".

[end]
