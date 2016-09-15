# Eric Raymond’s 17 Unix Rules

## Rule of Clarity

 * Clarity is better than cleverness.

 * Developers should write programs as if the most important communication is to the developer, including themselves, who will read and maintain the program rather than the computer. This rule aims to make code readable and comprehensible for whoever works on the code in future.


## Rule of Composition

 * Design programs to be connected with other programs.

 * Developers should write programs that can communicate easily with other programs. This rule aims to allow developers to break down projects into small, simple programs rather than overly complex monolithic programs.


## Rule of Diversity

 * Distrust all claims for one true way.

 * Developers should design their programs to be flexible and open. This rule aims to make programs flexible, allowing them to be used in ways other than those their developers intended.


## Rule of Economy

 * Programmer time is expensive; conserve it in preference to machine time.

 * Developers should value developer time over machine time, because machine cycles today are relatively inexpensive compared to prices in the 1970s. This rule aims to reduce development costs of projects.


## Rule of Extensibility

 * Design for the future, because it will be here sooner than you think.

 * Developers should design for the future by making their protocols extensible, allowing for easy plugins without modification to the program's architecture by other developers, noting the version of the program, and more. This rule aims to extend the lifespan and enhance the utility of the code the developer writes.


## Rule of Generation

 * Avoid hand-hacking; write programs to write programs when you can.

 * Developers should avoid writing code by hand and instead write abstract high-level programs that generate code. This rule aims to reduce human errors and save time.


## Rule of Least Surprise

 * In interface design, always do the least surprising thing.

 * Developers should design programs that build on top of the potential users' expected knowledge; for example, ‘+’ in a calculator program should always mean 'addition'. This rule aims to encourage developers to build intuitive products that are easy to use.


## Rule of Modularity

 * Write simple parts connected by clean interfaces.

 * Developers should build a program out of simple parts connected by well defined interfaces, so problems are local, and parts of the program can be replaced in future versions to support new features. This rule aims to save time on debugging code that is complex, long, and unreadable.


## Rule of Optimization

 * Prototype before polishing. Get it working before you optimize it.

 * Developers should prototype software before polishing it. This rule aims to prevent developers from spending too much time for marginal gains.


## Rule of Parsimony

 * Write a big program only when it is clear by demonstration that nothing else will do.

 * Developers should avoid writing big programs. This rule aims to prevent overinvestment of development time in failed or suboptimal approaches caused by the owners of the program’s reluctance to throw away visibly large pieces of work. Smaller programs are not only easier to optimize and maintain; they are easier to delete when deprecated.


## Rule of Repair

 * Repair what you can — but when you must fail, fail noisily and as soon as possible.

 * Developers should design programs that fail in a manner that is easy to localize and diagnose or in other words “fail noisily”. This rule aims to prevent incorrect output from a program from becoming an input and corrupting the output of other code undetected.


## Rule of Representation

 * Fold knowledge into data, so program logic can be stupid and robust.

 * Developers should choose to make data more complicated rather than the procedural logic of the program when faced with the choice, because it is easier for humans to understand complex data compared with complex logic. This rule aims to make programs more readable for any developer working on the project, which allows the program to be maintained.


## Rule of Robustness

 * Robustness is the child of transparency and simplicity.

 * Developers should design robust programs by designing for transparency and discoverability, because code that is easy to understand is easier to stress test for unexpected conditions that may not be foreseeable in complex programs. This rule aims to help developers build robust, reliable products.


## Rule of Separation

 * Separate policy from mechanism; separate interfaces from engines.

 * Developers should separate the mechanisms of the programs from the policies of the programs; one method is to divide a program into a front-end interface and a back-end engine with which that interface communicates. This rule aims to prevent bug introduction by allowing policies to be changed with minimum likelihood of destabilizing operational mechanisms.


## Rule of Silence

 * When a program has nothing surprising to say, it should say nothing.

 * Developers should design programs so that they do not print unnecessary output. This rule aims to allow other programs and developers to pick out the information they need from a program's output without having to parse verbosity.


## Rule of Simplicity

 * Design for simplicity; add complexity only where you must.

 * Developers should design for simplicity by looking for ways to break up program systems into small, straightforward cooperating pieces. This rule aims to discourage developers’ affection for writing “intricate and beautiful complexities” that are in reality bug prone programs.


## Rule of Transparency

 * Design for visibility to make inspection and debugging easier.

 * Developers should design for visibility and discoverability by writing in a way that their thought process can lucidly be seen by future developers working on the project and using input and output formats that make it easy to identify valid input and correct output. This rule aims to reduce debugging time and extend the lifespan of programs.

[end]