## Main Loop in JavaScript

 * Use form

        document.addEventListener('DOMContentLoaded', function(){
          'use strict';
          /* ... */
        });

 * This is the fastest of the pure JS methods of ensuring the DOM is ready: http://jsperf.com/onload-vs-domcontentloaded (accessed 20140727).
 * Note that use of jQuery [`ready{}`](http://api.jquery.com/ready/) is considerably faster:  http://jsperf.com/jquery-ready-vs-domcontentloaded (accessed 20140727).

[end]