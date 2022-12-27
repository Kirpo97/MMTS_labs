# Вариант 15
  
matr_smeg_2 = [
#     1   2   3   4   5   6   7   8   9  10  11  12  13  14  15   j/i                  
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],  # 1
    ['1','0','1','0','1','0','0','0','0','0','0','0','0','0','0'],  # 2
    ['0','1','0','1','0','0','0','0','0','0','0','0','0','0','0'],  # 3
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],  # 4
    ['0','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],  # 5
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],  # 6
    ['0','0','1','1','0','1','0','0','0','0','0','0','0','0','0'],  # 7
    ['0','0','0','1','0','0','1','0','0','0','0','1','0','0','0'],  # 8
    ['0','0','0','0','0','1','0','0','0','0','0','0','1','0','0'],  # 9
    ['0','0','0','0','0','1','1','0','1','0','1','0','0','0','0'],  # 10
    ['0','0','0','0','0','0','1','0','0','0','0','0','0','1','0'],  # 11
    ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],  # 12
    ['0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],  # 13
    ['0','0','0','0','0','0','0','0','1','1','0','1','0','0','1'],  # 14
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']   # 15
]

matr_ints_2 = [
#     1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26  j/i                  
    ['-1','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 1
    ['1', '1','-1', '0', '1','-1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 2
    ['0','-1', '1', '1', '0', '0','-1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 3
    ['0', '0', '0','-1', '0', '0', '0','-1','-1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 4
    ['0', '0', '0', '0','-1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 5
    ['0', '0', '0', '0', '0', '0', '0', '0', '0','-1', '0','-1','-1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 6
    ['0', '0', '0', '0', '0', '0', '1', '1', '0', '1','-1', '0', '0','-1','-1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 7
    ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],  # 8
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0','-1', '0', '0','-1', '1','-1', '0', '0', '0', '0'],  # 9
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '0','-1', '0', '0', '0'],  # 10
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0','-1','-1', '0', '0', '0', '0', '1', '0', '0'],  # 11
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0','-1', '0', '0', '1', '0', '0', '0', '0', '0','-1', '0'],  # 12
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1','-1', '0', '0', '0', '0', '0'],  # 13
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1','-1', '1', '1'],  # 14
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0','-1']   # 15
]

#  Множественное представление G(i)
M_smeg = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]

#  Множественное представление G^-1(i). Разделение на подмножества, где есть 1 и -1
M_ints_1 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
M_ints_m1 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]

# Находим пересечения подмножеств
peres_mnog = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]

a = [{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15}]
R = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
V = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]

#  Находим длины пути R(i)
R_lambda_1 = M_smeg
R_lambda_2 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_3 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_4 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_5 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_6 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_7 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_8 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_9 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda_10 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
R_lambda = [
    R_lambda_1,
    R_lambda_2,
    R_lambda_3,
    R_lambda_4,
    R_lambda_5,
    R_lambda_6,
    R_lambda_7,
    R_lambda_8,
    R_lambda_9,
    R_lambda_10
]

#  Находим длины пути Q(i)
Q_lambda_1 = peres_mnog
Q_lambda_2 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_3 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_4 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_5 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_6 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_7 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_8 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_9 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda_10 = [set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set(),set()]
Q_lambda = [
    Q_lambda_1,
    Q_lambda_2,
    Q_lambda_3,
    Q_lambda_4,
    Q_lambda_5,
    Q_lambda_6,
    Q_lambda_7,
    Q_lambda_8,
    Q_lambda_9,
    Q_lambda_10
]

def calc_G(matr, mnog, r):    
    for i in range(r):
        for j in range(r):
            if matr[i][j] == '1':
                mnog[i].add(j+1)
    print("G() = ",mnog,'\n') 

# Разделение на подмножества
def deference(matr, mng_1, mng_m1, range_1, range_2):   
    for i in range(range_1):
        for j in range(range_2):
            if matr[i][j] == '-1':
                mng_m1[i].add(j+1)
            elif matr[i][j] == '1':
                mng_1[i].add(j+1)
    print("G_m1() = ", mng_m1)  
    print("G_1() = ", mng_1)  
    
# Вычисление G^-1() с длинной пути 1, находим пересечения подмножеств
def calc_Gm1(peres_mng, mng_1, mng_m1, r, r2): 
    for k in range(r):  
        for p in range(r2):
            if (mng_m1[k].intersection(mng_1[p])):
                peres_mng[k].add(p+1) 
    print("G^-1() = ",peres_mng)
    
# Вычисление длины пути R(i) и Q(i)
def calc_lambda(str, p1, p2, range_1, range_2):
    for R in range(range_1):    
        for u in range(range_2):     
            for l in range(range_2):       
                if l in p2[u]:
                    p1[R][u].update(p1[R-1][l-1])
        print(str,"(",R+1,") = ", p1[R]) 
        
def calc(str, p1, p2, r):
    for t in range(r):            
        p2[t] = a[t] | p1[0][t] | p1[1][t] | p1[2][t] | p1[3][t] | p1[4][t]
        print(str, "(",t+1,") = ", p2[t])         

def res(r):
    for i in range(r):
        V[i] = R[i] & Q[i]
        print("V",i+1," = ", V[i])
    print()   
    print("__Р Е З У Л Ь Т А Т__")  
    print()
    
    # отфильтруем результаты:
    o = 1
    a = [set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
    list_s = []
    for i in range(15):
        if (V[i].isdisjoint(V[o])):
            V[i].discard(i)
            a[i] = V[i]
            o += 1
        if a[i] != set():
            list_s.append(a[i])
            print("V",i+1," = ", a[i])
              
    return list_s




if __name__ == '__main__':
    
    l_sm = len(matr_smeg_2)       
    l_in_y = len(matr_ints_2)
    l_in_x = len(matr_ints_2[0])

    calc_G(matr_smeg_2, M_smeg, l_sm)
    deference(matr_ints_2, M_ints_1, M_ints_m1, l_in_y, l_in_x)
    calc_Gm1(peres_mnog, M_ints_1, M_ints_m1, l_in_y, l_in_y)

    print()

    # Вычисление длин R(i)
    calc_lambda("R_lambda",R_lambda, M_smeg, 10, l_sm) # 10 - максимальная длинна пути lambda
    calc("R",R_lambda, R, l_in_y)
    print()

    # Вычисление длин Q(i)
    calc_lambda("Q_lambda",Q_lambda, peres_mnog, 10, l_in_y)
    calc("Q",Q_lambda, Q, l_in_y)

    print()
    list_s = res(l_sm)
    print()


    import numpy as np

    matr_dost_1 = np.matrix ([
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0]
        ])

    m_s = np.matrix ([
    #    1 2 3 4 5 6 7 8 9 10   j/i      
        [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],  # 1
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],  # 2
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # 3
        [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],  # 4
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],  # 5
        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],  # 6
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],  # 7
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],  # 8
        [0,0,0,0,0,0,0,1,0,1],  # 9
        [0,0,0,0,0,0,0,0,0,0]  # 10
    ])
    
    matr_dost_2 = matr_dost_1

    for k in range(5):
        for i in list_s[k]:
            matr_dost_1[k] |= m_s[i-1]        
        
    matr_dost_t = matr_dost_1.transpose()

    for k in range(5):
        for i in list_s[k]:
            matr_dost_2[k] |= matr_dost_t[i-1]  
    matr_dost_t2 = matr_dost_2.transpose()
        
    np.fill_diagonal(matr_dost_t2, 0)
    matr_dost_t2

