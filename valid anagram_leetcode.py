s = str(input())
t = str(input())


def isanagram(string1, string2):
    flag = False
    if len(string1) != len(string2):
        return flag
    else:
        if len(string1) == 0 and len(string2) == 0:
            flag = True
            return flag
        else:
            hashmap = {}
            for i in string1:
                hashmap.update({i: string1.count(i)})

            for i in range(len(string1)):
                countchar = string2.count(string2[i])
                if string2[i] in hashmap:
                    if countchar == hashmap[string2[i]]:
                        flag = True
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break

        return flag


print(isanagram(s, t))
