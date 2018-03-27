# 4.1_遍历列表用for, 列表是集合, 是可迭代的;
magicians = ['alice', 'david', 'carolina'];
for magician in magicians:
    print(magician.title());

# 4.2_避免缩进错误;


# 4.3_创建数值列表;
# 4.3.1_range()函数;
for value in range(1,5):
    print(value);
# 指定`3`为步长;
numbers = list(range(1, 16, 3));
print(numbers);

# 4.3.3_对数字列表执行简单的统计计算: min(), max(), sum();
digits = range(1, 11);
print(min(digits));
print(max(digits));
print(sum(digits));

# 4.3.4_列表解析;
squares = [value**2 for value in range(1,11)];
print(squares);


# 4.4_使用列表的一部分: 切片;
players = ['charles', 'martina', 'michael', 'florence', 'eli'];
print(players[1:3]);
print(players[:3]);
print(players[1:]);

# 4.4.2_遍历切片;
# 4.4.3_复制列表: [:];

# 4.5_元组: 不可修改的列表, 圆括号的形式;

# 4.6_代码格式;









