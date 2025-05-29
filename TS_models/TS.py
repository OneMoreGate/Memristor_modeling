import numpy as np

class ThresholdSwitch():
    R_off: float = 5e10
    R_on: float = 3e4
    V_th: float = 0.45
    V_hold: float = 0.05
    distribs: bool = False
    V_th_dist: float = V_th
    V_hold_dist: float = V_hold
    V_th_std: float = 0.03
    V_hold_std: float = 0.01

    def __init__(self,  R_off = R_off, R_on = R_on, V_th = V_th, V_hold = V_hold) -> None:
        self.R_off = R_off
        self.R_on = R_on
        self.V_th = V_th
        self.V_hold = V_hold
        self.state = 'off'

    def params_distibs(self, distribs = distribs, V_th_std = V_th_std, V_hold_std = V_hold_std) -> None:
        self.distribs = distribs
        self.V_th_std = V_th_std
        self.V_hold_std = V_hold_std

    def get_resistance(self, voltage: float) -> float:
        if (self.state == 'off') and ((voltage) < self.V_th):
            return self.R_off
        elif (self.state == 'off') and ((voltage) > self.V_th):
            self.state = 'on'
            if self.distribs == True:
                self.V_th = np.random.normal(loc = self.V_th_dist, scale = self.V_th_std)
            return self.R_on
        elif (self.state == 'on') and ((voltage) > self.V_hold):
            return self.R_on
        elif (self.state == 'on') and ((voltage) < self.V_hold):
            self.state = 'off'
            if self.distribs == True:
                self.V_hold = np.random.normal(loc = self.V_hold_dist, scale = self.V_hold_std)
            return self.R_off