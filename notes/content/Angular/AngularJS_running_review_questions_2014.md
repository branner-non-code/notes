
 * 1.2.3.Q1: How would you explain the basics of templating in Angular?

   * —

 * 1.2.3.Q2: What is the purpose of each of the Angular components we listed in the introduction to this reading? How do you use each of those components?

    * `ng-init`: set initial scope
    * `{{ }}`: demarcate expression within template
    * `ng-app`: declare the start of AngularJS usage
    * `ng-repeat`: looping
    * `ng-click`: like `onClick`
    * `ng-model`: apparently to declare variable
    * `filter`: impose stricture on 
    * `ng-if`: flow-control based on condition
    * `ng-switch`: introduce flow-control block based on condition
    * `ng-switch-when`: flow-control statement based on value
    * `ng-switch-default`: end flow-control block
    * `ng-class`: dynamically set CSS classes
    * `ng-submit`: directive for submit-buttons

 * 1.2.3. tight coupling:

   * High interdependence by classes or other components.

 * 1.2.4.Q1: What is binding?

   * The existence of pigeonholes in the View where data from the Model can be inserted.

 * 1.2.4.Q2: What is the purpose of the braces in Angular templates?

   * To indicate where in the view some data from the model is to be inserted.

 * 1.2.4.Q3: Give some examples of expressions that can be evaluated in an Angular template.

   * string concatenation, arithmetic

 * 1.2.4.Q4: The video recommends that you not put much logic in your Angular templates. Why do you think this is?

   * To keep the structure modular and to keep View and Model separate.

 * 1.2.4.Q5: How can you use data binding in Angular to set a CSS class?

   * By replacing the name of a class with a double-brace-delimited expression. Use `ng-class`.

 * 1.2.5.Q1: Can you describe what a filter does in Angular?

   * It restricts the expression of some object to a subset of that object's content.

 * 1.2.5.Q2: What's the syntax for filters?

        {{ object | filter}}

 * 1.2.5.Q3: Can you use more than one filter? 

   * By chaining.

 * 1.3.1.Q1: What is a controller?

   * Connect markup to data.

 * 1.3.1.Q2: How do you link to a controller in your HTML file?

   * Wrap code-block in `div ng-controller="name"></div>`, where `name` is a JS function.

 * 1.3.1.Q3: How do you link a controller to a DOM element?

   * `ng-controller="name"` in tag

 * 1.3.1.Q4: What's the syntax for declaring a controller?

   * `ng-controller="name"` in tag

 * 1.3.2.Q1: What's the purpose of a module?

   * to modularize (segregate) code into discrete pieces

 * 1.3.2.Q2: What's the syntax for defining a module?

        angular.module('myApp', [any_dependencies]);

 * 1.3.2.Q3: How do you link a module with an HTML template?

        <html ng-app="myApp">
        <script src="myApp.js"></script>

 * 1.3.2.Q4: Explain the concept of scope. Make sure you can describe what is meant by "parent" and "child" scope.

   * Data and methods that are available (as key-value pairs, name: data/method) in some subset of the code; scopes are hierarchical, parent scope being a superset of child scope

 * 1.3.2.Q5: What is a controller?

   * a kind of submodule, used for containing "bite-sized blocks of code"

 * 1.3.2.Q6: What's the syntax for defining a controller?

        angular.module('myApp', []) ... ..controller('MyCtrl', function() {});

 * 1.3.2.Q7: Explain what you do with $scope and $rootScope in Angular.

   * `$scope`: local scope of some controller
   * `$rootScope`: the top-level scope of the document

 * 1.3.2.Q8: How do you define a constant value for a module?

   * Call `.constant()` on a module, e.g.:

       `angular.module('myApp', []).constant('VERSION', 1.1);`

 * 1.3.4.Q1: Explain `$attrs` and `initial-attr-values`. How would you use this in a controller and template, and what's the advantage?
 
   * `$attrs`: container (key-value map) in a controller for initial values set for the controller in the template;
   * `initial-attr-values`: example of a `initial-dash-spaced-name` declaration made in the template.
   * These two elements can pass data from the template to the controller.

 * 1.3.4.Q2: How can you share state across controllers in Angular?

   * By use of `$scope.$emit` and `$rootScope.$broadcast`.

 * 1.3.4.Q3: Explain the difference between emitting and broadcasting an event in Angular.

   * `$broadcast` sends data down to children
   * `$emit` sends data up to parents (until 

        $scope.$on('show', function(event, data) {
          event.stopPropagation();
        }

     is encountered)

 * 1.4.1.Q1: What's the difference between CSS transitions and keyframe animations?

   * Keyframe animations are a kind of transition, but also allow for checkpoints (where special CSS can be applied for short durations), and for reversals and looping.

 * 1.4.1.Q2: What is the transition property shorthand for?

   * Long lists of parallel properties (` transition-property`, `transition-duration`, `transition-timing-function`, and `transition-delay`).

 * 1.4.1.Q3: What do the following transition parameters control? property, duration, timing-function, and delay

   * (as named)

 * 1.4.1.Q4: How can you detect when a transition has completed?

   * `transitionend` event fires.

 * 1.4.1.Q5: How do you use @keyframes at rules?

   * "They all link some type of condition, which at any time evaluates to either true or false. If the condition evaluates to true, then all of the statements within the group will be applied." (https://developer.mozilla.org/en-US/docs/Web/CSS/At-rule)

 * 1.4.1.Q6: How do you make an animation loop?

   * Use a keyframe.

 * 1.4.1.Q7: How could you implement a loading image animation?

   * Spinner?

 * 1.4.1.Q8: What is GreenSock?

   * Animation library dedicated to JavaScript animations and offers a variety of specialized features like animation paths, staggered animations, and timelines

 * 1.4.1.Q9: How would you animate an element using jQuery?

   * Use `.animate()`.


 * 1.4.2.Q1: What file do you need to include in a script tag in your templates to use ngAnimate?

   * `src="angular-1.2/angular-animate.js"`
   * See "Remastered Animation in AngularJS."

 * 1.4.2.Q2: What are the 'ng-' prefixed CSS classes you write rules for to achieve animations?

   * `.ng-enter`
   * `.ng-leave`
   * `.ng-move`
   * `.ng-enter-active`
   * `.ng-leave-active`
   * `.ng-move-active`
   * See "Remastered Animation in AngularJS."

 * 1.4.2.Q3: How could you animate an ng-hide call?

   * `$animate.addClass('ng-hide')`
   * `$animate.removeClass('ng-hide')`
   * See "Remastered Animation in AngularJS."

 * 1.4.2.Q4: How do you attach multiple animation events to a CSS class using JavaScript animations?

   * "Multiple animation events can be attached to a single CSS class (since animations are class based)."
   * See "Remastered Animation in AngularJS."

 * 1.4.2.Q5: How do you include ngAnimate as a dependency for your module?

   * "Include the `angular-animate.js` file (which is apart of the downloadable zip file present on the angularjs.org website or within the code.angularjs.org listing page) into your webpage and reference the ngAnimate module inside of your application module."

        `var myApp = angular.module('MyApp', ['ngAnimate']);`

     See "Remastered Animation in AngularJS."

 * 1.4.2.Q6: Give the starting and ending CSS classes for each of the following events: enter, leave, move.

   * `.ng-enter`
   * `.ng-leave`
   * `.ng-move`
   * `.ng-enter-active`
   * `.ng-leave-active`
   * `.ng-move-active`
   * See "Remastered Animation in AngularJS."

 * 1.4.2.Q7: How do animations work with ng-repeat?

   * "The ngRepeat directive fires off the enter, leave and move events when items are inserted into, removed from, and moved around within the repeated list of items. All that you have to do is have a CSS class present and apply the matching Transition, Keyframe or JavaScript animation code to handle the animation on that CSS class value."
   * See "Remastered Animation in AngularJS."

 * 1.4.2.Q8: What is a staggered animation?

   * "A stagger is an animation that occurs that contains a delay between each successive animation which causes a "curtain-like" effect to occur."
   * See "Staggering Animations in AngularJS."

 * 1.4.2.Q9: Give a code example that uses staggered animation.

   * See "Staggering Animations in AngularJS."


[end]