## Basic Haskell keywords

### main, putStrLn

`main` has to be the last function of a program:

```hs
main = putStrLn "Hello, World!"
```

or

```hs
fac n = if n == 0 then 1
        else n * fac (n-1)

main = print (fac 10)
```

or

```hs
main = do
        let fac n = if n == 0 then 1
                else n * fac (n-1)
        print (fac 10)
```

(Note use of `let` here.)

### putStrLn vs. print

`print x` is `putStrLn show(x)`.

`show` converts strings to their unicode representation in order to display them. So `putStrLn` is preferable for printing strings (followed automatically by a newline).

```hs
Prelude> putStrLn "我"
我
Prelude> print "我"
"\25105"
Prelude> show "我"
"\"\\25105\""
```

[end]