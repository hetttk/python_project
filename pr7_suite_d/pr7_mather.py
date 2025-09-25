
import math

def calc_fact(n):
    return 1 if n<=1 else n*calc_fact(n-1)

def calc_ci(p, r, t):
    return round(p * ((1 + r/100.0) ** t), 2)

def angles_math(angle_deg):
    rad = math.radians(angle_deg)
    return round(math.sin(rad),4), round(math.cos(rad),4), round(math.tan(rad),4)

def figure_area(shape, *args):
    if shape=="circle":
        return round(math.pi * args[0]**2, 2)
    if shape=="rect":
        return args[0]*args[1]
    if shape=="tri":
        return 0.5*args[0]*args[1]
    return None
