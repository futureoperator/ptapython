##输入一个1到7的数字，输出对应的星期名的缩写。
##1        Mon
##2        Tue
##3     Wed
##4        Thu
##5        Fri
##6        Sat
##7       Sun
##
##输入格式:
##输入1到7之间数字
##
##输出格式:
##输出对应的星期名的缩写


dic={'1':'Mon','2':'Tue','3':'Wed','4':'Thu','5':'Fri','6':'Sat','7':'Sun'}
n=input()
print(dic.get(n))##获取字典里的值用get，形式把索引放在get里，别写成dic(n).get()
