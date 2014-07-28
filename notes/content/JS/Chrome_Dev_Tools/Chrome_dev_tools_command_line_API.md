## Chrome Dev Tools Command Line API

Summarizing 

 * https://developer.chrome.com/devtools/docs/commandline-api, accessed 20140716.
 * https://developer.chrome.com/devtools/docs/console-api, accessed 20140716.

### Basic console control

 * new line w/o executing script: `shift-enter`
 * clear console history: `clear()`; `console.clear()`; `cmd-k`; `^-l` (ell)
 * display message: `console.log(object [, object, ...])`; `console.info(object [, object, ...])`; `console.debug(object [, object, ...])`
   * first parameter may contain format specifiers, including
     * `%o`: expandable DOM element
     * `%O`: expandable JavaScript object
     * `%c`: CSS style
   * add warning icon: `console.warn(object [, object, ...])`
   * count log messages produced: `console.count(label_string)`
 * toggle CPU profiling session : `profile([name])`/`profileEnd([name])`; can be nested
 * toggle timer: `console.time(label)` / `console.timeEnd(label)`
 * toggle timeline recording: `console.timeline(label)` /
`console.timelineEnd()`
 * log time-stamp: `console.timeStamp([label])`


### DOM elements

 * most recently evaluated expression: `$_`
 * last five selected DOM elements: `$0` - `$4`
 * first DOM element with `selector`: `$(selector)`
 * array of elements that match `selector`: `$$(selector)`; `document.querySelectorAll()`
 * array of DOM elements with `path` XPath expression: `$x(path)`

### Objects

 * select `object`: `inspect(object)`
 * copy string representation of `object`: `copy(object)`
 * object-style listing of `object`'s properties: `dir(object)`; `console.dir(object)`; `console.log("%O", object)`; `console.error(object [, object, ...])` (includes stack trace)
 * return array of `object`'s properties: `keys(object)`
 * return array of `object`'s values: `values(object)`
 * XML representation of `object`: `dirxml(object)`; `console.dirxml(object)`
 * return event listeners on `object`: `getEventListeners(object)`
 * toggle logging of events on `object`: `monitorEvents(object[, "events"])` / `monitorEvents(object[, "events"])` (`events` can be single string or array of strings)
 * log stack trace: `console.trace([object])`
 * tabulate object contents: `table(object[, columns])`
 * evaluate truth of `object`: `console.assert(expression, object)`
toggle logging group: `console.group(object[, object, ...])` or `console.groupCollapsed(object[, object, ...])` / `console.groupEnd()`

### Functions

 * select `function`: `inspect(function)`
 * toggle logging function name and arguments: `monitor(function)` / `unmonitor(function)`
 * toggle debugger on `function`: `debug(function)` / `undebug(function)`
 * start debugging session: `debugger`; note: not a method of `console`

### Other

 * toggle JavaScript CPU profile: `console.profile([label])` / `console.profileEnd()`

[end]
