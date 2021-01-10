import random
def quicksort(array):
    if len(array) < 2:
        return array
    else: 
        #pivot = array[0]
        pivot = array[random.randint(0,len(array)-1)]
        #print(random.randint(0,len(array)-1))
        #print(pivot)
        less = [i for i in array[0:] if i < pivot]
        greater = [i for i in array[0:] if i > pivot]
        #print(less)
        #print(greater)
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3, 123, 231 ,325, 234]))