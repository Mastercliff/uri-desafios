IN = float(input())

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
count_1 = IN / 1

rest2 = rest % 0.5
IN = rest - rest2
count_05 = IN/ 0.5

rest = rest2 % 0.25
IN = rest2 - rest
count_025 = IN / 0.25

rest2 = rest % 0.10
IN = rest - rest2
count_010 = IN/ 0.10

rest = rest2 % 0.05
IN = rest2 - rest
count_005 = IN / 0.05


count_001 = rest/ 0.01




l_nota = [count_100, count_50, count_20, count_10, count_5, count_2]
l_nota_vl = [100, 50, 20, 10, 5, 2]

l_moeda = [count_1, count_05, count_025, count_010, count_005, count_001]
l_moeda_vl = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in range(6):
    print("{} nota(s) de R$ {}.00".format(int(l_nota[i]), int(l_nota_vl[i])))

print("MOEDAS:")
for i in range(6):
    print("{} moeda(s) de R$ {:.2f}".format(round(l_moeda[i]), l_moeda_vl[i]))