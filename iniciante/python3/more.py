input_list = input().split()
final_list = list(map(lambda x: int(x), input_list))
def maior(lista):
    if lista[0] > lista[1]:
        if lista[0] > lista[2]:
            return lista[0]
    if lista[1] > lista[2]:
            return lista[1]
    else:
        return lista[2]
valor = maior(final_list)
print("{} eh o maior".format(valor))