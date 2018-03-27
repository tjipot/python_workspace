# p56: collatz(), @20170110;

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

print('Pls type in a number:')
collatz(int(input()))

