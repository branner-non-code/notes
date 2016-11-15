## Running Haskell

### GHCi interpreter

Quit using `:q`.

 1. At prompt: `ghci` (installed as part of Haskell Platform). 

 1. Run `ghci` as:
 
    ```bash
    stack exec -- ghci
    ```

### Compiling and running Haskell code

```bash
ghc -o hello hello.hs
./hello
```

### Try Haskell (online code pen)

http://tryhaskell.org/

### Haskell Platform

> The Platform comes with GHC, the de-facto standard Haskell compiler, with many useful tools that will let you program Haskell painlessly. (https://wiki.haskell.org/Haskell_in_5_steps#Install_Haskell)

 1. Download from https://www.haskell.org/platform/

 1. Includes:

    * the Glasgow Haskell Compiler
    * the Cabal build system
    * the Stack tool for developing projects
    * support for profiling and code coverage analysis
    * 35 core & widely-used packages

### Haskell Stack

> Stack will automate the installation and management of the GHC compiler, libraries, and other build tools. (https://wiki.haskell.org/Haskell_in_5_steps#Install_Haskell)

 1. Download from https://haskell-lang.org/get-started. (accessed 20161025)

 1. Run as:

    ```bash
    stack new new-project
    cd new-project
    stack build
    stack exec new-project-exe
    ```

### Hugs

No longer actively maintained. (https://en.wikipedia.org/wiki/Haskell_(programming_language)#Implementations, accessed 20160125)

[end]