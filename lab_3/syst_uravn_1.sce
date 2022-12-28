// система диф. уравнений
function dz=syst(t,z,u)
    dz(1)=z(2);
    dz(2)=(-9*z(2)-15*z(1)-7*u(t))/6;
endfunction

// управляющее воздействие
function ut=u(t,z)
    ut=-K*(z-zf);
endfunction

// Задание начальных условий
z0=[0;0];
zf=[-16;0] //цулевое состояние
t0=0;
t=0:0.05:10;

//вычисление полюсов и матр. обратной связи
A=[0 1;-15/6 -9/6];
B=[0;-7/6];
p=roots(6*%s^2+9*%s+15);
p=p*10;
K=ppol(A,B,p);

// Решение
z=ode(z0,t0,t,list(syst,u));

// Результат
out=[t' z']

//вычисление управляющего воздействия
u_list=[];
for i=z
    u_list($+1)=-K*(i-zf);
end

// Построение графиков
plot2d(t, z(1,:));
xgrid;

show_window(1)
plot2d(t,u_list,style=[color("red")]);
