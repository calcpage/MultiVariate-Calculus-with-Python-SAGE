#MrG 2018.0614 UMC10 Cross Product
#1) Find Cross Product vxw given u=<1,-2,1> and v=<3,1,-2>
show("#1) Find Cross Product vxw given u=<1,-2,1> and v=<3,1,-2>")
u=vector([1,-2,1]);show("u=",u)
v=vector([3,1,-2]);show("v=",v)
c=u.cross_product(v);show("c=",c)
show("")

#2) Find the area of the parallelogram: u=<1,-2,1> and v=<3,1,-2>
show("#2) Find the area of the parallelogram defined by u=<1,-2,1> and v=<3,1,-2>")
show("abs(c)=",abs(c))
show("abs(c)=",abs(c).n())
show("")

#3) Find the volume of the parallelopiped: u=<1,1,0>, v=<0,1,1>, w=<1,0,1>
show("#3) Find the volume of the parallelopiped: u=<1,1,0>, v=<0,1,1>, w=<1,0,1>")
u=vector([1,1,0]);show("u=",u)
v=vector([0,1,1]);show("v=",v)
w=vector([1,0,1]);show("w=",w)
c=u.cross_product(v);show("c=",c)
show("area=",c.dot_product(w))
p1=plot(u,color='red')
p2=plot(v,color='green')
p3=plot(w,color='blue')
show(p1+p2+p3,aspect_ratio=(1,1,1))
