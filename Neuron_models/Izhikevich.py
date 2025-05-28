import numpy as np

class Izhikevich():
    a: float  = 0.02
    b: float = 0.2
    c: float  = -65
    d: float = 2
    I: float = 15
    v_init: float = c
    u_init: float = 0

    def __init__(self, a = a, b = b, c = c, d = d, I = I) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.a = a
        self.I = I
    
    def initial_conditions(self, v_init = v_init, u_init = u_init) -> None:
        self.v_init = v_init
        self.u_init = u_init

    def calculate(self, time_interval: float = 100, dots: int = 100000) -> tuple:
        self.v: list = [self.v_init]
        self.u: list = [self.u_init]
        time_array = np.linspace(0, time_interval, dots)
        delta_t = time_array[1] - time_array[0]
        for i in range(dots - 1):
            if self.v[i] >= 30:
                self.v.append(self.c)
                self.u.append(self.u[i] + self.d)
            else:
                self.v.append((0.04 * self.v[i] ** 2 + 5 * self.v[i] + 140 - self.u[i] + self.I) * delta_t + self.v[i])
                self.u.append(self.a * (self.b * self.v[i] - self.u[i]) * delta_t + self.u[i])
        return time_array, self.v, self.u
    
    