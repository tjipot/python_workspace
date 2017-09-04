#! /usr/bin/env python3
# Part2_chapter7: 模式匹配与正则表达式(p115), @20170113;

import re 	# Regex's module;

###7.1: 不用正则表达式来查找文本, 'isPhoneNumber.py', @20170111;
# # Version 1: idiot way;
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True
# # Running;
# print('\'415-555-4242\' is a phone number? ', end='' )
# print(str(isPhoneNumber('415-555-4242')) + '.')
# print('\'Moshi moshi\' is a phone number? ', end='')
# print(str(isPhoneNumber('Moshi moshi')) + '.')
# # Version 2: idiot way;
# def isPhoneNumber2(message):
#     for i in range(len(message)):
#         chunk = message[i:i+12]
#         if isPhoneNumber(chunk):
#             print('Phone number found: ' + chunk)
#     print('Done')
# # Running;
# msg = 'Call me at 415-555-1011 tomorrow, 415-555-9999 is my office.'
# isPhoneNumber2(msg)


##7.2: 用正则表达式查找模式文本, 基本步骤: 创建正则表达式对象->匹配Regex对象(得到结果);
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   #1.compile a Regex object, return a Regex; 
# mo = phoneNumRegex.search('my number is 425-555-4242')  #2.call Regex's method, return a Match;
# print(mo.group())	                                #3.call Match's method, return a string, groups() returns a tuple;


###7.3: 用正则表达式匹配更多模式;
#7.3.1: 用括号进行分组;
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d{3}-\d{4})')	#reg object;
# mo = phoneNumRegex.search('My number is 123-111-4444')	#match object;
# print('Result: ' + mo.group())				#match.group() returns result;
# g2 = mo.group(2)
# print('group 2 is: ' + g2)
# g1, g2_a = mo.groups()
# print('group 1 & 2 are: ' + g1 + ' ' + g2)

#7.3.2: 用管道分配多个分组, 字符'|'为管道, 表达多个中的某一个的意思;
# heroRegex = re.compile(r'Batman|Tina Fey')	#blank has effect on matching: "r'Batman  |  Tina Fey'", with two spaces around '|', influences;
# mo1 = heroRegex.search('Batman and Tina Fey')	#这个search方法只会返回一个匹配, findall()会返回所有的匹配;
# print('Result: ' + mo1.group())
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo2 = batRegex.search('Batmobile lost a wheel')
# print('batRegex result: ' + mo2.group())

#7.3.3: 问号('?')可以实现可选匹配(零次或一次);
#7.3.4: 星号('*')匹配零次或多次;
#7.3.5: 加号('+')匹配一次或多次;
#7.3.6: 花括号('{}')匹配特定的次数;


###7.4: 贪心匹配和非贪心匹配('贪心匹配'是能匹配最多的内容, 就返回最多的内容的结果);
###Python默认是贪心匹配的, 在匹配的花括号后跟一个'?'即告诉解释器要非贪心匹配;
# greedyRegex = re.compile(r'(Ha){3,5}')			#Requires 3 to 5: as many as possible;
# greedyRegexMo = greedyRegex.search('HaHaHaHaHaHa')	#6 'Ha';
# print('Greedy result: ' + greedyRegexMo.group())	#Result: 5 'Ha';
# nongreedyRegex = re.compile(r'(Ha){3,5}?')		#Requires 3 to 5: as less as possible;
# nongreedyRegexMo = nongreedyRegex.search('HaHaHaHaHaHa')#6 'Ha';
# print('Nongreedy Result: ' + nongreedyRegexMo.group())	#Result: 3 'Ha';


###7.5: findall() returns a list of strings of matching results;
###另外: 正则规则中有没有分组(即有没有用'()'把某部分规则分组起来), 是不一样的;
# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# aboutMeInfo   = 'Cell: 415-555-9999   Work: 212-555-8888'
# phoneNumMatch = phoneNumRegex.findall(aboutMeInfo)	#findall() returns each result into a list;
# for eachNumber in phoneNumMatch:
# 	print('Result list: ' + str(phoneNumMatch))
# 	print('Result phone number: ' + eachNumber)

###7.6: 字符分类, \d(0-9任一数字), \D, \w(字母, 数字, 下划线字符), \W, \s(空格, 制表符, 换行符), \S;
# xmasRegex = re.compile(r'\d+\s\w+')
# xmasString = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, \
# 		6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge";
# print(xmasRegex.findall(xmasString))


###7.7: 定制字符分类, 有时用'\d\w\s'太宽泛了, 故引入: 短横'-'表示区间范围, 左方括号后跟插入字符'^'表示取非后面的内容;
###在方括号'[]'内, 普通的正则表达式符号不会被解释('.', '*', '?', '()');
# constantRegex  = re.compile(r'[^aeiouAEIOU][^aeiouAEIOU]')
# constantString = 'RoboCop eats baby food, BABY FOOD.'
# constantMatch  = constantRegex.findall(constantString)
# print(constantMatch)


###7.8: 插入字符'^'表示要在开始处, 美元字符'$'表示要在末尾处;
###7.9: 通配符, 用句点'.'表示, 匹配除了换行符之外的所有字符, 要匹配真正的句点, 用'\.';
#7.9.1: 点星'.*'匹配所有字符, 可以是零次或多次所有字符;
#7.9.2: 把're.DOTALL'作为re.compile()的第二个参数, 匹配包括换行字符在内的所有字符;
##7.10: 正则表达式符号小结;
##7.11: 不区分大小写匹配: re.IGNORECASE或re.I;


##7.12: sub()方法替换字符串: 参数1(要去替换的内容), 参数2(被替换的内容体);
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# agentNamesContent = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
# agentNamesString = agentNamesRegex.sub(r'\1****', agentNamesContent)
# print(agentNamesString)


##7.13: 管理复杂的正则表达式, 用're.VERBOSE'可以忽略正则字符串中的空白符和注释, 也可以将正则表达式放在多行中, 用三个引号'''引起来;
##7.14: re.compile()的第二个参数只接受一个值, 故组合使用're.IGNORECASE', 're.DOTALL'和're.VERBOSE'要用管道'|'表示按位或;
##7.15: 项目, 电话号码和email提取程序;

##7.16: 小结;
##7.18: 实战项目;

