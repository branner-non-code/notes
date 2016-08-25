## Things Learned, Ubuntu (running list)

 1. Find available Ubuntu packages with `apt-cache search`.

 1. To list all installed packages on Ubuntu, use

        dpkg --get-selections

### Ideas

 1. Partitioning an integer is hard — good hard interview problem. See Tim Peters' solution at http://code.activestate.com/recipes/218332-generator-for-integer-partitions/. 
 
        def gen_partitions_ms(n):
            """Generate all partitions of integer n (>= 0).
        
            Each partition is represented as a multiset, i.e. a dictionary
            mapping an integer to the number of copies of that integer in
            the partition.  For example, the partitions of 4 are {4: 1},
            {3: 1, 1: 1}, {2: 2}, {2: 1, 1: 2}, and {1: 4}.  In general,
            sum(k * v for k, v in a_partition.iteritems()) == n, and
            len(a_partition) is never larger than about sqrt(2*n).
        
            Note that the _same_ dictionary object is returned each time.
            This is for speed:  generating each partition goes quickly,
            taking constant time independent of n.
            """
        
            if n < 0:
                raise ValueError("n must be >= 0")
        
            if n == 0:
                yield {}
                return
        
            ms = {n: 1}
            keys = [n]  # ms.keys(), from largest to smallest
            yield ms
        
            while keys != [1]:
                # Reuse any 1's.
                if keys[-1] == 1:
                    del keys[-1]
                    reuse = ms.pop(1)
                else:
                    reuse = 0
        
                # Let i be the smallest key larger than 1.  Reuse one
                # instance of i.
                i = keys[-1]
                newcount = ms[i] = ms[i] - 1
                reuse += i
                if newcount == 0:
                    del keys[-1], ms[i]
        
                # Break the remainder into pieces of size i-1.
                i -= 1
                q, r = divmod(reuse, i)
                ms[i] = q
                keys.append(i)
                if r:
                    ms[r] = 1
                    keys.append(r)
        
                yield ms

    Recursive solution at http://stackoverflow.com/a/10036764/621762:

        def partition(number):
            answer = set()
            answer.add((number, ))
            for x in range(1, number):
                for y in partition(number - x):
                    answer.add(tuple(sorted((x, ) + y)))
            return answer

    which I've rewritten as:

        def partition(n):
            result = {(n,)}
            result.update({tuple(sorted((summand,) + remainder))
                for summand in range(1, n)
                for remainder in partition(n-summand)
            })
            return result


 1. More practical problem: find a single interesting partition. Idea: generate random numbers between 1 and the remainder until they add up to n:

        import random
        
        def make_random_partition(n):
            """Return a partition of n, with reasonably small cardinality."""
            remainder = n
            summands = []
            while remainder:
                upper_bound = int(remainder * 1 /2) + 1
                summands.append(random.randint(1, upper_bound))
                remainder = remainder - summands[-1]
            # Test with assert sum(summands) == n
            assert sum(summands) == n
            return summands

---

### Already moved to Notes on line.

(None)

[end]
