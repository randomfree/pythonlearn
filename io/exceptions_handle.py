try:
    text = input('Enter someting -->')
except EOFError:
    print('why didi you do an EOF on me?')
except KeyboardInterrupt:
    print('you cancelled the operation.')
else:
    print('you extered {}'.format(text))
