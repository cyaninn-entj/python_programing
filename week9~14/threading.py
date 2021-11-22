import threading
#import time

class sum_number :
    maxnum=""
    def __init__(self,num) :
        self.maxnum=num

    def sum_(self) :
        maxnum=self.maxnum
        num_list=[]
        for i in range(1,maxnum+1) : 
            num_list.append(i)
        total=sum(num_list)
        print("1+2+3+......+ %d = %d" % (maxnum, total))
        

number1=sum_number(1000)
number2=sum_number(100000)
number3=sum_number(10000000)

th1=threading.Thread(target=number1.sum_)
th2=threading.Thread(target=number2.sum_)
th3=threading.Thread(target=number3.sum_)

th1.start()
th2.start()
th3.start()