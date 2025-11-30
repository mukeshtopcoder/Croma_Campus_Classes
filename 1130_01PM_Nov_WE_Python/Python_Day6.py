"""
print(2 + 3 * 4 ** 2 // 8 % 3)
# 2 + 3 * 4 ** 2 // 8 % 3
# 2 + 3 * 16 // 8 % 3
# 2 + 48 // 8 % 3
# 2 + 6 % 3
# 2 + 0
# 2   Answer
# PEMDAS
# P => Parenthesis ()
# E => Exponential **
# M Muln * , D Div / , // , % , A Add + , S Sub - (LTR)
# *= , -= , += etc
# >>  ,   <<


Bitwise Operator
Left Shift   <<
Right Shift  >>

a = 27
print(a>>2)
# Answer =>  6

a = 19
print(a>>1)
print(a>>2)
print(a>>3)
9 , 4 , 2 will be answer

a = 5
print(a<<1)
print(a<<2)
10 , 20 will be the amswer


print(1 << 2 + 1)
# 1<<2+1
# 1<<3
# 8 Answer


a = 3
b = 2
a *= b + 1  #   a = a*b+1  => 6+1 => 7 (but there is *=)
print(a)

# a *= b + 1
# a *= 3
# a = a*3
# a = 9


print(3 < 5 > 2 == 2)
# 3 < 5 > 2 == 2
# 3<5 AND 5>2 AND 2==2
# True AND True AND True
# True

print(10 // 3 * 3 + 1 % 3)

# 10 // 3 * 3 + 1 % 3
# 3*3+1%3
# 9+1%3
# 9+1
# 10


x = 10
y = 20
print(x & y | x ^ y)

# x & y | x ^ y
# (x&y)|(x^y)
# (10&20) | (10^20)
# 0 | 30
# 30


a = True
b = False
print(a & b or a ^ b)

# a & b or a ^ b
# (a&b) or (a^b)      ^ XOR => if both are same (False) otherwise True
# False or True
# True

x = 8
print(x >> 1 << 2)
# x>>1<<2
# 8>>1 <<2
# 4<<2
# 16

print(5 + True * False + (not False) )
# 5 + True * False + (not False)
# 5 + True * False + True
# 5 + 0 + True
# 5 + 0 + 1
# 6


print((not 0) * (False or 1))

# (not 0) * (False or 1)
# True * (False or 1)
# True * True
# 1


print(4 + 3 * 2 ** 2 // 2 - 1)

# 4 + 3 * 2 ** 2 // 2 - 1
# 4 + 3 * 4 // 2 - 1
# 4 + 3 * 4 // 2 - 1
# 4 + 12//2 - 1
# 4 + 6 - 1
# 9

"""
