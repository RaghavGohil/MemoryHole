import my_math
from global_data import GlobalData

class Tween: # only linear interpolation
    def __init__(self)->None:
        self.elapsed = 0
        self.finished = False
        
    def count(self,time_in_seconds:float)->None:
        self.elapsed += GlobalData.deltatime/time_in_seconds
        if self.elapsed > time_in_seconds:
            self.finished = True

    def value(self,from_val:float,to_val:float,time_in_seconds:float)->float:
        self.elapsed += GlobalData.deltatime/time_in_seconds
        if self.elapsed < 1:
            return my_math.lerp(from_val,to_val,self.elapsed)
        else:
            self.finished = True
            return to_val