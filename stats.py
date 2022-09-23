"""
Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. 
The median is the number that would appear at the midpoint of a list if it were sorted. 
The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. 
Also include a function named mean, which computes the average of a set of numbers. 
Each function expects a list of numbers as an argument and returns a single number.
"""


def mean(num):
    length = len(num)
    sum = 0
    if length == 0:
        return 0
    else:
        for n in num:
            sum = sum + n
            numMean = sum/length
        return numMean

def median(num):
    num.sort()
    length = len(num)
    mid = int(length/2)
    if length == 0:
        return 0
    else:
        if length % 2 == 1:                 #Evaluates whether the length of the array is odd or even.
            return num[mid]
        else:
            numMedian = (num[mid]+num[mid-1])/2
            return numMedian

def mode(num):
    length = len(num)
    if length == 0:
        return 0
    else:
        numMode = max(set(num), key = num.count)
        return numMode

def main(): 
    numList = [1, 2, 3, 4, 5, 5]
    
    print("List: ", numList, "\n")
    mean()
    median(numList)
    mode(numList)

    print("Mean: ", mean(numList))
    print("Median: ", median(numList))
    print("Mode: ", mode(numList))
    
if __name__ == '__main__':
    main()