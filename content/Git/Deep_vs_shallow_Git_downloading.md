## Deep vs shallow Git downloading

 1. When cloning a repository, you can omit its past history by cloning as:

        git clone <repo> --depth=1

   Numbers higher than `1` here include successively larger numbers of past commits.

 1. If past history is needed, it is possible to retrieve the whole set of past commits with

        git fetch --unshallow

[end]
