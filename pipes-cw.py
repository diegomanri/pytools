# My solution for CodeWars "Lario and Muigi Pipe Problem"

def pipe_fix(nums):
    first = nums[0]
    last = nums[-1]
    newlist = []
    for pipes in range(first, last+1):
        newlist.append(pipes)
    return newlist

dlist = [2,3,6,7,8,13]
print(pipe_fix(dlist))

# Other user solutions
# def pipe_fix(nums):
    #return list(range(nums[0], nums[-1] + 1))