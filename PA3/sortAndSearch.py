import time
import copy
import csv
import math
import json

def main():
    pass
    # write outputs to file
    input_data = []
    """
    with open(r_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            input_data.append(line.strip())
    """
    
    # df = pd.read_csv('data.csv')
    # ls_date_price = df.values.tolist()
    ls_date_price = []
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csvreader)
        for row in csvreader:
            ls_date_price.append(row)

    

    """date = list(df['Date'])
    price = list(df['Price'])"""
    with open('queries.json','r') as f:
        x = json.load(f)
    queries = [i for i in x]
    with open("output.csv", "w") as csvfile:
        exec1 = linear_search(queries, ls_date_price)[0]
        arr1 = linear_search(queries, ls_date_price)[1]
        
        exec2 = bubbleSort(ls_date_price)[0]
        arr2 = bubbleSort(ls_date_price)[1]
        
        exec3 = selectionSort(ls_date_price, len(ls_date_price))[0]
        arr3 = selectionSort(ls_date_price, len(ls_date_price))[1]
        
        exec4 = BinarySearch(queries, ls_date_price)[0]
        arr4 = BinarySearch(queries, ls_date_price)[1]
        
        
        writer = csv.DictWriter(csvfile, fieldnames = ['Name','Time','Output']) 
        writer.writeheader()
        writer.writerow({'Name': 'Linear Search', 'Time':exec1 , 'Output':list(arr1) })
        writer.writerow({'Name': 'Bubble Sort', 'Time':exec2 , 'Output':list(arr2) })
        writer.writerow({'Name': 'Other Sort', 'Time':exec3 , 'Output':list(arr3) })
        writer.writerow({'Name': 'Other Search', 'Time':exec4 , 'Output':list(arr4) })
        
     
        
def linear_search(queries, array):
    start = time.time()
    arr = []
    for i in queries:
        for j in range(len(array)):
            if array[j][1] == i:
                arr.append(array[j]) 
                break
                
    end = time.time()
    exec_time = end - start
    return [exec_time,arr]

def bubbleSort(ls):    
    # record start time
    start = time.time()
    arr = ls.copy()
    n = len(arr) 
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.time()
    exec_time = end - start
    return [exec_time,arr]

def selectionSort(ls, size):
    start = time.time()
    arr = ls.copy()
    for s in range(size):
        min_idx = s         
        for i in range(s + 1, size):             
            # For sorting in descending order
            # for minimum element in each loop
            if arr[i][1] < arr[min_idx][1]:
                min_idx = i 
        # Arranging min at the correct position
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])
    end = time.time()
    exec_time = end - start
    return [exec_time,arr]

def BinarySearch(queries, ls):
    start = time.time()
    arr = []
    for val in queries:
        first = 0
        last = len(ls)-1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first+last)//2
            if ls[mid][1] == val:
                index = mid
                arr.append(ls[index])
                break
            else:
                if val<ls[mid][1]:
                    last = mid -1
                else:
                    first = mid +1
    end = time.time()
    exec_time = end - start
    return [exec_time,arr]
