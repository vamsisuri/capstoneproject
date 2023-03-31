import time
def timer(fun):
    def wrapper(*kargrs,**kwargs):
        start_time=time.time()
        result=fun(*kargrs,**kwargs)
        end_time=time.time()
        print(end_time-start_time)
        print(result)
        return result
    return wrapper
@timer
def cal(a,b):
    return a/b
cal(10000000777777777777777777777777777777778,399999999999967896838838839399974848848477778858858.5555)

