class solute:
    def findnode(diff, top, node):
        if node == top:
            return -1
        newDiff = int(diff/2)
        l = r - diff
        r = top - 1
        print(l)
        print(r)
        if l == node or r == node:
            return top
        elif (node < l):
            return findnode(newDiff, l, node)
        elif (node > l):
            return findnode(newDiff, r, node)
        return -1

    def ans(self,h, q):
        top = (2**h) - 1
        arr = []
        for i in range(len(q)):
            arr.append(findnode((top - 1)//2, top, q[i]))
        return arr
        
solution=solute()
print(solution.ans(3, [7, 3, 5, 1]))

#https://foobar.withgoogle.com/?eid=kfjty
