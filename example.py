import seagull_scaring as ss

scarer = ss.Scarer(
    r"media\seagull.wav",
    2700,
    60,
    300,
    "ssv2cfg.ini",
    "ss_log.txt",
)
scarer.start()
