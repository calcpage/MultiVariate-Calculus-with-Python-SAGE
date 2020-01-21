#MrG 2018.0614 UMC09 Dot Products
#1) Find the angle between v=<3,-1,2> and w=<-4,0,2>
show("#1) Find the angle between v=<3,-1,2> and w=<-4,0,2>")
v=vector([3,-1,2]);show("v=",v);show("abs(v)=",abs(v))
w=vector([-4,0,2]);show("w=",w);show("abs(w)=",abs(w))
d=v.dot_product(w);show("d=",d)
show("cos(theta)=",d/abs(v)/abs(w))
show("theta=",arccos(d/abs(v)/abs(w)).n()," radians")
show("theta=",(180/pi*arccos(d/abs(v)/abs(w))).n()," degrees")
show("")

#2) Find the line through the point (1,-2,4) and parallel to the vector v=<2,4,-4>
show("#2) Find the line through the point (1,-2,4) and parallel to the vector v=<2,4,-4>")
x(t)=1+2*t;show("x(t)=",x(t))
y(t)=-2+4*t;show("y(t)=",y(t))
z(t)=4-4*t;show("z(t)=",z(t))
p1=parametric_plot3d((x(t), y(t), z(t)), (t,0,2))
p2=point([0,0,0],color='red')
p3=point([1,-2,4],color='green')
p4=plot(vector([2,4,-4]),color='orange')
show(p1+p2+p3+p4,aspect_ratio=(1,1,1))
