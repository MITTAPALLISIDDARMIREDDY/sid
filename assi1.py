n=input("")
x=n.split(",")
te=[int(i) for i in x]
c=50
h=30
for j in te:
    q=round(((2*c*j)//h)**(0.5))
    print(q,end=", "[:-1])

