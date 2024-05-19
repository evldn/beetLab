import sys
from munkres import Munkres
from scipy.optimize import linear_sum_assignment


def CTG(matrix, nu):
    # CTG Есть дозаривание до дня v.
    # Есть функция gamma(k), где k - типа текущий день
    # gamma(k) = n - 2v + 2k + 1 (для k от 1 до v-1)
    # gamma(v-1) = n - 2v - 2 + 2v + 1 = n - 1
    # gamma(k) = n + 2v - 2k (для k от v до 2v-1)
    # gamma(v+1) = n + 2v - 2v - 2 = n - 2
    # gamma(k) = n - k + 1 (для k от 2v до n)
    # Вот, если мы остортируем партии по сахаристости в день k, то gamma(k) говорит, что мы берём gamma(k)-ую максимальную партию
    # (Возможно не максимальную, а минимальную, надо посмотреть, на самом деле + надо проверить что эта формула нормально работает)
    n = len(matrix)
    block = [0] * n
    ans = []
    gamma = []
    for_ans = []
    for i in range(n):
        for_ans.append((matrix[i][0], i))
        if i < int(nu) - 1:
            gamma.append(n - 2 * int(nu) + 2 * (i + 1) + 1)
        elif i >= int(nu) - 1 and i < 2 * int(nu) - 1:
            gamma.append(n + 2 * int(nu) - 2 * (i + 1))
        else:
            gamma.append(n - i)
    for_ans.sort()
    for i in range(0, n):
        ans.append((for_ans[gamma[i]-1][1], i))
    return ans


def get_provident_greedy_solution_upgrade(matrix, nu, k):
    # T(K)G Аналогично бережливо жадному, только в момент
    # применения бережливого алгоритма берём не самый минимальный,
    # а k-ый по возрастанию (1 <= k <= n-v+2)
    n = len(matrix)
    block = [0] * n
    ans = []
    for i in range(n):
        k = min(k, n-i)
        if i < int(nu):
            for_ans = []
            for j in range(n):
                if block[j]:
                    continue
                for_ans.append([matrix[j][i], j])
            for_ans.sort()
            id = for_ans[k-1][1]
            block[id] = 1
            ans.append((id, i))
        else:
            id_mx = -1
            mx = -sys.maxsize
            for j in range(n):
                if block[j]:
                    continue
                if matrix[j][i] > mx:
                    id_mx = j
                    mx = matrix[j][i]
            block[id_mx] = 1
            ans.append((id_mx, i))
    return ans

def get_greedy_solution_upgrade(matrix, k):
    # G(k) Жадная страгия модифицированная. Но выбираем какие берём на k дней вперёд.
    n = len(matrix)
    block = [0] * n
    ans = []
    i = 0
    while i < n:
        if i + k <= n:
            #выбираем k максимальных значений
            for_ans = []
            for j in range(n):
                if block[j]:
                    continue
                for_ans.append([matrix[j][i], j])
            for_ans.sort()
            for_ans.reverse()
            for j in range(k):
                ans.append((for_ans[j][1],i + j))
                block[for_ans[j][1]] = 1
            i += k
        else:
            id = -1
            mx = -sys.maxsize - 1
            for j in range(n):
                if block[j]:
                    continue
                if matrix[j][i] > mx:
                    id = j
                    mx = matrix[j][i]
            block[id] = 1
            ans.append((id, i))
            i+=1
    return ans

def assignment_max(matrix):
    cost_matrix = -matrix.copy()
    cost_matrix = cost_matrix.transpose()

    indexes = linear_sum_assignment(cost_matrix)

    return indexes
def get_max_solution(matrix):
    for row in matrix:
        for i in range(len(row)):
            row[i] *= -1
    m = Munkres()
    indexes = m.compute(matrix)
    for row in matrix:
        for i in range(len(row)):
            row[i] *= -1
    return indexes

#def get_min_solution(matrix):
    #m = Munkres()
    #indexes = m.compute(matrix)
    #return indexes

def get_greedy_solution(matrix):
    n = len(matrix)
    block = [0] * n
    ans = []
    for i in range(n):
        id = -1
        mx = -sys.maxsize - 1
        for j in range(n):
            if block[j]:
                continue
            if matrix[j][i] > mx:
                id = j
                mx = matrix[j][i]
        block[id] = 1
        ans.append((id, i))
    return ans

def get_provident_solution(matrix):
    n = len(matrix)
    block = [0] * n
    ans = []
    for i in range(n):
        id = -1
        mn = sys.maxsize
        for j in range(n):
            if block[j]:
                continue
            if matrix[j][i] < mn:
                id = j
                mn = matrix[j][i]
        block[id] = 1
        ans.append((id, i))
    return ans

def get_greedy_provident_solution(matrix, nu):
    n = len(matrix)
    block = [0] * n
    ans = []
    for i in range(n):
        id_mn = -1
        id_mx = -1
        mx = -sys.maxsize
        mn = sys.maxsize-1
        for j in range(n):
            if block[j]:
                continue
            if matrix[j][i] < mn:
                id_mn = j
                mn = matrix[j][i]
            if matrix[j][i] > mx:
                id_mx = j
                mx = matrix[j][i]
        id = -1
        if(i < nu):
            id = id_mx
        else:
            id = id_mn
        block[id] = 1
        ans.append((id, i))
    return ans

def get_provident_greedy_solution(matrix, nu):
    n = len(matrix)
    block = [0] * n
    ans = []
    for i in range(n):
        id_mn = -1
        id_mx = -1
        mx = -sys.maxsize
        mn = sys.maxsize
        for j in range(n):
            if block[j]:
                continue
            if matrix[j][i] < mn:
                id_mn = j
                mn = matrix[j][i]
            if matrix[j][i] > mx:
                id_mx = j
                mx = matrix[j][i]
        id = -1
        if(i < (int)(nu)):
            id = id_mn
        else:
            id = id_mx
        block[id] = 1
        ans.append((id, i))
    return ans