# coding: UTF-8
import random
print "欢迎使用随机选择器"
flag=True
add_over=False

#print "请输入选项数目"
#d=input("> ")
list=[]
#for i in range(0,d):
d=0

while not add_over:
    print "请输入选项名，输入e结束"
    item=raw_input("> ")
    if item!='e':
        list.append(item)
        d+=1
    else:
        add_over=True
add_over=False    
while True:
    r=random.randint(0, 10000)    
    print "\n经过随机处理，我们建议您选择：",list[r%d],"\n"

    print "是否继续选择，输入y继续选择，输入其余字符串退出："
    if raw_input("> ") != "y":
        break

    print "是否要修改已有选项，输入y修改，输入其余字符串不修改 "
    if raw_input("> ")=="y":
        flag=True
    else:
        flag=False
        
    while flag == True:   
        print "请选择修改方式，输入1增加候选项，输入2删除已有候选项，输入其他结束修改"
        choice=input("> ")
        if choice == 1 :
            #print "请输入增加的数目："
            #num=input("> ")
            #for i in range(0,num):
            #    print "请输入增加的第%d个选项名" %(i+1)
            #    list.append(raw_input("> "))
            #d+=num
            while not add_over:
                print "请输入选项名，输入e结束"
                item=raw_input("> ")
                if item!='e':
                    list.append(item)
                    d+=1
                else:
                    add_over=True
            add_over=False
        elif choice ==2 :
            #print "请输入删除的数目："
            #num=input("> ")
            del_over=False
            while not del_over:
                print "请输入要删除的项的编号，输入e结束"
                k=0
                for obj in list:
                    print k,".",obj
                    k+=1
                num=raw_input("> ")
                if num.isdigit() and num < len(list):    
                    del list[num]
                    d-=1
                if num == 'e':
                    del_over=True
                else:
                    print "输入错误，请重新输入"
        print "是否继续修改，输入y继续修改，输入其余字符串结束修改 "
        if raw_input("> ")=="y":
            flag=True
        else:
            flag=False
        
print "谢谢您的使用，再见\n"
