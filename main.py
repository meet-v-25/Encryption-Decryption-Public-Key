###### """ ''' Defining Functions ''' """ ###### 

# Overall Key Generation Algorithm
def Key_Generation(p,q,x):
    n = p * q ; y = x 
    phi_n = (p-1)*(q-1)
    (g,x,d) = EEA(phi_n,x)
    return (int(y),int(d),int(n))

# Extended Euclidean Algorithm
def EEA(a,b):
    y=0;d=1
    if(a==0): return b,y,d
    (g,yy,dd) = EEA(b%a,a)
    d=yy ; y = (dd-(b/a)*yy)
    return (g,y,d)

def func(x):
     return 3.5*(x**3)- 2.7*x - 17 

def func_1(x,c):
    return 3.5*(x**3)- 2.7*x - 17 - c

def func_2(x,c):
    return 5*(x**4) - 3.2*(x**2) - c
 
def derivFunc_1(x):               # Derivative of the func_1
    return 10.5*(x**2) - 2.7  

def derivFunc_2(x):               # Derivative of the func_2
    return 20*(x**3) - 6.4*(x)

# Newton Raphson function to find the root
def newtonRaphson(x,c):
    h = func_1(x,c) / derivFunc_1(x)
    while abs(h) >= 0.0001:
        x = x - h       # x_(i+1) = x_(i) - ( f(x) / f'(x) )
        h = func_1(x,c)/derivFunc_1(x)
    return x

# Using Newton Raphson to generate the key
def newtonRaphson_KeyGeneration(x,c):
    h = func_2(x,c) / derivFunc_2(x)
    while abs(h) >= 0.0001:
        h = func_2(x,c)/derivFunc_2(x)
        x = x - h       # x(i+1) = x(i) - f(x(i)) / f'(x(i))
    return x



###### """ ''' Initialization ''' """ ###### 

p = 17 ; q = 13 ; x = 7
Sa, Pa, n = Key_Generation(p, q, x)

x0 = 1
c = newtonRaphson_KeyGeneration(x0, Sa)

ASCII=[] ; cipher=[] ; DecipheredText = ''; 
PlainText = input("\nEnter Your Message: ")



###### """ ''' Encryption Algorithm ''' """ ###### 

for i in range(len(PlainText)):
    ASCII.append(ord(PlainText[i]))

for i in range(len(ASCII)):
    temp = newtonRaphson(x0, ASCII[i]) + c
    cipher.append(temp)



###### """ ''' Decryption Algorithm ''' """ ###### 

x0 = 1
GeneratedKey = newtonRaphson_KeyGeneration(x0, Sa)

for i in range(len(cipher)):
    DecipheredText += chr(int(round((func(cipher[i] - GeneratedKey)), 0)))


###### """ ''' Printing Output ''' """ ###### 

# print("\nPlain Text is:",PlainText)
# print("\nASCII values for plain text are :",ASCII)
print("\nEncrypted values are:",cipher)
print("\nYour Decrypted Text is:", DecipheredText,"\n")
