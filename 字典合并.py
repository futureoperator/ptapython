dic1=eval(input())
dic2=eval(input())
d3={}
def adddic(dic):
    for key,value in dic.items():
        if key in d3:
            d3[key]+=value
        else:
            d3[key]=value
adddic(dic1)
adddic(dic2)
ls=list(d3.items())
ls.sort(key=lambda x : ord(x[0]) if type(x[0])==str else x[0])
finald3=str(dict(ls)).replace(' ','').replace("'",'"')
print(finald3)
