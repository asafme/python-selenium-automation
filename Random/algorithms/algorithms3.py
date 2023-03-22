# when given a list, the program should return a list of all the elements below the original list's arithmetical mean.

n_list = [1, 3, 5, 6, 4, 10, 2, 3]
n = len(n_list)

get_sum = sum(n_list)
mean = get_sum/n

print("mean is:" + str(mean))


# when given a list of elements, find the two lowest elements. they can be equal to each other or different.


arr = [111, 13, 25, 9, 34, 1]
n = len(arr)
arr.sort()

print("smallest element is "+str(arr[0]))
print("second smallest element is "+str(arr[1]))









