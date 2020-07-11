fin = open("vasesin.txt", "r")
n = int(fin.readline())
fin.close()

fout = open("vasesout.txt", "w")
if n >= 6:
    ans = "1 2 " + str(n - 3)
    fout.write(ans)
else:
    fout.write("0 0 0")
fout.close()
