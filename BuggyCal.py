def main():
    x = int(input("Number of test cases b/w 1 to 100"))
    Final = []
    if x > 0 and x < 101:
        for i in range(x):
            l = int(input("Enter the first number"))
            b = int(input("Enter the second number"))
            answer = cal(l, b)
            Final.append(answer)
    print(Final)
    #else:
     #   main()


def cal(l, b):
    Fina = 0
    for x in range(1, 10):
        m = pow(10, x)
        FirstNumber = (int((l % m) / pow(10, x - 1)))
        SecondNumber = (int((b % m) / pow(10, x - 1)))
        FirstNo = FirstNumber * (m / 10)
        SecondNo = SecondNumber * (m / 10)
        #print("First number is {}". format(FirstNo))
        #print("Second number is {}". format(SecondNo))
        Add = FirstNo + SecondNo
        Fina += (Add % m)
    return Fina


if __name__ == "__main__":
    print('Yo')
    main()
