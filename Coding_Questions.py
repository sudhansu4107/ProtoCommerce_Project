n = int(input("Please enter the size:"))

# -----------------------------increasing triangle/Right triangle-------------------------
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *
# --------------------------------Decreasing triangle/R.Downgrade triangle-------------------------------
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *
# ----------------------------Left triangle------------------------------
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=' ')
#     for j in range(i + 1):
#         print("x", end=" ")
#     print()
#
#
#           x
#         x x
#       x x x
#     x x x x
#   x x x x x
# -----------------------Left downgrade triangle----------------------------------
# for i in range(n):
#     for j in range(i + 1):
#         print(' ', end=" ")
#     for j in range(i, n):
#         print("x", end=" ")
#     print()

# x x x x x
#   x x x x
#     x x x
#       x x
#         x
# --------------------------Hill pattern------------------------------------
# for i in range(n):
#     for j in range(i, n):
#         print(' ', end=" ")
#     for j in range(i):  # To print one less column we use i
#         print('X', end=" ")
#     for j in range(i + 1):
#         print('X', end=" ")
#     print()

#         X
#       X X X
#     X X X X X
#   X X X X X X X
# X X X X X X X X X
# -------------------------Reverse Hill pattern-------------------------
# for i in range(n):
#     # empty triangle
#     for j in range(i + 1):
#         print(' ', end=" ")
#     for j in range(i,n-1):  # To print one less column we use n-1
#         print("X", end=" ")
#     for j in range(i, n):
#         print("X", end=" ")
#     print()
#


# -------------------------Find the below  code for Diamond pattern---------------------------------

# for i in range(n-1):  # Code  to reduce  one row we use n-1
#     for j in range(i,n):
#         print(' ',end=" ")
#     for j in range(i):
#         print('X',end=" ")
#     for j in range(i+1):
#         print('X',end=" ")
#     print()
#
# for i in range(n):
#     # empty triangle
#     for j in range(i + 1):
#         print(' ', end=" ")
#     for j in range(i,n-1):
#         print("X", end=" ")
#     for j in range(i, n):
#         print("X", end=" ")
#     print()

# --------------Pyramid------------------
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for j in range(i):
#         print("X",end=" ")
#     for j in range(i+1):
#         print("X",end=" ")
#     print()

# -------------------- Pyramid--------------------
row=0

while row<n:
    space=n-row-1
    while space>0:
        print(end=" ")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()
#------------------Thankyou  ---------------------------
