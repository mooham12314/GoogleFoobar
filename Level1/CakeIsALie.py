class solute:
    def solution(self,s):
        num=[]
        word=[]
        option=[]
        length=len(s)
        print(length)
        #find factor to get word count
        for i in range(1,length):
            if length % i == 0:
               num.append(i)
        num.append(length)
        #get word length from word count
        for i in range(len(num)):
            num[i]=length/num[i]
        print(num)
        #substring from word count
        for i in range(len(num)):
            temp=s[0:num[i]]
            word.append(temp)
        print(word)
        #check for equal part
        for i in range(len(num)):
            option.append(word[i])
            for j in range(0,length,num[i]):
                if word[i]!=s[j:j+num[i]]:
                    option.pop()
                    break
        #select best option
        print(option)
        print(length/len(option[-1]))
        return length/len(option[-1])
        
solution=solute()
strin6="abcabcabcabc"
strin2="ababa"
s1="z"
solution.solution(s1)
