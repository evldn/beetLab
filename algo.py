import sys
from munkres import Munkres
from scipy.optimize import linear_sum_assignment

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