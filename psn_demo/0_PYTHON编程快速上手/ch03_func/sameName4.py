# p51 @20170108

def spam():
    #eggs = 'spam local'
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()

#Traceback (most recent call last):
#  File "/Users/haoranye/Desktop/sameName4.py", line 6, in <module>
#    spam()
#  File "/Users/haoranye/Desktop/sameName4.py", line 2, in spam
#    print(eggs)
#UnboundLocalError: local variable 'eggs' referenced before assignment
