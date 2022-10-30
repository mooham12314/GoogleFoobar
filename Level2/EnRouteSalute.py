def ez(walk):
    a=0
    b=0
    for i in walk:
        if i == '<':
            a += b
        elif i == '>':
            b += 1
    a=a<<1
    return a

ez(">----<")

