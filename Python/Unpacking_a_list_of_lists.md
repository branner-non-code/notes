Unpacking a list of lists
=========================

With nested loops
-----------------
~~~
a_list = []
b_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
for i in b_list:
    for j in i:
        a_list.append(j)
print(a_list)
: [1, 2, 3, 4, 5, 6, 7, 8]
~~~

Better:

~~~
a_list = []
b_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
for i in b_list:
    a_list.extend(i)
print(a_list)
: [1, 2, 3, 4, 5, 6, 7, 8]
~~~

With nested comprehensions
--------------------------
~~~
[j for i in b_list
    for j in i]
: [1, 2, 3, 4, 5, 6, 7, 8]
~~~

