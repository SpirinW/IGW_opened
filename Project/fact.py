def fact(n):
    try:
        n = int(n)
    except:
        return 'Error: invalid input'
    a=1
    for i in range(n,1,-1):
        a*=i
    return a
