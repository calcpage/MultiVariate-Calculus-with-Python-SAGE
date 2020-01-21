#MrG 2018.0523 NCC03 What Is A Matrix?
#1) Find the sum of 2 matrices
show("Find the sum of 2 matrices")
a=matrix([(2,3,-1),(4,0,7)]);show("a=",a)
b=matrix([(1,-2,-1),(-5,3,-4)]);show("b=",b)
show("a+b=",a+b)
show("4*a=",4*a)
show("3*b=",3*b)
show("4*a-3*b=",4*a-3*b)

#2) Find the product of 2 matrices
show("Find the product of 2 matrices")
c=matrix([(2,1,3),(1,-1,0)]);show("c=",c)
d=matrix([(1,0),(2,1),(3,2)]);show("d=",d)
show("c*d=",c*d)

#3a) Find the POI: 3*x-2*y==4, 6*x+y==13 (Cramer's Rule)
show("Find the POI: 3*x-2*y==4, 6*x+y==13 (Cramer's Rule)")
a=matrix([(4,-2),(13,1)]);show("a=",a)
b=matrix([(3,4),(6,13)]);show("b=",b)
c=matrix([(3,-2),(6,1)]);show("c=",c)
show("det(a)=",det(a))
show("det(b)=",det(b))
show("det(c)=",det(c))
show("x=",det(a)/det(c))
show("y=",det(b)/det(c))

#3b) Find the POI: 3*x-2*y==4, 6*x+y==13 (Inverse Matrix)
show("Find the POI: 3*x-2*y==4, 6*x+y==13 (Inverse Matrix)")
a=matrix([(3,-2),(6,1)]);show("a=",a)
b=matrix(2,1,[(4),(13)]);show("b=",b)
show(a^(-1))
show((a^(-1))*b)
