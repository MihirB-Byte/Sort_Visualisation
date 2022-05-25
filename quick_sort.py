def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower

def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)
    
def quicksort(xs):
    _quicksort(xs, 0, len(xs)-1)
    return xs

"""
user_inputs = [int(x) for x in input("Enter multiple values seperated with comma : ").split(" ")] #getting multiple values from the user seperated by space
print("the list is : " + str(user_inputs))

Sorted_list=quicksort(user_inputs)
print("Sorted list : " + str(Sorted_list)) """