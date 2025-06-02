ts = ThresholdSwitch()
ts.params_distibs(distribs=True)
ex_lif = ExtendedLIF(ts=ts)
time, voltage, resistance = ex_lif.calculate()