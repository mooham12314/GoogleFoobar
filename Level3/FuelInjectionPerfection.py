import math
def solution(s):
    num=int(s)
    count=0
    while num>3:
        print(str(num)+'->')
        if num%2==0:
            num=num>>1
            count=count+1
#        elif math.sqrt(num+1)%1==0:
#            num=num+1
#            count=count+1
        else:
            if num&2:
                num=(num+1)>>2
                count=count+3
                print('sss')
            else:
                num=num-1
                count=count+1
    if num==2:
        count=count+1
        return count
    if num==3:
        count=count+2
        return count
    return count

#for i in range(64,128):
    print(i,solution(str(i)))
print(solution('95'))
