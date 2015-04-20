# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/py
def countCuts(array):
    sortedArray = sorted(array)
    if len(sortedArray) < 1:
        return
    newArray = []
    cutLen = sortedArray[0]
    counter = 0
    for x in sortedArray:
        x = x - cutLen
        newArray.append(x)
        counter+=1
    print counter
    
    while 0 in newArray:
        newArray.remove(0)
    
    countCuts(newArray)
    

if __name__ == '__main__':
    a = input()
    array = map(int, raw_input().strip().split(" "))
    countCuts(array)


