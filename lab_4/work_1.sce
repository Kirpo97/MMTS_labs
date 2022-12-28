x=0:0.1:30;
y1=(300-12*x)/4;
y2=(120-4*x)/4;
y3=(252-3*x)/12;
plot(x,y1,'-r',x,y2,'-g',x,y3,'-b');
mtlb_hold('on');
plot([0 30],[0 40],'--b','LineWidth',2)

A=[4,4;3,12]
b=[-120;-252]
z = linsolve(A,b)
xgrid();
