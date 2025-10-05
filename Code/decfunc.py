def original(a,b):
    print("inside original")
    ans = a/b
    return ans 

def modified(func):
    def swap(a,b):
        if a<b:
            print("swapping the numbers...")
            a,b = b,a
            print("swapping done bete ....")
        return func(a,b)
    return swap

# original = modified(original)
# ans = original(2,4)
# print(ans)

@modified
def origin(x,y):
    return original(x,y)

print(origin(2,4))