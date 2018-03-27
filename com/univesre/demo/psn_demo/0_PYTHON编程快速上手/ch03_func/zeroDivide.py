# p53, try/except statement; @20170108

def spam(divideBy):
    try:
        return 42/divideBy
    except:
        print('Error: Invalid Denominator, Return: ', end='')

print(spam(0))
print(spam(1))
print(spam(2))
print(spam(3))
