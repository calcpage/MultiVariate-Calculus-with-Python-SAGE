#MrG 2018.0708 XTRAS 3D Graphs
#1a) Does SAGE use the Right Hand Rule?
show("#1a) Does SAGE use the Right Hand Rule?")
var('t')
xaxis=parametric_plot([t,0,0],(t,0,3),color='red')
yaxis=parametric_plot([0,t,0],(t,0,3),color='green')
zaxis=parametric_plot([0,0,t],(t,0,3),color='magenta')
#defining lines paramtrically throught point (0,0,0) parallel to each unit vector i, j, k
#show(xaxis+yaxis+zaxis)
show("")

#1b) Does SAGE use the Right Hand Rule?
show("#1a) Does SAGE use the Right Hand Rule?")
var('t')
xaxis=parametric_plot([t,0,0],(t,-3,3),color='red')
yaxis=parametric_plot([0,t,0],(t,-3,3),color='green')
zaxis=parametric_plot([0,0,t],(t,-3,3),color='magenta')
#defining lines paramtrically throught point (0,0,0) parallel to each unit vector i, j, k
#show(xaxis+yaxis+zaxis)
show("")

#2) graph z==2, y==-1, z==3
show("#2) graph x=2, y=-1, z=3")
var('y,z')
p1=implicit_plot3d(x==2,(x,-3,3),(y,-3,3),(z,-3,3))
p2=implicit_plot3d(y==-1,(x,-3,3),(y,-3,3),(z,-3,3))
p3=implicit_plot3d(z==3,(x,-3,3),(y,-3,3),(z,-3,3))
#show(p1+p2+p3+xaxis+yaxis+zaxis)
show("")

#3) graph 2*x+3*y+4*z==0 and 2*x+3*y+4*z==12
#3) note: x/a+y/b+z/c==1 has x-intercept (a,0,0), y-intercept (0,b,0) and z-intercept (0,0,c)
#3) 2D analog: x/a+y/b==1 has x-intercept (a,0) and y-intercept (0,b)
show("#3) graph 2*x+3*y+4*z==0 and 2*x+3*y+4*z==12")
p1=implicit_plot3d(2*x+3*y+4*z==0,(x,-6,6),(y,-6,6),(z,-6,6))
p2=implicit_plot3d(2*x+3*y+4*z==12,(x,-6,6),(y,-6,6),(z,-6,6))
p3=point([6,0,0],color='red')
p4=point([0,4,0],color='red')
p5=point([0,0,3],color='red')
show(p1+p2+p3+p4+p5+xaxis+yaxis+zaxis)
#y=f(x) curves in 2D -> tangent line: y=m*x+b -> y-b=m(x-0) -> delatY=m*deltaX
#z=f(x,y) surfaces in 3D -> tangent plane: fx*deltaX+fy*deltaY++fz*deltaZ=0
