Unpacking a list of lists
=========================

With nested loops
-----------------
~~~
a_list = []
b_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
for item in b_list:
    for subitem in item:
        a_list.append(subitem)
print(a_list)
: [1, 2, 3, 4, 5, 6, 7, 8]
~~~

Better:

~~~
a_list = []
b_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
for item in b_list:
    a_list.extend(item)
print(a_list)
: [1, 2, 3, 4, 5, 6, 7, 8]
~~~

With nested comprehensions
--------------------------
~~~
b_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
[subitem for item in b_list
    for subitem in item]
: [1, 2, 3, 4, 5, 6, 7, 8]
~~~

