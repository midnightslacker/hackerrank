#!/usr/bin/py
def lonelyinteger(numArray):
    newArray = []
    answer = 0
    for number in numArray:
        if number in newArray:
            newArray.remove(number)
        else:
            newArray.append(number)
    return newArray[0]

if __name__ == '__main__':
    a = input()
    array = map(int, raw_input().strip().split(" "))
    print lonelyinteger(array)

