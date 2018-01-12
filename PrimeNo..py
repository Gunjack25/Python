def main():
    testcases=int(input(''))

    lowerend = []
    higherend = []
    ys = [[]]
    for i in range(testcases):
        lowerend.append(int(input('')))
        higherend.append(int(input('')))

    for i in range(testcases):
        y=primer(higherend[i],lowerend[i])
        ys.append(y)
    for i in range(1,len(ys)):

        for j in range(len(ys[i])):
            print('{}'.format(ys[i][j]))


def primer(higherend,lowerend):
    x=[]

    y=list(range(2,higherend+1))
    for j in range(2,higherend+1):
        flag=0
        for k in range(2,j):
            if j % k == 0:
                flag = 1

            if flag == 1:
                x.append(j)
                break

    y = [t for t in y if t not in x and t>=lowerend]
    return y


if __name__=='__main__':
    main()