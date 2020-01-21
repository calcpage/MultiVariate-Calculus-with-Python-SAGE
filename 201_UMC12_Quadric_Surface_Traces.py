#MrG 2018.0614 UMC12 Quadric Surfaces
#1) Graph Cylinder z=y^2
show("#1) Graph Cylinder z=y^2")
var('y')
#plot3d(y^2,(x,0,4),(y,-2,2)).show(aspect_ratio=(1,1,1))
show("")

#2) Interact!
show("Interact!")
var('x,y,z')
quadrics = {'Ellipsoid':x^2+y^2+z^2-1,'Elliptic paraboloid':x^2+y^2-z,'Hyperbolic paraboloid':x^2-y^2-z, '1-Sheeted Hyperboloid':x^2+y^2-z^2-1,'2-Sheeted Hyperboloid':x^2-y^2-z^2-1, 'Cone':x^2+y^2-z^2}
@interact
def quads(q = selector(quadrics.keys()), a = slider(0,5,1/2,default = 1)):
    f = quadrics[q].subs({x:x*a^(1/2)})
    if a==0 or q=='Cone': pretty_print(latex(f), "    (degenerate)")
    else: pretty_print(latex(f))
    p = implicit_plot3d(f,(x,-2,2),(y,-2,2),(z,-2,2), plot_points = 75)
    show(p)
