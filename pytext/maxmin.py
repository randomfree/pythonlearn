#获取列表中的最大值和最小值
def findMinAndMax(L):
    if len(L)>0:
        max = L[0]
        min = L[0]
    else:
        max = None
        min = None
    for i in L:
        if i>max:
            max = i
        if i<min:
            min = i

    return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
