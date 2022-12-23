import numpy as np
# Матрица смежности
print('\n''ЗАДАНИЕ 2''\n')

m_smeg_1 = np.array([
#    1  2  3  4  5  6  7  8  9  10  i/j
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 1
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],# 2
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],# 3
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],# 4
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],# 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],# 6
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],# 7
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],# 8
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],# 9
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10
])

Q_i_0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Q_j_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_j_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_j_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_j_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_j_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_j_6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
Q_j_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
Q_j_t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Q_j_0 = [1, 1, 1, 1 ,1, 1, 1, 1, 1, 1]
Q_i_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_i_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_i_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_i_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_i_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_i_6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q_i_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
Q_i_t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

Q_j = [Q_j_0, Q_j_1, Q_j_2, Q_j_3, Q_j_4, Q_j_5, Q_j_6, Q_j_7, Q_i_t]   
      
def calc_Q(matr, Q_j, Q_i): 
    for j in range(10):
        for i in range(10):
            if matr[j][i] >= 1:
                Q_i[j] += matr[j][i]
                Q_j[i] += matr[j][i]
    print("Q_j = ", Q_j)                       
    print("Q_i = ", Q_i)
    print()
    
print("m_smeg^0:\n", Q_j_0,'\n')    
    
print("m_smeg^1:\n", m_smeg_1)    
calc_Q(m_smeg_1, Q_j_1, Q_i_1) 
  
m_smeg_2 = np.linalg.matrix_power(m_smeg_1, 2)
print("m_smeg^2:\n", m_smeg_2) 
calc_Q(m_smeg_2, Q_j_2, Q_i_2)   

m_smeg_3 = m_smeg_2.dot(m_smeg_1)
print("m_smeg^3:\n", m_smeg_3) 
calc_Q(m_smeg_3, Q_j_3, Q_i_3) 

m_smeg_4 = m_smeg_3.dot(m_smeg_1)
print("m_smeg^4:\n", m_smeg_4) 
calc_Q(m_smeg_4, Q_j_4, Q_i_4) 

m_smeg_5 = m_smeg_4.dot(m_smeg_1)
print("m_smeg^5:\n", m_smeg_5) 
calc_Q(m_smeg_5, Q_j_5, Q_i_5) 

m_smeg_6 = m_smeg_5.dot(m_smeg_1)
print("m_smeg^6:\n", m_smeg_6) 
calc_Q(m_smeg_6, Q_j_6, Q_i_6) 

m_smeg_7 = m_smeg_6.dot(m_smeg_1)
print("m_smeg^7:\n", m_smeg_7) 
calc_Q(m_smeg_7, Q_j_7, Q_i_7) 

total = m_smeg_1 + m_smeg_2 + m_smeg_3 + m_smeg_4 + m_smeg_5 + m_smeg_6 + m_smeg_7
print("total:\n", total)
calc_Q(total, Q_j_t, Q_i_t)

print('\nСВОЙСТВА:')
print('1. Определение порядка элементов:\n')

p0 = 'Элементы 0 порядка'
p1 = 'Элементы 1 порядка'
p2 = 'Элементы 2 порядка'
p3 = 'Элементы 3 порядка'
p4 = 'Элементы 4 порядка'
p5 = 'Элементы 5 порядка'
p6 = 'Элементы 6 порядка'
p = [p0, p1 ,p2 ,p3 ,p4 ,p5, p6]

order_p1 = [
# узел   1 2 3 4 5 6 7 8 9 10   
        [0,0,0,0,0,0,0,0,0,0], # 0 порядок
        [0,0,0,0,0,0,0,0,0,0], # 1 порядок
        [0,0,0,0,0,0,0,0,0,0], # 2 порядок
        [0,0,0,0,0,0,0,0,0,0], # 3 порядок
        [0,0,0,0,0,0,0,0,0,0], # 4 порядок
        [0,0,0,0,0,0,0,0,0,0], # 5 порядок
        [0,0,0,0,0,0,0,0,0,0], # 6
        ]

order_p2 = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        ]

res = [0,0,0,0,0,0,0,0,0,0]

def order_J(param1, param2, o_p1, o_p2):
    for i in range(10):
        if param1[i] > 0:
            o_p1[i] = i+1
        if param2[i] == 0:
            o_p2[i] = i+1

for x in range(7):
    order_J(Q_j[x], Q_j[x+1], order_p1[x], order_p2[x])
    print(p[x],'\n',order_p1[x],'\n',order_p2[x],'\n')
    
for v in range(7):      
    for x in range(10):
        if order_p1[v][x] == order_p2[v][x]:
            res[x] = v
print('узел:\t',[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('порядок:',res,'\n')

print('2. Опредедение тактности системы:')
print('Тактность = ', max(res),'\n')

print('3. Определение контуров')

def searsh_contour():
    s = -1
    flag_1 = False
    for a in range(0,8): 
        s = s +1 
        if total[s][a] > 0:
            flag_1 = True
            
    if flag_1 == False:
        print('Контуры не найдены')        
    else:
        print('Контур найден')    
       
searsh_contour()       

print('\n''4. Определение входных элементов потока')

for i in range(10):
    if Q_j_1[i] == 0:
        print('Входной элемент:',i+1)

print('\n''5. Определение выходных элементов потока')

for i in range(10):
    if Q_i_1[i] == 0:
        print('Выходной элемент:',i+1 )

print('\n''6. Определение висящих вершин')

def searsh_v():
    flag = False
    for i in range(10):
        if Q_i_1[i] == 0:
            if Q_j_1[i] == 0:
                flag = True            
    if flag == True:
        print('Висящая вершина найдена')
    else:
        print('Висящих вершин нет')
        
searsh_v()

print('\n''7. Определение числа путей длиной Lambda')

def count_path(matr, str):
    count = [0,0,0]
    str2 = ['','','']
    for k in range(10):
        for i in range(10):
            if matr[i][k] == 1:
                count[0] += 1
                str2[0] = 'с 1 путём'
            elif matr[i][k] == 2:
                count[1] += 1
                str2[1] = 'с 2 путями'
            elif matr[i][k] == 3:
                count[2] += 1
                str2[2] = 'с 3 путями'
    for j in range(3):
        if count[j] > 0:         
            print(count[j], 'элементов', str, str2[j])
            
count_path(m_smeg_1, 'длиной 1')
count_path(m_smeg_2, 'длиной 2')
count_path(m_smeg_3, 'длиной 3')
count_path(m_smeg_4, 'длиной 4')
count_path(m_smeg_5, 'длиной 5')
count_path(m_smeg_6, 'длиной 6')

print('\n''8. Определение всевозможных путей между двумя элементами')

for k in range(10):
    for i in range(10):
        if total[k][i] > 0:
            print('От узла',k+1,'до узла',i+1,'колличество путей =', total[k][i])

print('\n''9. Определение всех элементов, участвующих в формировании данного')

s1 = set()
s2 = set()
s3 = set()
s4 = set()
s5 = set()
s6 = set()
s7 = set()
s8 = set()    
s9 = set()
s10 = set()   
s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]    

for k in range(10):
    for i in range(10):
        if total[i][k] > 0:     
            s[k].add(i+1)
for i in range(10):
    print('Элементы формирующие узлел',i+1,':',s[i])