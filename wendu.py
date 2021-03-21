wendu=input('tpye the tem plz:')
if wendu[-1] in ('F', 'f'):
    C=(eval(wendu[0:-1])-32)/1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif wendu[-1] in ('c','C'):
    F=eval(wendu[0:-1])*1.8+32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print('输入错误')

