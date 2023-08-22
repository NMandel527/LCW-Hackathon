import csv
# this is assuming all of the addresses have been converted into coordinate points
# and those coordinate points have been stored in a list called coordinatePoints
def main():

    #this takes a randomly generated list of addresses that a Goggle API turns into coordinate points
    #turns it into a 2d list of x,y coordinates
    with open("Adresses - Sheet2.csv", "r") as read_obj:
        csv_reader = csv.reader(read_obj)

        list_of_csv = list(csv_reader)

    listxy = list_of_csv

    for row in range(len(list_of_csv)):
        for col in range(len(list_of_csv[row])):
            # newlist[row][col]= float(list_of_csv[row][col])
            # print(float(list_of_csv[row][col]))
            listxy[row][col] = float(list_of_csv[row][col])
    #print(listxy)

    #sort by left to right
    listxy.sort(key=lambda x:x[0])

    xcenter = 39.798335 #center of america
    ycenter = -99.087231 #center of america

    nw = []
    nwcount = 0
    ne = []
    necount = 0
    sw = []
    swcount = 0
    se = []
    secount = 0
    north = []
    south = []
    truck = 0

    # this takes in the coordinate points and divides them up into regions and then prints each region with its proper points

    for row in range(len(listxy)):
        for col in range(len(listxy[row])):
            if col == 0:
                x = listxy[row][col]
            elif col == 1:
                y = listxy[row][col]
        if x < xcenter:
            if y < ycenter:
                sw.append(listxy[row])
                swcount += 1
            elif y >= ycenter:
                nw.append(listxy[row])
                nwcount += 1
        if x >= xcenter:
            if y < ycenter:
                se.append(listxy[row])
                secount += 1
            elif y >= ycenter:
                ne.append(listxy[row])
                necount += 1

    print("Southwest Region:", sw, "\nSoutheast region:", se, "\nNortheast Region:", ne, "\nNorthwest Region:", nw)
    # # now we have to assign the number of trucks into each region

    if necount + nwcount <= 250:
        north = ne + nw
        truck += 1
    if necount > 250:
        truck += necount//250
        neremainder = necount%250
    if nwcount > 250:
        truck += nwcount // 250
        nwremainder = nwcount % 250
    if nwremainder > 0 and neremainder > 0:
        if nwremainder + neremainder > 250:
            truck += 2
        while nwremainder < 250 and neremainder > 0 :
            nw.append(ne[0])
            del ne[0]
            nwcount += 1
            neremainder -=1
        truck += 1
        while neremainder < 250 and nwremainder > 0 :
            ne.append(nw[len[nw]-1])
            del nw[len[nw]-1]
            necount += 1
            nwremainder -= 1
        truck += 1
    print(truck)

main()
