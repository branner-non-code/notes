## Ruby: Ways to strip trailing carriage return (`\r`) and/or newline (`\n`) from lines in a file

Assume a basic pattern like this:

```ruby
file = 'db/fixtures/words'
collection = []
File.readlines(file).each do |line|
  collection << line
end
```

How do we get rid of end-of-line characters on each line?
    
 1. With Ruby's idiomatic `chomp` method:
 
    ```ruby
    collection << line.chomp
    ```
    
 1. With a standard-looking string-substitution method:
 
    ```ruby
    collection << line.gsub("\n", '')
    ```
    
    But if line is terminated in `\r\n`, which can happen on some systems, you will be removing the `\n` but leaving the `\r` intact — undesirable.

 1. With the `strip` method:
 
    ```ruby
    collection << line.strip
    ```
    
    `strip`, however, will also remove leading and trailing whitespace from each `line` — which you may or may not want.

 1. With the `delete` method:
 
    ```ruby
    collection << line.delete!("\n")
    ```

[nd]