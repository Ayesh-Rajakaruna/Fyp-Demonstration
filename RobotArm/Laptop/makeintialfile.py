servername = 1
intialpoint = 0
fw = open("./Laptop/DataSets/{}{}.txt".format("Initialization", servername), "w")


def decimal_to_binary(decimal, num_digits):
    binary = bin(decimal)[2:] 
    binary = str(binary.zfill(num_digits))
    return binary


if intialpoint == 13:
    lis = [i for i in range(intialpoint)]
    for i in lis:
        fw.write(decimal_to_binary(i,10)+decimal_to_binary(2,2) + "\n")
elif intialpoint > 13:
    lis = [i for i in range(intialpoint-13,intialpoint)]
    for i in lis:
        fw.write(decimal_to_binary(i,10)+decimal_to_binary(2,2) + "\n")
else:
    lis = [0]*(13-intialpoint) + [i for i in range(intialpoint)]
    count = -1
    for i in lis:
        count = count + 1
        if count > (13-intialpoint):
            fw.write(decimal_to_binary(i,10)+decimal_to_binary(2,2) + "\n")
        else:
            fw.write(decimal_to_binary(i,10)+decimal_to_binary(0,2)+ "\n")