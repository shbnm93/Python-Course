# data = open("d:/mydata.txt", "r")
# data = open("d:/mydata.txt", "r+")
# data = open("d:/mydata.txt", "w")
# data = open("d:/mydata.txt", "w+")
# data = open("d:/mydata.txt", "x")
# data = open("d:/mydata.txt", "rt")
# data = open("d:/mydata.txt", "rb")
# data = open("d:/mydata.txt", "r+b")


# data = open("mydata.txt", "a+")
# # print(data.read())
# # print(data.readline())
# # print(data.readline())

# # print(data.readlines())
# data.seek(5)
# data.write("\nAli")

# data.close()


with open("mydata.txt", "a+") as data:
    data.seek(5)
    data.write("\nAli")