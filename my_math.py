def lerp(vec1:list ,vec2:list ,t:float)->list:
    res = [0,0]
    res[0] += vec1[0] * (1-t) + vec2[0] * t
    res[1] += vec1[1] * (1-t) + vec2[1] * t
    return res 