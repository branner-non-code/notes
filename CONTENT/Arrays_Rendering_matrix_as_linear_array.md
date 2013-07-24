## Rendering a matrix as a linear array

Rendering a matrix as a linear array is a procedure common in generations of programming languages predating Python. How do I convert between the index of the linear array and the coordinates row and column of the corresponding matrix?

Matrix showing linear array-indices of matrix-cells:

~~~
row_number: +—————————————————+

    2       | 8 | 9 | 10 | 11 |

            +———+———+————+————+

    1       | 4 | 5 |  6 |  7 |

            +———+———+————+————+

    0       | 0 | 1 |  2 |  3 |

            +—————————————————+

              0 | 1 |  2 |  3    <= column_number

  total_rows  = 3
  total_columns = 4
~~~

Three small calculations are needed to convert between an index and the corresponding row_number and column_number:

~~~
    index = row_number * total_columns + column_number
    column_number = index % total_columns
    # Python 3, non-integer division
    row_number = (index - column_number) / total_columns
    # Alternately, by integer division
    row_number = index // total_columns
~~~

[end]
