def my_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0]+my_sum(arr[1:])

print(my_sum([2,3,4,5,6,7,8]))