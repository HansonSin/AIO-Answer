with open('sitin.txt', 'r') as inputFile1: 
    mylist = list(inputFile1)

inputFile1.close()

row, seats = mylist[0].split(' ', 1)
tickets = mylist[1]

noOfSeats = int(row) * int(seats)
noOfTickets = int(tickets)
if noOfSeats <= noOfTickets:
    standing = noOfTickets - noOfSeats
    seatNo = noOfSeats
else:
    seatNo = noOfTickets
    standing = 0

outputFile = open('sitout.txt','w') 
outputFile.write(str(seatNo) + ' ' + str(standing)); 
outputFile.close()
