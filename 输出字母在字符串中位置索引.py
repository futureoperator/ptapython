##输入一个字符串，再输入两个字符，求这两个字符在字符串中的索引。
##
##输入格式:
##第一行输入字符串
##第二行输入两个字符，用空格分开。
##
##输出格式:
##从右向左输出字符和索引，即下标最大的字符最先输出。每行一个。
##
##输入样例:
##在这里给出一组输入。例如：
##
##pmispsissippi
##s p
##输出样例:
##在这里给出相应的输出。例如：
##
##11 p
##10 p
##8 s
##7 s
##5 s
##4 p
##3 s
##0 p

n=input()
a,b=input().split()
ls=[]
for i in range(len(n)):
    if a==n[i]:
        ls.append([i,a])
    elif b==n[i]:
        ls.append([i,b])
ls=ls[::-1]
for i in range(len(ls)):
    print(ls[i][0],end=' ')
    print(ls[i][1])
