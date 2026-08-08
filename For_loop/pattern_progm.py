# # 🔹 1. Square of Stars
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

    # * * * * *
    # * * * * *
    # * * * * *
    # * * * * *
    # * * * * *

#============================================================
# # Right-Angled Triangle
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *


# r=6
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# ===========================================================================================
# 3. inverted Triangle
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

    # * * * * * *
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *
# =======================================================================================================================================================
#number triangle

# for i in range(1,7):
#     for j in range (i):
#         print(i,end=" ")
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
#==================================================================================================================
# for i in range(1,7):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# # 1 2 3 4 5 6
#===================================================================================================
#
# # 🔹 5. Right-Aligned Triangle
# rows = 5
# for i in range(1, rows + 1):
#     print("  " * (rows - i) + "* " * i)

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# ======================//////////////////////////////////////////////////'''''''''''''''''''''''''''''''
#pyramid
# r = 5
# for i in range (1,r+1):
#     print(" "*(r-i)+"* "* i+" "*(r-i))

# rows=6
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "* " * i)

#
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# ================================================================////////////////////////////////////////////////////////////////
# rows=6
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "* " * i)
#
# for j in range(rows-1,0,-1):
#     print(" " * (rows - j) + "* " * j)
# #
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

# ======================================================================================================
#hollow triangle
n = 5  # size of the square

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
# #     print()
#
# # * * * * *
# # *       *
# # *       *
# # *       *
# # * * * * *
#
# rows = 5
#
# for i in range(rows):
#     print(" " * (rows - i), end="")  # for formatting
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()
#  #     1
#  #    1 1
#  #   1 2 1
#  #  1 3 3 1
#  # 1 4 6 4 1
#
# rows = 5
# num = 1
#
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



# n = 9  # total columns
#
# for i in range(1, 4):  # rows = 3
#     for j in range(1, n + 1):
#         if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if (i==j):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n = 6
# for i in range(n):
#     for j in range(n):
#         if j == n-i-1:
#             print("*", end=" ")
#         else:
#                 print(" ",end=" ")
#     print()

# r=6
# for i in range (1,r):
#     for j in range(i,r):
#         print("*",end=" ")
#     print()
#

n = 4
for i in range(n):
    print("  " * i + "* " * (n - i))
