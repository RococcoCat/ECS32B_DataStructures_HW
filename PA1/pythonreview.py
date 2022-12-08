import itertools

def findWithSum(arr, val, num=0):
    output = {}
    combs = list(itertools.combinations(arr, num)) # all the diff. combinations of nums in arr of len num
    # if sum of the combo equals the value, make a dict with the key as the index of the number in arr and the values are the numbers that sum to value
    for comb in combs:
        if sum(comb) == val:
            for i in set(comb):
                for j in range(comb.count(i)):
                    # index of output will be next occurence of i in arr
                    indices = [a for a, x in enumerate(arr) if x == i] # get list of indices for each number in the combo
                    output[indices[j]] = i 

    return output
