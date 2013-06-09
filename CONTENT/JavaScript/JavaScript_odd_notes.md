## JavaScript odd notes

 1. Toggle boolean
 
        boolean = !boolean

 1. Output to console
 
        console.log(...)

 1. Call function on page load
 
        <body onload="initialize()"> // assumes script already loaded in head

 1. Declare global variables:
  *  Declare them on default object by prepending `this.` to each of them.
  *  Better still prepend `global.`, but place this at the head of the file:

            var global = this;
 
 1. `document.body` is null
  * because `body` element has not yet been created when it is already being fetched
  * place script at end of `body`
[end]
