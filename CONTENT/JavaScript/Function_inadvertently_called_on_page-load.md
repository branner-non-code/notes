### Function inadvertently called on page-load

Function, when assigned to an event handler, omits `()`; otherwise, will be called on page-load. 

* Correct:

            var theButton = document.createElement('button');
            theButton.onclick=showMe;

            function showMe() {console.log('here');}
  * It would be incorrect to use

            theButton.onclick=showMe();
    or
    
            theButton.onclick='showMe()';  

[end]
