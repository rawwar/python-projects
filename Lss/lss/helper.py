import time
# import cProfile


# Used as a decorator to measure time taken for executing a function
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print '%r  %2.2f ms' %(method.__name__, (te - ts) * 1000)
        return result
    return timed

# cProfile.run('interactive_input([r"H:\Git\python-projects\Lss\data1"])')