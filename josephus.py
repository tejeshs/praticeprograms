
def josephus(w,l=1,h=2):
        if h > w and l <= w:
                return ((w-l)*2+1)
        l = h
        h = h * 2
        return josephus(w,l,h)
result = josephus(w=1)
print(result)
