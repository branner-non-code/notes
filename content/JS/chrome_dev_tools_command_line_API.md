## Chrome Dev Tools Command Line API

Summarizing https://developer.chrome.com/devtools/docs/commandline-api, accessed 20140716.

### Basic control

 * new line w/o executing script: `shift-enter`
 * clear console history: `clear()`; also `console.clear()`, `cmd-k`, `^-l` (ell)
 * toggle CPU profiling session : `profile([name])`/`profileEnd([name])`; can be nested

### DOM elements

 * most recently evaluated expression: `$_`
 * last five selected DOM elements: `$0` - `$4`
 * first DOM element with `selector`: `$(selector)`
 * array of elements that match `selector`: `$$(selector)`; `document.querySelectorAll()`
 * array of DOM elements with `path` XPath expression: `$x(path)`

### Objects

 * select `object`: `inspect(object)`
 * copy string representation of `object`: `copy(object)`
 * object-style listing of `object`'s properties: `dir(object)`; `console.dir()`
 * return array of `object`'s properties: `keys(object)`
 * return array of `object`'s values: `values(object)`
 * XML representation of `object`: `dirxml(object)`; `console.dirxml()`
 * return event listeners on `object`: `getEventListeners(object)`
 * toggle logging of events on `object`: `monitorEvents(object[, "events"])` / `monitorEvents(object[, "events"])` (`events` can be single string or array of strings)
 * tabulate object contents: `table(object[, columns])`
 * return array of values of all properties of `object`: `values(object)`

### Functions

 * select `function`: `inspect(function)`
 * toggle logging function name and arguments: `monitor(function)` / `unmonitor(function)`
 * toggle debugger on `function`: `debug(function)` / `undebug(function)`

 * XPath expression: qqq

[end]