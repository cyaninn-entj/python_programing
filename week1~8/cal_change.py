#4장 셀프 스터디 1
money = int(input("지폐로 교환 : "))

man_5=man_1=chun_5=chun_1=coin = 0


man_5 = int(money / 50000)
money = money % 50000

man_1 = int(money / 10000)
money = money % 10000

chun_5 = int(money / 5000)
money = money % 5000

chun_1 = int(money / 1000)
money = money % 1000

coin = money

print("5만원 지폐 -> %d" % man_5)
print("1만원 지폐 -> %d" % man_1)
print("5천원 지폐 -> %d" % chun_5)
print("1천원 지폐 -> %d" % chun_1)
print("잔돈 -> %d" % coin)
