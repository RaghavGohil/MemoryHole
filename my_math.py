import math

def lerp(a:float,b:float,t:float)->float:
    res = 0
    res += a * (1-t) + b*t
    return res

def vec_lerp(vec1:list ,vec2:list ,t:float)->list:
    res = [0,0]
    res[0] += vec1[0] * (1-t) + vec2[0] * t
    res[1] += vec1[1] * (1-t) + vec2[1] * t
    return res 

def vec_normalize(vec:list)->list:
    mag = math.sqrt(vec[0]**2+vec[1]**2)
    vec = [vec[0]/mag,vec[1]/mag]
    return vec 

def vec_mul(vec:list,n)->list:
    return [vec[0]*n,vec[1]*n] 

def vec_add(vec1:list,vec2:list)->list:
    return [vec1[0]+vec2[0],vec1[1]+vec2[1]]

def vec_is_zero(vec:list)->bool:
    return True if vec[0] == 0 and vec[1] == 0 else False
