# p57: inputVerification, the upgradation of collatz(), @20170110;

def collatz(number):
    while(True):
        if(number%2 == 0):
            number = number//2
            print(number)
        elif(number == 1):
            #print(number)
            break
        else:
            number = number * 3 + 1
            print(number)

try:
    print('Pls type in a number:')
    collatz(int(input()))
except:
    print('Invalid number: Value Error', end=', ')
    print('Pls input a number.')
