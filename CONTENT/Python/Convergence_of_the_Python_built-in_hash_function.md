## Convergence of the Python built-in hash function

Python's build-in hash function includes some randomization, with the effect, I think of preventing its average from converging rapidly when applied to strings.

I tested it by successively concatenating strings of 'a' and taking the `hash()`, then finding the mean and standard deviation of the hashes.

~~~
import numpy
import sys
            
def main(s='', hashes = []):
    while True:
        try:
            s += 'aaaaaaaaaaaaa'
            hashes.append(hash(s))
            cardinality = len(hashes)
            if not cardinality % 10000:
                print('{:10d}: avg.: {:> 8.2e}, s.d. {:> 8.2e}'.
                        format(cardinality, numpy.mean(hashes),
                            numpy.std(hashes)))
        except KeyboardInterrupt:
            print('\n',len(hashes))
            sys.exit(0)

In [1]: HC.main()
     10000: avg.:   5.64e+16, s.d.   5.32e+18
     20000: avg.:   5.81e+16, s.d.   5.31e+18
     30000: avg.:   5.34e+16, s.d.   5.32e+18
     40000: avg.:   4.79e+16, s.d.   5.31e+18
     50000: avg.:   2.98e+16, s.d.   5.32e+18
     60000: avg.:   1.80e+16, s.d.   5.32e+18
     70000: avg.:   1.13e+16, s.d.   5.32e+18
     80000: avg.:   7.74e+15, s.d.   5.33e+18
     90000: avg.:   1.36e+16, s.d.   5.33e+18
    100000: avg.:   1.91e+16, s.d.   5.33e+18
    110000: avg.:   2.31e+16, s.d.   5.33e+18
    120000: avg.:   2.01e+16, s.d.   5.33e+18
    130000: avg.:   1.42e+16, s.d.   5.33e+18
    140000: avg.:   1.07e+16, s.d.   5.33e+18
    150000: avg.:   1.08e+16, s.d.   5.32e+18
    160000: avg.:   1.63e+16, s.d.   5.33e+18
    170000: avg.:   1.90e+16, s.d.   5.33e+18
    180000: avg.:   2.43e+16, s.d.   5.33e+18
    190000: avg.:   2.38e+16, s.d.   5.33e+18
    200000: avg.:   2.26e+16, s.d.   5.33e+18
    210000: avg.:   2.38e+16, s.d.   5.33e+18
    220000: avg.:   2.55e+16, s.d.   5.33e+18
    230000: avg.:   2.27e+16, s.d.   5.33e+18
    240000: avg.:   2.42e+16, s.d.   5.33e+18
    250000: avg.:   2.24e+16, s.d.   5.33e+18
    260000: avg.:   1.81e+16, s.d.   5.33e+18
    270000: avg.:   1.54e+16, s.d.   5.33e+18
    280000: avg.:   1.36e+16, s.d.   5.33e+18
    290000: avg.:   1.07e+16, s.d.   5.33e+18
    300000: avg.:   1.30e+16, s.d.   5.33e+18
    310000: avg.:   1.28e+16, s.d.   5.33e+18
    320000: avg.:   1.26e+16, s.d.   5.33e+18
    330000: avg.:   1.12e+16, s.d.   5.33e+18
    340000: avg.:   1.09e+16, s.d.   5.33e+18
    350000: avg.:   1.05e+16, s.d.   5.33e+18
    360000: avg.:   1.12e+16, s.d.   5.33e+18
    370000: avg.:   1.28e+16, s.d.   5.33e+18
    380000: avg.:   1.43e+16, s.d.   5.33e+18
    390000: avg.:   1.35e+16, s.d.   5.33e+18
    400000: avg.:   1.16e+16, s.d.   5.33e+18

~~~

Even though the built-in hash function hashes strings to both positive and negative integers, the mean in this case varies around a large positive number, rather than 0.

For comparison, here are the same procedures carried out on MD5:

~~~
# MD5.py
import numpy
import sys
import hashlib                                                                  
 
def main(s='', hashes = []):
    while True:
        try:
            s += 'aaaaaaaaaaaaa' 
            temp = hashlib.md5(s.encode())
            temp = int(temp.hexdigest(), 16)
            hashes.append(temp)
            cardinality = len(hashes)
            if not cardinality % 10000:
                print('{:10d}: avg.: {:> 8.2e}, s.d. {:> 8.2e}'.
                        format(cardinality, numpy.mean(hashes),
                            numpy.std(hashes)))
        except KeyboardInterrupt:
            print('\n',len(hashes))
            sys.exit(0)

In [1]: M.main()
     10000: avg.:  1.70e+38, s.d.  9.80e+37
     20000: avg.:  1.71e+38, s.d.  9.85e+37
     30000: avg.:  1.71e+38, s.d.  9.86e+37
     40000: avg.:  1.71e+38, s.d.  9.84e+37
     50000: avg.:  1.71e+38, s.d.  9.85e+37
     60000: avg.:  1.71e+38, s.d.  9.84e+37
     70000: avg.:  1.71e+38, s.d.  9.83e+37
     80000: avg.:  1.71e+38, s.d.  9.83e+37
     90000: avg.:  1.71e+38, s.d.  9.84e+37
    100000: avg.:  1.71e+38, s.d.  9.83e+37
~~~

and on SHA256:

~~~
# SHA256.py
import numpy                                                                    
import sys
import hashlib
 
def main(s='', hashes = []):
    while True:
        try:
            s += 'aaaaaaaaaaaaa' 
            temp = hashlib.sha256(s.encode())
            temp = int(temp.hexdigest(), 16)
            hashes.append(temp)
            cardinality = len(hashes)
            if not cardinality % 10000:
                print('{:10d}: avg.: {:> 8.2e}, s.d. {:> 8.2e}'.
                        format(cardinality, numpy.mean(hashes),
                            numpy.std(hashes)))
        except KeyboardInterrupt:
            print('\n',len(hashes))
            sys.exit(0)

In [1]: SHA256.main()
     10000: avg.:  5.76e+76, s.d.  3.32e+76
     20000: avg.:  5.77e+76, s.d.  3.33e+76
     30000: avg.:  5.79e+76, s.d.  3.34e+76
     40000: avg.:  5.78e+76, s.d.  3.34e+76
     50000: avg.:  5.77e+76, s.d.  3.34e+76
     60000: avg.:  5.77e+76, s.d.  3.34e+76
     70000: avg.:  5.78e+76, s.d.  3.34e+76
     80000: avg.:  5.77e+76, s.d.  3.34e+76
     90000: avg.:  5.77e+76, s.d.  3.34e+76
    100000: avg.:  5.78e+76, s.d.  3.34e+76

~~~
