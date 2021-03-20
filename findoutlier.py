#! python3
# findoutlier.py - looks through a list of even or odd numbers and returns the outlier.

def find_outlier(integers):
    
    # Will check if there are any odd numbers in the list
    oddCount = 0
    for n in integers:
        if n % 2 != 0:
            oddCount += 1
    
    # If there are odd numbers then go through the list again and return the odd number
    if oddCount == 1:
        for n in integers:
            if n % 2 != 0:
                return n
            
    # If odd numbers were not identified then go through the list and return the even number         
    else:
        for n in integers:
            if n % 2 == 0:
                return n
    
x = find_outlier([2, 4, 10, 6, 8, 99])
print(x)