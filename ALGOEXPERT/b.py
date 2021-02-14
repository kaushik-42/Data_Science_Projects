def binary_no(n):
    m = ''
    while n:
        m += str(n % 2)
        n >>= 1
    if(len(m) % 2 == 0):
        m = m[::-1]
    else:
        m = '0'+m[::-1]
    m = list(m)
    i = len(m)-1
    while(i > 0):
        m[i], m[i-1] = m[i-1], m[i]
        i -= 2
    return m


m = binary_no(100)
c = "".join(i for i in m)
print(int(c, 2))
