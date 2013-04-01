Random lists of characters
--------------------------

1.  ​20130311. I had thought of specifying a range of codepoints and
    converting them to characters:

        chr(R.randint(32, 126))

    which works well for Chinese. But Marek changed that to this, which
    is better for ASCII:

        R.choice(string.ascii_letters)

    I wrote a piece of code to time the two:

        def both(x):
            start = T.time()
            for i in range(x):
                a = R.choice(string.ascii_letters)
            print('R.choice(string.ascii_letters)', T.time() - start)
            start = T.time()
            for i in range(x):
                a = chr(R.randint(32, 126))
            print('chr(R.randint(32, 126))', T.time() - start)

        In [21]: both(10000000)
        R.choice(string.ascii_letters) 69.98532509803772
        chr(R.randint(32, 126)) 109.04312491416931

    Marek’s is much faster.

[end]
