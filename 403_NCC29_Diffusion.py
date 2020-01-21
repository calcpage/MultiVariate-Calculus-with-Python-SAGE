#MrG 2018.0721 NCC29 Diffusion Equation aka Heat Equation
#1) Let u=u(x,y,z,t) = concentration of smoke in room (no air flow)
#1) Let u=u(x,y,z,t) = concentration of ink blot in cup (no fluid flow)
#1) Let u=u(x,y,z,t) = heat of planar solid at (x,y,z) over time t 
#1) and Vector Field F=flow of smoke, ink or heat

#1) Thermodynamics gives us F=-k*u.gradient(), flow goes from highest to lowest concentration
#1) because: gradient points in direction of highest incease of u
#1) Relate Flux and amount of smoke - if D is bounded by closed surface S, then:
#1) double integral of F.NdS over S = -d(triple integral udV)/dt 
#1) because: flux outof D = - variation of total amount of smoke inside D

#1) lhs=triple integral of divF dV over D
#1) rhs=triple integral of - partial u over partial t dV over D
#1) therefore: ut=-divF=k*div(u.gradient())=k*u.laplacian=k*(uxx+uyy+uzz)

