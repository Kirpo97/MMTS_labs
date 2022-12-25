function dy=syst(x,y)
    dy(1)=y(2);
    dy(2)=-y(2)/x-y(1);
endfunction

//начальные значения
y0=[0.77;-0.5];
x0=1

//решение
x=1:0.05:1.5;
y=ode(y0,x0,x,syst);

z=[x' y']

plot2d(x, y')
xgrid
