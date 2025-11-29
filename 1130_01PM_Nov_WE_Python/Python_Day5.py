"""
Bitwise Operator:-
    and =>  &
    or  =>  |

a = 7
b = 5
print(a and b)
print(b and a)
print(a or b)
print(b or a)


a = 19
b = 28
print( a & b )
Answer =>   16


a = 29
b = 42
print( a & b )


a = 29
b = 42
print( a | b )


a = 47
b = 56
print( (a | b)-(a & b) )
Answer =>    23

~ (tile)
a = 8
print( a )
print( ~a )
Answer =>   -9

a = -4
print( a )
print( ~a )
Answer =>   3



a = 5
b = 10
print(a < b < 20)
# print(a < b AND b < 20)   => True


x = True        # 1
y = False       # 0
print(x + y * x)
# print(1 + 0*1)   #PEMDAS
# print(1 + 0)


print(4 ** 0 ** 2)
# 4**0**2 => 4**(0**2) => 4**(0) => 1
# print(0**0)   also 0



a = 12
b = 5
print(a ^ b)   #  ^ XOR operator (if all inputs are same answer is 0 otherwise 1)
# 1100
# 0101
# 1001 =>  9 Ans


print((3 and 0) or (0 and 3))
# (3 and 0) or (0 and 3)
# 0 or 0
# 0


print(256 is 256)  # True
print(257 is 257)  # True


a = 7
print(~a + 1)
#  -8 + 1 => -7


a = True
b = False
print((a or b) and not (a and b))
#  (a or b) and not (a and b)
#  True and not (a and b)
#  True and not False
#  True and True
#  True


print(10 > 5 == True)
# (10 > 5 == True)
# (10 > 5 AND 5 == True)
# ( True AND False )
# False


"""






