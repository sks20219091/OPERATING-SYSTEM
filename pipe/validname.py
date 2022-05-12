from os import fork, pipe, fdopen, close


def getValidNames(s: str) -> str:
    lis = s.split()
    ans = []
    for x in lis:
        if len(x) >= 5 and len(x) < 8 and x[0:1].isalpha() == True:
            # we can proceed:
            # need to check for any special characters;
            for y in x:
                if y.isalnum() == False:
                    continue

            ans.append(x)

    valid = " ".join(ans)
    return valid


def main():

    # create pipes
    r1, w1 = pipe()  # P TO C
    r2, w2 = pipe()  # C TO P
    pid = fork()

    if pid > 0:

        # receivce from child.
        close(w2)
        r2 = fdopen(r2)
        s = r2.read()
        r2.close()

        lis = getValidNames(s)
        print("The valid names are  : "+lis)

    else:
        close(r2)
        w2 = fdopen(w2, 'w')
        # child sends the stream of numbers first.
        s = input("Enter stream of names  : ")
        w2.write(s)

        w2.close()


if _name_ == "_main_":
    main()
