def ex_dig_op(a):
    j=0
    d=[]
    c=''  
    digit = ['1','2','3','4','5','6','7','8','9','0','.']
    operator = ['+','-','*','/','(',')','=']
    b= len(a)  
    for i in a:
       j+=1
       if i in  digit :
           c += i
       if i in  operator or j==b:
          if c!= '':
            c1 = float(c)
            d.append(c1)
            c=''
          if j != b:
            if i == '=':
                break
          d.append(i)
    return  d 

def in_par(d):
    while ')' in d:
        j2 = j=d.index(')')
        while d[j]!='(':
            j-=1
        f1=[]    
        j1=j+1
        for i in range(j1,j2) :   
            f1.append(d[i])
        s=pri_cal(f1)     
        d[j1-1]=s
        for i in range(j1,j2+1) :
            d.pop(j1)
        if '(' not in d:
            break
    return d

def pri_cal(f):
    while '*' in f:
        i=f.index('*')
        f[i-1]=f[i-1]*f[i+1]
        f.pop(i)
        f.pop(i)

    while '/' in f:
        i=f.index('/')
        f[i-1]=f[i-1]/f[i+1]
        f.pop(i)
        f.pop(i)

    while '-' in f:
        i=f.index('-')
        f[i-1]=f[i-1]-f[i+1]
        f.pop(i)
        f.pop(i)
    
    while '+' in f:
        i=f.index('+')
        f[i-1]=f[i-1]+f[i+1]
        f.pop(i)
        f.pop(i)
        
    return f[0]
print('|______________________|')
print('|##### CALCULATOR #####|')
print('|----------------------|')
a = input('Enter your calcut :')
d =in_par( ex_dig_op(a))
re=pri_cal(d)
print(a ,'= ',re)
