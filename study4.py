#1
def s1(num):
    return int(num) ** 2
ans = s1("10")

#2
def s2(num):
    print(str(num))
ans = s2("hello")


#3
def add(a,b,c,x=2, y=2):
    """
    return 3 + 5 + 3.
    hissu 3
    opusyon 2
    : param x: int.
    : param y: int.
    : param z: int.
    """
    return x + y
ans3 = add(3,5,2)
print(ans3)

#4
def two(start):
    """
    ans4_1 = integer / 2.
    : param ans4_1: int.
    : param integer: int.
    """
    ans4_1 = start
    ans4_1 /= 2
    return ans4_1
def four(r):
    """
    return = r * 4.
    """
    
    r *= 4
    return r

result1 = two(40)
print(result1)

result2 = four(20)
print(result2)

ans4 = two(6)
result3 = four(ans4)
print(result3)


#5
def change_float(num):
    """
    try-except.
    change to float.
    """
    try:
        A = float(num)
        return A
    except(ValueError):
        print("invalid input")




result = change_float("Hello")
print(result)


