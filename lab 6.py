print 'how many numbers do you want to add together'
userinput = int(raw_input())
total = 0
for x in range(userinput):
    print 'enter a number:'
    userinput = int(raw_input())
    total = total + userinput
print 'your answer is'
print total

alist = []
for x in range(userinput):
    print 'enter number you must:'
    userinput = int(raw_input())
    alist.append(userinput)
print 'your answer is'
print sum (alist)

fact = 1
print' what number do you want to take a factorial of?'
userinput = int(raw_input())
for x in range(1,int(userinput)+1,1):
    fact = fact * x
print fact

print'enter a number to find the factors of it'
u = int(raw_input())
for x in range(1,int(u)+1):
    if u % x == 0:
        
        print x
        
