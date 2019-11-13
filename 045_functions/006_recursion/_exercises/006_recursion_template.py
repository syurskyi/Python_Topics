# Recursive Functions

# ___ mysum L
#     __ n_ L
#         r_ 0
#     e_
#         r_ L_0_ + m_(L_1___  # Call myself


# ___ m_
#     print m_([1 2 3 4 5]))

# print()
# ######################################################################################################################
# Recursive Functions

# ___ mysum
#     print L
#     __ n_ L
#         r_ 0
#     ___
#         r_ L_0_ + m_(L_1___  # Call myself

# ___ main
#     print m_([1, 2, 3, 4, 5]))

# print()
# ######################################################################################################################
# Recursive Functions

# ___ mysum
#     __ ___ L r__ 0
#     r_ nonempty 0  # Call a function that calls me

# ___ nonempty L
#     r_ L_0_ + mysum(L_1___  # Indirectly recursive

# ___ m_
#     print(m_([1.1, 2.2, 3.3, 4.4]))

# print()
# ######################################################################################################################
# Indirect Function Call

# ___ echo message  # Name echo assigned to function object
#     print message

# echo Direct call

# x  echo  # Now x references the function too
# x Indirect call!  # Call object through name by adding ()

# ___ indirect func arg
#     func arg  # Call the passed-in object by adding ()


# i_(e_ Argument call!  # Pass the function to another function

# print()