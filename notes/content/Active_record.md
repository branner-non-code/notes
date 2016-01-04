## Active Record notes

 1. For every column in the database, Active Record provides getter and setter instance methods; they don't need to be specified manually.
 
 1. After create, migrate, seed, apparently need to `load 'config/environment.rb'` in Pry.
 
 1. Basic methods:
 
    * `all`
    * `find_by`
    * `where(<attribute>: <value>)` or `where(<SQL string>)` (cf. `pluck)
    * `order(<attribute>)`: use `:desc` etc.
    * `limit(<int>)`
    * `count`
    * `pluck(<attributes in series>)`
    * `first`
    * `find(<id>)`
    * `find_by(<attribute>)`
    * `qqq`
    * `qqq`
    * `qqq`
    * `qqq`


[end]