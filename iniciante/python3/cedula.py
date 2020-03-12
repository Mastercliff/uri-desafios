IN = int(input())
FN = IN

rest = IN % 100
IN = IN -rest
count_100 = IN / 100

rest2 = rest % 50
IN = rest -rest2
count_50 = IN / 50

rest = rest2 % 20
IN = rest2 - rest
count_20 = IN / 20

rest2 = rest % 10
IN = rest - rest2
count_10 = IN/ 10

rest = rest2 % 5
IN = rest2 - rest
count_5 = IN /5

rest2 = rest % 2
IN = rest - rest2
count_2 = IN/ 2

rest = rest2 % 1
IN = rest2 - rest
count_1 = IN /1

l = [count_100, count_50, count_20, count_10, count_5, count_2, count_1]
l2 = [100, 50, 20, 10, 5, 2, 1]

print(FN)
for i in range(7):
    print("{} nota(s) de R$ {},00".format(int(l[i]), int(l2[i])))