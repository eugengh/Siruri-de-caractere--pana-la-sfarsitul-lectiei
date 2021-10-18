a='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
a1 = ""
a2 = ""
for i in a:
    e = chr(ord(i)+1)
    a1+=e
    b=a1.replace('!', ' ')
    s=b.replace('[','A')
print("a1 = ", s)
a2 = s
for i in a:
    m=a2.replace(("Z"),("A"))
    n=m.replace('!', ' ')
    k = n.replace('[', 'A')
print("a2 = ", k)
print(a.replace(' ','-',len(a)))      
        
    

    



#print(ord('A'))
#print(ord('Y'))