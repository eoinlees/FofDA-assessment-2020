List = input("Enter a number of letters, numbers or words seperated by a space: ")


num = [1, 5, 8, 7, 7, 8, 7, 1]

def counts(List):
    userList = List.split()
    print(dict((i, userList.count(i)) for i in userList))
counts(num)