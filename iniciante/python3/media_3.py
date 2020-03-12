N1, N2, N3, N4 = input().split()

N1 = float(N1) * 2
N2 = float(N2) * 3
N3 = float(N3) * 4
N4 = float(N4) * 1
MEDIA = (N1+N2+N3+N4)/10
if 5 <= MEDIA <= 6.9:
    EN = float(input())

print("Media: {:.1f}".format(MEDIA))
if MEDIA >= 7.0:
    print("Aluno aprovado.")
elif 5 <= MEDIA <= 6.9:
    print("Aluno em exame.")
    print("Nota do exame: {:.1f}".format(EN))
    NF = (MEDIA + EN)/2
    if NF >= 5:
        print("Aluno aprovado.")
        print("Media Final: {:.1f}\n".format(NF))
    elif NF <= 4.9:
        print("Aluno reprovado.")
        print("Media Final: {:.1f}\n".format(NF))
else:
    print("Aluno reprovado.")