def simplify_fraction(a,b):
    if a > b:
        greater = a
    else:
        greater = b
    t = 1
    while(t < greater):
        t += 1
        if a % t == 0 and b % t == 0:
            a = a / t
            b = b / t
            t = 1
    return f"{int(a)}/{int(b)}"

def slope_formula(x1,y1,x2,y2):
    rise = y2 - y1
    run = x2 - x1
    answer = simplify_fraction(rise, run)
    return answer

print(slope_formula(6,-11,10,9), "Is your slope!")
