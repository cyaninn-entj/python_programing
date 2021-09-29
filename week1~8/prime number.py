num = int(input(숫자 입력  ))

for i in range(2, num)  
    if num % i == 0  
        print(num,은 소수가 아닙니다.)
        break
    else  
        print(num,은 소수입니다.)
        break