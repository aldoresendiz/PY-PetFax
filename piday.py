# def f(n):
#     if n == 1:
#         return 1/6
#     else:
#         return f(n - 1) +  1 / (n * ( 4 * n - 1) * ( 4 * n - 2))

# def g(n):
#     if n == 1:
#         return 1/30
#     else:
#         return  g(n - 1) + 1 / (n * ( 4 * n + 1) * ( 4 * n + 2))

# F = f(2024)
# G = g(2024)

# print(f(2024) + 3 - g(2024))
#print(result)

def find_f_g(n):
    f_n_minus_1 = 1/6
    g_n_minus_1 = 1/30
    f_n, g_n = 0, 0
    for i in range(2, n + 1):
        f_n = f_n_minus_1 + (1 / (i * (4 * i - 1) * (4 * i - 2)))
        g_n = g_n_minus_1 + (1 / (i * (4 * i + 1) * (4 * i + 2)))
        f_n_minus_1, g_n_minus_1 = f_n, g_n

    return f_n, g_n


F, G = find_f_g(2024)

print(F)
print(G)

results = F + 3 - G

print(f"Happy {results} Day!!!")

# def find_f_g(n):
#     f_n_minus_1 = 1/6
#     g_n_minus_1 = 1/30
#     print(f_n_minus_1)
#     print(g_n_minus_1)

#     f_n, g_n = 0  , 0
#     for i in range (2, n +1):
#         f_n = f_n_minus_1 + (1 / ( i * (4 * i  - 1)) * (4 * i - 2) )
#         g_n = g_n_minus_1  +( 1 / ( i * (4 * i  + 1)) * (4 * i + 2))
#         f_n_minus_1, g_n_minus_1 = f_n, g_n
    
#         # return f_n , g_n
#     return f_n , g_n


# F , G = find_f_g(2024)

# print(F)
# print(G)

# results = F + 3 - G

# print(f"Happy {results} Day!!!")