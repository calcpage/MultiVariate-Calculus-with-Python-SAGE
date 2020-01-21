#MrG 2018.0614 NCC10 Verifying Local Min, Local Max or Saddle Points
#1) view the min: z=x^2+y^2
show("#1) view the min: z=x^2+y^2")
f(x,y)=x^2+y^2
plot3d(f(x,y),(x,-2.5,2.5),(y,-2.5,2.5))
contour_plot(f(x,y),(x,-2.5,2.5),(y,-2.5,2.5), labels=True, label_colors='red')
show("")

#2) view the max: z=-x^2-y^2
show("#2) view the max: z=-x^2-y^2")
f(x,y)=-x^2-y^2
plot3d(f(x,y),(x,-2.5,2.5),(y,-2.5,2.5))
contour_plot(f(x,y),(x,-2.5,2.5),(y,-2.5,2.5), labels=True, label_colors='red')
show("")

#3) view a saddle point: z=x^2-y^2
show("#3) view 2 maxs and a saddle point: z=x^2-y^2")
f(x,y)=x^2-y^2
plot3d(f(x,y),(x,-2.5,2.5),(y,-2.5,2.5)).show()
contour_plot(f(x,y),(x,-2.5,2.5),(y,-2.5,2.5), labels=True, label_colors='red').show()
