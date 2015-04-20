# Enter your code here. Read input from STDIN. Print output to STDOUT

def isClassCancelled(students, must_attend, student_times):
    student_counter = 0
    for time in student_times:
        if time <= 0:
            student_counter = student_counter + 1
        else:
            continue
    
    if int(student_counter) < int(must_attend):
        print "YES"
        return
    else:
        print "NO"
        return

if __name__=='__main__':
    test_cases = raw_input()
    for _ in range(int(test_cases)):
        students, must_attend = raw_input().split()
        student_times = map(int, raw_input().split(" "))
        isClassCancelled(students, must_attend, student_times)


        
