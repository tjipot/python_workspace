
def readLinesFromFile(fileName):
    # urlTupleEntries = []
    fileContent = ''
    for line in open(fileName):
        # lineWithoutRowBreak = line.replace('\n', '')   # 行尾有一个'\n', 提取之后只剩一个元素
        # 判断: 1.长度为1或2, 2.包含'-->', 3.'\n', 满足上述条件的行都不要;
        if not (len(line ) ==1 or len(line ) ==2 or len(line ) ==3 or ('-->' in line)):
            fileContent += line.replace('\n', ' ')
    print(fileContent)


# readLinesFromFile('/Users/univesre/Desktop/28.srt')



# 除以128;
inputDemo = [[[28, 25, 24], [27, 24, 23], [27, 24, 22], [32, 28, 24], [31, 27, 25], [31, 27, 26]]
	, [[29, 23, 23], [30, 24, 24], [32, 24, 23], [27, 24, 22], [27, 23, 21], [26, 22, 20]]]


rultList01 = []
rultList02 = []
rultList03 = []
for i in range(len(inputDemo)):
	rultList02 = []
	for j in range(len(inputDemo[i])):
		rultList03 = []
		for k in range(len(inputDemo[i][j])):
			normEleValue = (inputDemo[i][j][k] - 128) / 128
			print(normEleValue)
			rultList03.append(normEleValue)
		rultList02.append(rultList03)
	rultList01.append(rultList02)

print(rultList01)

# inputRult = (inputDemo - 128) / 128






