# python3


def build_heap(data):
    swaps = []

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    thelast = len(data) - 1
    parent = 0
    while thelast != 0:
        last = thelast
        while last != 0 : #one line
            parent = int((last-1)/2)
            if data[last] < data[parent] :
                data[last], data[parent] =  data[parent], data[last]
                swaps.append([parent,last])
            last = parent
        thelast -= 1

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    i = input() # file or input
    if "i" in i.lower() :
        n = int(input())
        data = list(map(int, input().split()))

    elif "f" in i.lower() :
        name = input()
        name = "./tests/" + name
        if "a" not in name:
            with open(name, mode = 'r' ,  encoding = "utf8") as fail:
                n = int(fail.readline())# number of elements
                data = list(map(int, fail.readline().split()))
        else :
            return
                
    else :
        return
    assert len(data) == n

    swaps = build_heap(data) #array of swaps

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
