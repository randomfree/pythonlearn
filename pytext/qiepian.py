#去掉字符串首位空格
def trim(s):
    if s[0:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[0:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')

