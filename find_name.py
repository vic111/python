#一个用于查找你的姓名是否在表中
#进行姓名的补全

name = {'Adam','Alex','Amy','Bob','Boom',
        'Candy','Chris','David','Jason',
        'Jasonstatham','Bill'}
while(1):
    i_name = input ('请输入你的姓名').title()
    fname = []
    for i in name:
        if i[0:len(i_name)] == i_name:
            fname.append (i)
    if len (fname) == 0:
        print ('数据库没有找到你的姓名')
    elif len(fname)==1:
        print('用户',fname,'你好!')
        exit ()
    else:
        print ('你的姓名可能是',fname)

