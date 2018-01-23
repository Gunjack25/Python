def pallindrome(value):
    for i in range(20):
        x = checkpallindrome(value+i)
        if x==1:
            print(value+i)
            break

def checkpallindrome(val):
    flag=0
    list_val=list(str(val))
    len_val=len(list_val)
    for i in range(len_val):
        if list_val[i]  == list_val[-1-i]:
            flag=1
        else:
            flag=0
            break

    return flag

def main():
    iter = int(input(''))
    val=[]
    for _ in range(iter):
        values = int(input(''))
        val.append(values)

    for i in range(len(val)):
        pallindrome(val[i])

main()