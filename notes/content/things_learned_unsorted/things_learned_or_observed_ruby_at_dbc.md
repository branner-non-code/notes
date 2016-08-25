Orange Tree 1. Many Students have:

```ruby
def mature?
  if @age >= 5
    true
  else
    false
  end
end
```

This could be boiled down to:

```ruby
def mature?
  @age >= 5
end
```

First, `age >= 5` will be evaluated, either `true` or `false`, and after that the value will be assigned to `@mature`.

Similarly:

```ruby
def has_oranges?
  unless @oranges.empty?
    return true
  else
    return false
  end
end
```

can just become 

```ruby
def has_oranges?
  !@oranges.empty?
end
```

---

Orange Tree 1. Student has:

```ruby
[2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2].sample
```

Can rewrite as

```ruby
rand(2.5..3.2).round(1)
```

---

Orange Tree 1. Many Students fail to use argument-order independence, including `args.fetch(key, default_value)` consistently. The nuisance is that you always have to pass in a hash, but let that become your habit. 

Also, many students

---

Orange Tree 1. Student neglects to write tests. 

---

Orange Tree 1. Student fails to eliminate commented-out code before pull request.

---

Orange Tree 1. Use of `reduce` to find average:

```ruby
average = (items.reduce(0) {|sum, n| sum + n.diameter}) / item.length
```

---

In conversation with Chris. A range can be used as a hash key, but finding the key to which a given integer belongs is a function of the hash keys as array, and does not make use of the intrinsic efficiency of a hash:

```ruby
>> h = {(0..9) => 'a', (10..19) => 'b'}
=> {0..9=>"a", 10..19=>"b"}
>> h.select {|k| k.include?(3)}
=> {0..9=>"a"}
>> h.select {|k| k.include?(13)}
=> {10..19=>"b"}
```

---

To empty an array, rather than creating a new array and assigning it:

```ruby
a.clear
```

Note that this method is destructive, even without the use of `!`.

---

At time of Ruby Todos challenges, some students are still using `require` etc. for CSV and other files.

---

`Float::INFINITY`

---

`===` in case statements.

---

When to use `require` and `require_relative`, etc.

---

Examples of planning unit tests.

---

[end]