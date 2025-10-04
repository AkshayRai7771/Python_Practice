def countAndSay(n: int,result : str) -> str:
    mp = {}
    for x in s :
        if x in mp :
            mp[x]+=1
        else : mp[x]=1
        result = f"{mp[x]}{x}"
    if n == 1:
        result = "1"
        return result
    return countAndSay(n-1,result)

s = ""
x = countAndSay(4,s)
print(x)