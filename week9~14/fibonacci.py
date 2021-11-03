def FA(num) : 
    result=0
    if num==0:
        result=0
    elif num==1:
        result=1
    else : 
        result=FA(num-1) + FA(num-2)
    return result



fn=int(input("피보나치 수열 f(n)을 입력 : "))
result=FA(fn)
print("f(%d) = %d" % (fn, result))
