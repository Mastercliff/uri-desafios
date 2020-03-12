IN1,IN2 = input().split()

table = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

tt = int(IN2) * table[int(IN1)]

print("Total: R$ {:.2f}".format(tt))