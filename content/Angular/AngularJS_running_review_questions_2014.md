
 * 1.2.3.Q1: How would you explain the basics of templating in Angular?

    

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

    High interdependence by classes or other components.

 * 1.2.4.Q1: What is binding?

    The existence of pigeonholes in the View where data from the Model can be inserted.

 * 1.2.4.Q2: What is the purpose of the braces in Angular templates?

    To indicate where in the view some data from the model is to be inserted.

 * 1.2.4.Q3: Give some examples of expressions that can be evaluated in an Angular template.

    string concatenation, arithmetic

 * 1.2.4.Q4: The video recommends that you not put much logic in your Angular templates. Why do you think this is?

    To keep the structure modular and to keep View and Model separate.

 * 1.2.4.Q5: How can you use data binding in Angular to set a CSS class?

    By replacing the name of a class with a double-brace-delimited expression. Use `ng-class`.

 * 1.2.5.Q1: Can you describe what a filter does in Angular?

    It restricts the expression of some object to a subset of that object's content.

 * 1.2.5.Q2: What's the syntax for filters?

    {{ object | filter}}

 * 1.2.5.Q3: Can you use more than one filter? 

    By chaining.

 * 1.3.1.Q1: What is a controller?

    Connect markup to data.

 * 1.3.1.Q2: How do you link to a controller in your HTML file?

    Wrap code-block in `div ng-controller="name"></div>`, where `name` is a JS function.

 * 1.3.1.Q3: How do you link a controller to a DOM element?

    `ng-controller="name"` in tag

 * 1.3.1.Q4: What's the syntax for declaring a controller?

    `ng-controller="name"` in tag

 * 1.3.2.Q1: What's the purpose of a module?

    to modularize (segregate) code into discrete pieces

 * 1.3.2.Q2: What's the syntax for defining a module?

    `angular.module('myApp', [any_dependencies]);`

 * 1.3.2.Q3: How do you link a module with an HTML template?

    <html ng-app="myApp">

    <script src="./myApp.js"></script>

 * 1.3.2.Q4: Explain the concept of scope. Make sure you can describe what is meant by "parent" and "child" scope.

    data and methods that are available (as key-value pairs, name: data/method) in some subset of the code; scopes are hierarchical, parent scope being a superset of child scope

 * 1.3.2.Q5: What is a controller?

    a kind of submodule, used for containing "bite-sized blocks of code"

 * 1.3.2.Q6: What's the syntax for defining a controller?

    `angular.module('myApp', []) ... ..controller('MyCtrl', function() {});`

 * 1.3.2.Q7: Explain what you do with $scope and $rootScope in Angular.

    `$scope`: local scope of some controller; `$rootScope`: the top-level scope of the document

 * 1.3.2.Q8: How do you define a constant value for a module?

    Call `.constant()` on a module, e.g.: `angular.module('myApp', []).constant('VERSION', 1.1);`

[end]