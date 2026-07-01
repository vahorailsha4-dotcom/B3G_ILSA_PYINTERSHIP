import time 
def timer(func):
    def wrapper():
        start=time.time()
        result=func()
        end=time.time()
        print("Time Taken:",end-start,"Seconds")
        return result
    return wrapper
@timer
def calc_sum():
    total=0
    for i in range(1,1000001):
        total+=1
    print("Sum:",total)
calc_sum()