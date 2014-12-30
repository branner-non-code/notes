## Python: Name of active or previously called function

### Most recently called function

    import inspect
    inspect.stack()[0][3]

### Previous called function

    inspect.stack()[1][3]

I have put the following two functions in a utility module:

    def prepare_report(self):
        '''Used with report() to tell what work was done by a function.'''
        self.start_time = time.time()
        
    def report(self, table):
        '''Used with prepare_report() to tell what work was done by a function.'''
        print('Function {} done with {:.2f} seconds spent in all.'.
                format(inspect.stack()[1][3], time.time() - self.start_time))

When `report()` is called, it reports not itself but the function that called it.

[end]
