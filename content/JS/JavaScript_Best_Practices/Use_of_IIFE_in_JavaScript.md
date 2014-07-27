## Use of IIFE in JavaScript

 * IIFE "immediately-invoked function expression" is pronounced "iffy" (Thomas Hudspith-Tatham).
 * The main loop of the program can usefully be placed inside the IIFE, together with variable declarations. All functions can be placed outside the IIFE.
 * **Rationale**: 
   * Avoid creation of global properties. The IIFE mimics global scoping for important global properties while in fact operating within a local scope. 
   * Namespacing. Properties can be assigned names in local scope that are protected from conflict with the same names in other libraries.
   * Speed. Since properties are looked up locally first, making global properties local can save some look-up time.
   * Minification. Global properties can be assigned to minimal-length variable names within the IIFE.
 * **Format**: At the beginning of the file, use:
 
        ;(function (...) {
          /* Variable declarations */
          /* Main loop of program */
        })(...);
 
   * Code placed within `()` is evaluated as an expression at runtime, so placing a function within `()` evaluates it immediately. 
   * Other unary operators (`!`, `+`, `-`, `~`) can also be used, but `()` is normal practice. 
   * The initial `;` is a safeguard in case the present file begins with a closure and is concatenated to other JavaScript content that is missing a closing `;`.
 * Arguments useful to pass:
   * `window`
   * `document`
   * `undefined`: Under ECMA3 `undefined` was mutable and could be assigned a value. Including it in the parameter-list (but not the list of called arguments) prevents that. ECMA5 prevents the same thing with `'use strict';`.
   * jQuery: `window.jQuery` as argument in function call, `$` as parameter in function definition. jQuery uses `jQuery.noConflict();` for the same effect.

[end]