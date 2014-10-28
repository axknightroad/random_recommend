# coding: UTF-8
import random
print "欢迎使用随机选择器"
flag=True


print "请输入选项数目"
d=input("> ")
list=[]
for i in range(0,d):
    print "请输入第%d个选项名" %(i+1)
    list.append(raw_input("> "))
    
while True:
    r=random.randint(0, 100)    
    print "\n经过随机处理，我们建议您选择：",list[r%d],"\n"

    print "是否继续选择，输入yes继续选择，输入其余字符串退出："
    if raw_input("> ") != "yes":
        break

    print "是否要修改已有选项，输入yes修改，输入其余字符串不修改 "
    if raw_input("> ")=="yes":
        flag=True
    else:
        flag=False
        
    while flag == True:   
        print "请选择修改方式，输入1增加候选项，输入2删除已有候选项"
        choice=input("> ")
        if choice == 1 :
            print "请输入增加的数目："
            num=input("> ")
            for i in range(0,num):
                print "请输入增加的第%d个选项名" %(i+1)
                list.append(raw_input("> "))
            d+=num
        elif choice ==2 :
            print "请输入删除的数目："
            num=input("> ")
            for i in range(0,num):
                print "请输入要删除的项的编号：\n"
                k=0
                for obj in list:
                    print k,".",obj,"\n"
                    k+=1
                del list[input("> ")]
            d-=num
        print "是否继续修改，输入yes继续修改，输入其余字符串结束修改 "
        if raw_input("> ")=="yes":
            flag=True
        else:
            flag=False
        
print "谢谢您的使用，再见\n"
