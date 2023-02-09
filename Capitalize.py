

def solve(s):
    s=s.casefold()
    for i in range(len(s)):
        if s[i].isalpha()==True and (s[i-1]==" " or i==0):
            s=s[:i]+s[i].upper()+s[i+1:]
    k=str(s)
    return k



