#MrG 2018.0523 NCC05 HowTo parametric_plot3d()?
#1) What's The Equation Of A Line?
show("What's The Equation Of A Line?")
var('t')
parametric_plot3d([1+2*t, 2+t, 2-3*t], (t,0,20))

#2) What's The Equation Of A Helix?
show("What's The Equation Of A Helix?")
parametric_plot3d([sin(t), cos(t), t], (t,0,20))

#) What's The Equation Of A Cycloid?
show("What's The Equation Of A Cycloid?")
parametric_plot3d([0,2*t-2**sin(t), 2-2*cos(t)], (t,0,20))
