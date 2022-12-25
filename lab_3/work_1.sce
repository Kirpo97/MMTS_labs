function yd=ff(x,y)
    yd=0.25*y^2+x^2
endfunction

y0=-1
x0=0

x=0:0.05:0.5;
y=ode("rk",y0,x0,x,ff);

plot2d(x,y)
xgrid
