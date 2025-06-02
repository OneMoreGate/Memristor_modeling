class ExtendedLIF():
    I_inj: float = 5e-7
    C_m: float = 3e-10
    R_r: float = 1e6
    V_c_init: float = 0

    def __init__(self, ts: ThresholdSwitch, I_inj = I_inj, R_r = R_r, C_m = C_m) -> None:
        self.ts = ts
        self.I_inj = I_inj
        self.R_r = R_r
        self.C_m = C_m

    def initial_conditions(self, V_c_init = V_c_init) -> None:
        self.V_c_init = V_c_init

    def calculate(self, time_interval: float = 0.001, dots: int = 100000) -> tuple:
        self.R_ts = [self.ts.get_resistance(self.V_c_init)]
        self.V_c = [self.V_c_init]
        time_array = np.linspace(0, time_interval, dots)
        delta_t = time_array[1] - time_array[0]
        for i in range(1, dots):
            self.V_c.append((self.I_inj - self.V_c[i - 1] / self.R_ts[i - 1]) * (delta_t / self.C_m) + self.V_c[i - 1])
            self.R_ts.append(self.ts.get_resistance(self.V_c[i]))
        return time_array, self.V_c, self.R_ts