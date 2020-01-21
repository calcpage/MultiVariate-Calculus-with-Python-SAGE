#MrG 2018.0523 NCC04 What The Equation Of A Plane: a*x+b*y+c*z==d?
#1) Find The Equation of a plane, a*x+b*y+c*z==d, through the point (0,0,0) perpendicular to vector <1,5,10>
show("#1) Find The Equation of a plane, a*x+b*y+c*z==d, through the point (0,0,0) perpendicular to vector <1,5,10>")
var('y,z')
v=vector([1,5,10]);show("v=",v)
w=vector([x,y,z]);show("w=",w)
show("v.dot_product(w)=",v.dot_product(w)) #set dot product==0
show("d=",0+5*0+10*0)
show(solve(x+5*y+10*z==0,z))
show(solve(x+5*y+10*z==0,z)[0])
show(solve(x+5*y+10*z==0,z)[0].rhs())
p1=plot3d(solve(x+5*y+10*z==0,z)[0].rhs(),(x,-5,5),(y,-5,5))
p2=point([0,0,0],color='red')
p3=plot(v,color='green')
#show(p1+p2+p3)

#2) Find The Equation of a plane, a*x+b*y+c*z==d, through the point (2,1,-1) perpendicular to vector <1,5,10>
show("#2) Find The Equation of a plane, a*x+b*y+c*z==d, through the point (2,1,-1) perpendicular to vector <1,5,10>")
w=vector([x-2,y-1,z+1]);show("w=",w)
show("v.dot_product(w)=",v.dot_product(w)) #set dot product==0
show("d=",2+5*1+10*-1) #note d is distance between parallel planes thru (0,0,0) and (2,1,-1) if v is not just a normal vector but a unit vector too!
show(solve(x+5*y+10*z==-3,z))
show(solve(x+5*y+10*z==-3,z)[0])
show(solve(x+5*y+10*z==-3,z)[0].rhs())

#3) solve for (x,y,z): x+z==1, x+y==2, x+2*y+3*z==3
show('#3) solve for (x,y,z): x+z==1, x+y==2, x+2*y+3*z==3')
a=matrix([[1,0,1],[1,1,0],[1,2,3]]);show("a=",a);show("det(a)=",det(a));show("a^(-1)=",a^(-1))
b=matrix(3,1,[[1],[2],[3]]);show("b=",b);show("a^(-1)*b=",a^(-1)*b)
