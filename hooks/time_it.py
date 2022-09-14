import time


def time_it(function):
    n = time.process_time()
    function()
    elapsed_time = time.process_time() - n
    return elapsed_time
