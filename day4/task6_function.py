def find_sum(n):
    if n==1:
        return 1    
    else:
        return n+find_sum(n-1)    
n=21
print("The Number is:",n)        
print("Sum of Number 1 to n:",find_sum(n))
