def solve16(n):
    q=n
    s=0
    while q!=0:
        r=q%10
        q=q//10
        s+=r
    return s

assert solve16(2**15) == 26

print(solve16(2**1000))   #1366

f=open('names.txt','r')

def solve22():
    L=[]
    for ligne in f:
        L=sorted(ligne.split(','), key=str)
    A=[0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    S=0
    for i in range (len(L)):
        s=0
        for j in range (len(L[i])):
            for p in range (len(A)):
                if L[i][j]==A[p]:
                    s+=p
        S+=(i+1)*s
    return S          
    
print(solve22())          #871198282

def reverse(n):
    L=str(n)
    LR=''
    p=len(L)
    for i in L:
        LR=i+LR
    return int(LR)

def solve55():
    n=0
    L=[]
    while n < 10000:
        n+=1
        s=n
        s=s+reverse(s)
        p=1
        while p < 50 and s!= reverse(s):
            s=s+reverse(s)
            p+=1
            if p == 50:
                L.append(n)
    return len(L)       
    
print(solve55())          #249