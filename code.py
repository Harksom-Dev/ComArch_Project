def splitdata(x):
    a = []
    f = open(x, "r")
    a = f.read()
    arr = a.split("\n")
    return arr

# print(splitdata("test.txt"))

def simulateEX(x):
    print('@@@\nstate:\n\t\tpc 0\n\t\tmemory:')
    arr = splitdata(x)
    for i in range(len(arr)):
        print('\t\t\t\tmemory[{0}]={1}'.format(i,arr[i]))
    

simulateEX("test.txt")
 
