class trace:
    def __init__(self, rare1, rare2, rare3):
        self.rare1 = rare1
        self.rare2 = rare2
        self.rare3 = rare3

    def base_amt(self):
        return self.rare1 + self.rare2 * 3 + self.rare3 * 9


def diff():
    differ = max_trace.base_amt() - current_trace.base_amt()
    per_run = trace(1.25, 1, 0.158)
    erun = per_run.base_amt()
    runs = int(differ / erun)
    days = int(runs/max_runs_daily)
    print(f" The maximum amount of runs to max out a character is {int(max_trace.base_amt()/erun)}, or around"
          f" {int(max_trace.base_amt()/(erun*max_runs_daily))} days.")
    if differ == 0:
        return " The total amount of trace materials is sufficient. "
    elif differ < 0:
        return f" You have exceeded the required amount of runs by {-runs}, and have farmed for {-days} days more. "
    elif differ > 0:
        return (f" You need to farm for an additional {days} day(s),"
                f" and run an average of {runs} more runs to have sufficient amount of traces. ")


max_trace = trace(18, 69, 139)
print(f" The maximum trace materials required to max out a character is {max_trace.base_amt()}")
max_power = 240
max_runs_daily = 240/10
c1 = int(input(" Please enter trace materials of rarity 1: "))
c2 = int(input(" Please enter trace materials of rarity 2: "))
c3 = int(input(" Please enter trace materials of rarity 3: "))

current_trace = trace(c1, c2, c3)

print(diff())

