## JQuery content introduced in CodeCademy lessons

[edited 20140511]

Reference: http://jquery.com/.

All code begins with:

    $(document).ready(function() {});

### Effects

 * `fadeOut([<speed>])`
 * `fadeIn([<speed>])`
 * `fadeTo(<speed>, <opacity>)`
 * `slideDown(<speed>)`
 * `slideUp(<speed>)`
 * `slideToggle([<speed>])`
 * `hide()`
 * `remove()`
 * `append()`
 * `prepend()`
 * `appendTo()`
 * `prependTo()`
 * `after()`
 * `before()`
 * `empty()`
 * `addClass(<class name>)`
 * `removeClass(<class name>)`
 * `toggleClass(<class name>)`
 * `width()`
 * `height()`
 * `animate({<action>, <time>})`

 * `<speed>` can be:
   * `'slow'`
   * `'fast'`

### Events

 * `mouseenter(<function>)`
 * `mouseleave(<function>)`
 * `click(<function>)`
 * `dblclick(<function>)`
 * `focus(<function>)`
 * `keydown(<function>)`
 * `hover(<function1>, <function2>)`


### Miscellaneous

 * compound selectors: `$('p, li')`
 * event handlers: `this`

### Getters and setters

 * `html([<new contents>])`: Get the HTML contents of the first element in the set of matched elements, and replace them with `<new contents>`.
 * `css(<property>, <value>)`: http://api.jquery.com/css/
 * `val([<value>])`: Get or set the current value of the first element in the set of matched elements. http://api.jquery.com/val/
 * `on()`: general handler that takes the event, its selector, and an action as inputs. http://api.jquery.com/on/


### jQuery UI 

See http://jqueryui.com/

 * `effect('explode')`
 * `effect('bounce', {times:<times>}, <within_milliseconds>)`
 * `accordion({collapsible:<bool>, active:<bool>})`
 * `draggable()`
 * `resizable()`
 * `selectable()`
 * `sortable()`

[end]