import random
def read(): 
    input_path = "data1.txt" 

    with open(input_path, "r") as f:
        lines = f.read().splitlines()
    N, M, K = lines[0].strip().split()
    N = int(N)
    M = int(M)
    K = int(K)
    a,b,c,d,e,f = lines[1].strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)

    s = []
    for i in range(2, N+2):
        s_tmps = lines[i].strip().split()
        s_tmp = []
        for i in s_tmps:
            s_tmp.append(int(i))
        s.append(s_tmp)
    
    g = []
    for i in range(N+2, 2*N+2):
        g_tmps = lines[i].strip().split()
        g_tmp = []
        for i in g_tmps:
            g_tmp.append(int(i))
        g.append(g_tmp)

    t = []
    t_tmp = lines[2*N+2].strip().split()
    for i in t_tmp:
        t.append(int(i))
    
    return N,M,K,t,s,g,a,b,c,d,e,f


def candidates1(N):
    c_1 = []
    for i in range(N):
        c_1.append(int(i))
    return c_1
def candidates2(M):
    c_2 = []
    for i in range(M):
        c_2.append(int(i))
    return c_2

def start_value_1(c_1, N, b, K):
    while(1):
        result = []
        for i in range(K * b):
            result.append(-1)
        for i in range(K):
            rand = random.randint(1, N-i)
            result[i * b] = c_1.pop(rand - 1)
        tmp_1 = result[0]
        tmp_2 = 1
        for i in range(K):
            if tmp_1 != result[i * b]:
                tmp_2 = 0
        if tmp_2 == 0:
            break
    return result

def start_value_2(K, d):
    result = []
    for i in range(K*d):
        result.append(-1)
    return result      

def select_1(c_1, result, K, b, s, M, t, a, e):
    h = []
    for i in range(M):
        h_tmp = []
        for j in range(K):
            h_tmp.append(0)
        h.append(h_tmp)
    for i in range(K):
        for j in result[i*b : i*b + b -1]:
            if (j != -1):
                h[t[j]-1][i] = 1


    sum_max = 0
    for i in range(K):
        for j in c_1:
            sum = 0 
            project_max = 0 
            for k in result[i*b : i*b + b - 1]:
                if (k != -1):
                    if s[j][k] < e:
                        break
                    project_max = project_max + 1  
                    sum = sum + s[j][k]  
                

            
            sum = sum / (project_max) 
            if project_max >= a:
                sum = sum /100
            if sum > sum_max: 
                sum_h = 0 
                h[t[j]-1][i] = 1
                for m in range(K):
                    sum_h = sum_h + h[t[j]-1][m]
                if sum_h >= K:
                    h[t[j]-1][i] = 0
                    break
                if project_max >= b:
                    break
                sum_max = sum 
                global council, project, pj_max
                council = i
                project = j
                pj_max = project_max 
    return council, project, pj_max   

def select_2(c_2, result_1,result_2, K, g, b, c, d, t, f, M):
    h = []
    for i in range(M):
        h_tmp = []
        for j in range(K):
            h_tmp.append(0)
        h.append(h_tmp)
    for i in range(K):
        for j in result_1[i*b : i*b + b -1]:
            if (j != -1):
                h[t[j]-1][i] = 1
    sum_max = 0
    for i in range(K):
        teacher_max = 0
        for tc in result_2[i*d : i * d + d - 1]:
            if tc != -1 :
                teacher_max = teacher_max + 1
        for j in c_2:
            sum = 0
            for k in result_1[i*b : i*b + b - 1]:
                
                          
                if (k != -1):
                    if h[j-1][i] == 1:
                         break  
                    if g[k][j] < f:
                        break
                    sum = sum + g[k][j]
                if teacher_max >= d:
                    break
                if teacher_max >= c:
                    sum = 0.1 * sum
                if sum > sum_max:
                    sum_max = sum 
                global council, teacher, tc_max
                council = i
                teacher = j
                tc_max = teacher_max
    return council, teacher, tc_max 
def solution(result_1, result_2, N, M):
    sum1 = 0
    sum2 = 0
    for i in result_1:
        if i != -1:
            sum1 = sum1 + 1 
    if sum1 != N:
        return False
    
    for i in result_2:
        if i != -1:
            sum2 = sum2 +1
    if sum2 != M:
        return False
    else: return True




def main():
    N,M,K,t,s,g,a,b,c,d,e,f = read()
    c_1 = candidates1(N)
    c_2 = candidates2(M)
    result_1 = start_value_1(c_1,N, b, K)
    result_2 = start_value_2(K, d)
    while(len(c_1) != 0):
        council_1, project, project_max = select_1(c_1, result_1, K, b, s, M, t, a, e)
        result_1[council_1*b + project_max ] = project
        c_1.remove(project)
      
    while(len(c_2) != 0):
        council_2, teacher, tc_max = select_2(c_2, result_1,result_2, K, g, b, c, d, t, f, M)
        result_2[council_2*d + tc_max] = teacher 
        c_2.remove(teacher)
    if solution(result_1,result_2, N, M) == True:
        print(N)
        for i in range(N):
            print((result_1.index(i)//b),end = ' ')
        print(end='\n')
        print(M)
        for i in range(M):
            print((result_2.index(i)//d),end = ' ')
    else: print("No solution")
    
main()

