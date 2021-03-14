T = int(input("Cate teste vor avea loc?\n"))
f = open("Testari_in", "w")
f.write(str(T) + "\n")
k = 1
while k <= T:
    N = input("Cate numere o sa aiba testul {} ?\n".format(k))
    Max = input("Care este cel mai mare numar posibil in testul {} ?\n".format(k))
    f.write(str(N) + " " +str(Max) + "\n")
    k += 1
f.close()
