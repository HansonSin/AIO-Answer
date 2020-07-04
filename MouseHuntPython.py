fin = open("mousein.txt", "r")
xlis = []
ylis = []
for i in range(8):
    xin, yin = map(int, fin.readline().split(" "))
    xlis.append(xin)
    ylis.append(yin)
fin.close()
fout = open("mouseout.txt", "w")
if xlis.count(min(xlis)) == 4:
    fout.write("W")
elif xlis.count(max(xlis)) == 4:
    fout.write("E")
elif ylis.count(min(ylis)) == 4:
    fout.write("S")
elif ylis.count(max(ylis)) == 4:
    fout.write("N")
fout.close()
