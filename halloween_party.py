# Enter your code here. Read input from STDIN. Print output to STDOUT

def maxCandy (numCuts):
    if numCuts%2==0:
        print (numCuts/2) * (numCuts/2)
    else:
        print (numCuts/2) * ((numCuts/2) + 1)

if __name__=='__main__':
    test_cases = raw_input()
    for _ in range(int(test_cases)):
        numCuts = int(raw_input())
        maxCandy(numCuts)
