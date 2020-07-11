# open the input file to obtain the number of rows and seats
with open('sitin.txt', 'r') as inputFile1: 
    mylist = list(inputFile1) # assign the row to list
    
inputFile1.close() # remember that always close the file

# the input data is optained row by row and is assigned to list
# first list is first line of input file (no.of.rows and seats)
# second list is second line of input file (no.of.tickets sold)
row, seats = mylist[0].split(' ', 1)  # split the first element of list to get row and seats per row
tickets = mylist[1] # second row is only have the no.of.tickets sold

# calculate the total number of seats provided
# need to type casting the row and seats to integer datatype
# if number of seats is smaller or equal to number of tickets sold, number of people sitting = number of sets, the rest will be standing
# if number of seats is larger than the tickets solds, number of people sitting equal to number of tickets sold , and no people is standing
noOfSeats = int(row) * int(seats)
noOfTickets = int(tickets)
if noOfSeats <= noOfTickets:
    standing = noOfTickets - noOfSeats
    seatNo = noOfSeats
else:
    seatNo = noOfTickets
    standing = 0

# open output file, and write the result into it
# must close the file
outputFile = open('sitout.txt','w') 
outputFile.write(str(seatNo) + ' ' + str(standing)); 
outputFile.close()
