// система диф. уравнений
function dz=syst(t,z,u)
    dz(1)=z(2);
    dz(2)=(-9*z(2)-15*z(1)-7*u(t))/6;
endfunction

// управляющее воздействие
function ut=u(t)
    if (t<1) then
        ut=0;
    else
        ut=1;
    end
endfunction

// Задание начальных условий
z0=[0;0];
t0=0;
t=0:0.05:10;

// Решение
z=ode(z0,t0,t,list(syst,u));

// Результат
out=[t' z']

// Построение графика
plot2d(t, z(1,:))
xgrid
