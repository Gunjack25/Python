def main():
    x = []
    for i in range(100):
        x.append(int(input('')))
        if x[i] == 42:
            break

    for l in range(len(x)-1):
        print(x[l])



if __name__ == '__main__':
    main()

#COMPLETED!!