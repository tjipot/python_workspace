'''
数据结构(类与对象): 1.列表, 2.元组, 3.字典, 4.集合;
'''

# 1.List类的演示: 用'[]'表示, 是一个类: 有类的Field(字段)和Method(方法) +++++++++++++++++++++++++++++++++++++++++++++++++++++
def listDemo():

    shoplist = ['apple', 'mango', 'carrot', 'banana']   # 创建List的一种方式;
    print('I have', len(shoplist), 'items to purchase.')
    print('These items are:', end=' ')                  # 使用end参数;

    for item in shoplist:
        print(item, end=' ')                            # 使用end参数;

    print('\nI also have to buy rice.')
    shoplist.append('rice')                             # shoplist对象使用List类内的Method, 用'点'语法;
    print('My shopping list is now', shoplist, '.')
    print('I will sort my list now.')

    shoplist.sort()
    print('Sorted shopping list is', shoplist)
    print('The first item I will buy is', shoplist[0])

    olditem = shoplist[0]
    del shoplist[0]                                     # del: 列表中移除某元素;
    print('I bought the', olditem)
    print('My shopping list is now', shoplist)


# 2.Tuple类的演示: 用'()'表示, 类似于List, 但其内元素不可变 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def tupleDemo():
    # 我会推荐你总是使用括号来指明元组的开始与结束, 尽管括号是一个可选选项: 明了胜过晦涩, 显式优于隐式。

    zoo = ('python', 'elephant', 'penguin')                         # '()'即代表元组;
    print('Number of animals in the zoo is', len(zoo))              # 元组也有len用法, 说明也是序列;

    new_zoo = 'monkey', 'camel', zoo                                # 不用'()'的元组的声明;
    print('Number of cages in the new zoo is', len(new_zoo))
    print('All animals in new zoo are', new_zoo)

    print('Animals brought from old zoo are', new_zoo[2])           # 元组元素的寻找;
    print('Last animal brought from old zoo is', new_zoo[2][2])     # 元组中的元组;
    print('Number of animals in the new zoo is', len(new_zoo) - 1 + len(new_zoo[2]))

    tupleWithOneEle = ('one',)                                      # 必须要用一个逗号, 以便告诉Py这是一个元组, 即便看上去很奇怪;
    print('Tuple with only one ele: ', tupleWithOneEle)             # 用','号而不用'+'号: '+'号会要求运算符重载会报错;


# 3.Dict类的演示: 键(Keys)与值(Values)联系到一起(成对出现), 键需唯一且需是不可变对象, 构成元素: '{:,}' ++++++++++++++++++++++++++
# “ab”是地址（Address）簿（Book）的缩写
def dictDemo():

    ab = {
        'Swaroop': 'swaroop@swaroopch.com',
        'Larry': 'larry@wall.org',
        'Matsumoto': 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
    }

    print("Swaroop's address is", ab['Swaroop'], end='\n\n')

    # 删除一对'键-值'配对;
    del ab['Spammer']                                                       # dict中同样使用索引来查找项目;
    print('There are {} contacts in the address-book\n'.format(len(ab)))    # '{}'相当于占位符;

    for name, address in ab.items():                                        # name, address的用法: name与address是成一对的;
        print('Contact {} at {}'.format(name, address))                     # str.format()的用法;

    # 添加一对'键-值'配对;
    ab['Guido'] = 'guido@python.org'                                        # 支持临时添加;
    if 'Guido' in ab:
        print("\nGuido's address is", ab['Guido'])


# 4.Set类的演示: 集合(Set)是简单对象的无序集合(Collection) ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def setDemo():
    bri = set(['brazil', 'russia', 'india'])

    print('india' in bri)           # True
    print('usa' in bri)             # False

    bric = bri.copy()               # 应该是按值copy, 而不是引用copy;
    bric.add('china')
    print(bric)                     # {'brazil', 'russia', 'india', 'china'}
    bric.issuperset(bri)            # True, 超集判断;

    bri.remove('russia')
    print(bri & bric)               # {'brazil', 'india'}: 交集操作;
    print(bri.intersection(bric))   # {'brazil', 'india'}: 交集操作;


# 附01, 序列: in和not in表达式(资格测试, Membership Test), 以及索引操作(Indexing Operations), +++++++++++++++++++++++++++++++
# 同样还有切片(Slicing, 序列的一部分)操作;
def sequenceDemo():
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    name = 'swaroop'

    # 索引(Indexing)操作符;
    print('Item 0 is', shoplist[0])                 # list索引;
    print('Item 1 is', shoplist[1])
    print('Item 2 is', shoplist[2])
    print('Item 3 is', shoplist[3])
    print('Item -1 is', shoplist[-1])
    print('Item -2 is', shoplist[-2])
    print('Character 0 is', name[0])                # 字符串索引;

    # 下标(Subscription)操作符;
    print('Item 1 to 3 is', shoplist[1:3])          # List的切片;
    print('Item 2 to end is', shoplist[2:])
    print('Item 1 to -1 is', shoplist[1:-1])        # Item 1 to -1 is ['mango', 'carrot']: 列出元素还是正序列到截止元素为止;
    print('Item start to end is', shoplist[:])

    print('characters 1 to 3 is', name[1:3])        # 字符串的切片;
    print('characters 2 to end is', name[2:])
    print('characters 1 to -1 is', name[1:-1])      # characters 1 to -1 is waroo
    print('characters start to end is', name[:])

# 附02, 序列步长 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def stepDemo():
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    print(shoplist[::1])        # ['apple', 'mango', 'carrot', 'banana']
    print(shoplist[::2])        # ['apple', 'carrot']
    print(shoplist[::3])        # ['apple', 'banana']
    print(shoplist[::-1])       # ['banana', 'carrot', 'mango', 'apple'], 步长为-1有意思了;

# 附03: 引用 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 对象即内存!!!: 当你创建了一个对象(即内存)并将其分配给某个变量时，变量只会查阅(Refer)某个对象(即内存)，并且它也不会代表对象(即内存)本身.
def referDemo():

    print('Simple Assignment')
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    mylist = shoplist       # mylist 只是指向同一对象的另一种名称;

    # 我购买了第一项项目, 所以我将其从列表中删除;
    del shoplist[0]
    print('shoplist is', shoplist)
    print('mylist is', mylist)

    # 注意到 shoplist 和 mylist 二者都打印出了其中都没有 apple 的同样的列表，以此我们确认

    # 它们指向的是同一个对象

    print('Copy by making a full slice')

    # 通过生成一份完整的切片制作一份列表的副本

    mylist = shoplist[:]

    # 删除第一个项目

    del mylist[0]

    print('shoplist is', shoplist)

    print('mylist is', mylist)

    # 注意到现在两份列表已出现不同




########## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ### 运行;
# listDemo()
# tupleDemo()
# dictDemo()
# sequenceDemo()
# stepDemo()
setDemo()





