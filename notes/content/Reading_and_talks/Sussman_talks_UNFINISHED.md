Gerald Jay Sussman on Flexible Systems, The Power of Generic Operations

https://vimeo.com/151465912

Every programmer spends most of his life fixing code that is already built. That should be easy — the hard part should be coming up with new ideas. The model is EMACS.

Traditional mathematics is a natural language.

c. 34:00

48:00


This is very flexible, and yet there are still lots of constraints here — this is not a completely unconstrained system.

```scheme
(let ((g (generic-arithmetic numeric-arithmetic)))
  (add-to-generic-arithmetic! g numeric-arithmetic)
  (add-to-generic-arithmetic! g (function-arithmetic numeric-arithmetic))
  (add-to-generic-arithmetic! g (symbolic-arithmetic numeric-arithmetic))
  (install-arithmetic! g))

(+ 1 'a 3)
;Value (+ (+ 1 a) 3)

(pp (x 0 ((evolver F 'h stormer-2) numeric-a0 1)))
(+ 9.999833334166664e-3
   (+ (/ (expt h 2) 12)
      -9.999750002487318e-7))

(+ 'a ((+ cos sin) 3))
;Value (+ a -.8488724885405782)

(+ 'a ((+ cos sin) 'b))
;Error!
```

So I'll give you some examples of what I might do. [46:42] For example, here's how I might make myself a package like this. I might make a `generic-arithmetic` out of a `numeric-arithmetic` package — so I'm pulling up a bunch of operations this time — but now I'm going add `numeric-arithmetic` to it. Here [initially] I'm just picking out the operation **names** [from the `numeric-arithmetic` package]; here [second] I'm saying: for every operation name, add the numerical stuff; here [third] I'm going to add the function arithmetic over the numerical stuff; here [fourth] I'm going to add the symbolic arithmetic over the numerical stuff; and [fifth] I'm going to install that, and I get lots of things, except one bug, and we'll worry about that in a second.

Degeneracy in biological systems: multiple pathways to get the same result. Not the same as redundancy: many copies of the same machine; degeneracy is many different machines that do approximately the same thing. That's a very powerful thing to build into programs and we don't do it very often. Graceful degradation by having more than one way to solve the same problem, so that if any of the ways fail

Strategy: I could imagine writing many ways





---

From the RC talk on 20160829:

Among Sussman's bons mots this evening I transcribed imperfectly: "Data is just a stupid kind of program that can tell you what it is when you ask it," ascribed to "Stanley Greenberg (?)".

Does anyone have better information and/or better recall than I do about either the phrase or the person?

I find a related quip on line attributed to Bill Gosper: "A data structure is just a stupid programming language," but I'm pretty sure Sussman didn't mention Bill Gosper.

---

Real programmers program in make.

"I'm an engineer. I want *every* one of these tools."

The thing that interests me is not to eliminate bugs beforehand but to be able to find and fix them quickly. I'm interest in rapid repair.
