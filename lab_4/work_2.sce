A = [
12, 4;
4, 4;
3, 12;
];
b = [300;120;252];
c = [30;40];
lb=[0;0];
ub=[%inf;%inf];
[xopt,fopt]=karmarkar([],[],-c,[],[],[],[],[],A,b,lb,ub)
