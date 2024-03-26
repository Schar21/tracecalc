class trace:
    def __init__(self, rare1, rare2, rare3):
        self.rare1 = rare1
        self.rare2 = rare2
        self.rare3 = rare3

    def base_amt(self):
        return self.rare1 + self.rare2 * 3 + self.rare3 * 9


def diff():
    per_run_hsr = trace(1.25, 1, 0.158)
    per_run_gen = trace(2.2, 1.97, 0.24)
    game = input(" For which game do you want to calculate for? (H/G): ")
    if game.upper() == "H":
        differ = max_trace_hsr.base_amt() - current_trace.base_amt()
        erun = per_run_hsr.base_amt()
        runs = int(differ / erun)
        days = int(runs / max_runs_daily_hsr)
        if differ == 0:
            return " The total amount of trace materials is sufficient. "
        elif differ < 0:
            return f" You have exceeded the required amount of runs by {-runs}, and have farmed for {-days} days more. "
        elif differ > 0:
            print(f" The maximum amount of runs to max out a character is {int(max_trace_hsr.base_amt() / erun)},"
                  f" or around {int(max_trace_hsr.base_amt() / (erun * max_runs_daily_hsr))} days.")
            return (f" You need to farm for an additional {days} day(s),"
                    f" and run an average of {runs} more runs to have sufficient amount of traces. ")
    elif game.upper() == "G":
        differ = max_trace_gen.base_amt() - current_trace.base_amt()
        erun = per_run_gen.base_amt()
        runs = int(differ / erun)
        days = int(runs / max_runs_daily_gen)
        if differ == 0:
            return " The total amount of talent books is sufficient. "
        elif differ < 0:
            return f" You have exceeded the required amount of runs by {-runs}, and have farmed for {-days} days more. "
        elif differ > 0:
            print(f" For a single crown you need {int(max_trace_gen.base_amt() / (erun * 3))} runs.")
            print(f" For a double crown you need {int((max_trace_gen.base_amt() * 2) / (erun * 3))} runs.")
            print(f" For a triple crown you need {int(max_trace_gen.base_amt() / erun)} runs.")
            print(
                f" The maximum amount of runs to single crown a character is {int(max_trace_gen.base_amt() / (3 * erun))},"
                f" or around"
                f" {int(max_trace_gen.base_amt() / (3 * erun * max_runs_daily_gen))} days.")
            print(
                f" The maximum amount of runs to double crown a character is {int((max_trace_gen.base_amt() * 2) / (3 * erun))},"
                f" or around"
                f" {int((2 * max_trace_gen.base_amt()) / (3 * erun * max_runs_daily_gen))} days.")
            print(f" The maximum amount of runs to triple crown a character is {int(max_trace_gen.base_amt() / erun)},"
                  f" or around"
                  f" {int(max_trace_gen.base_amt() / (erun * max_runs_daily_gen))} days.")
            return (f" You need to farm for an additional {days} day(s),"
                    f" and run an average of {runs} more runs to have sufficient amount of talent books. ")


max_trace_hsr = trace(18, 69, 139)
max_trace_gen = trace(9, 114, 63)
max_power_hsr = 240
max_runs_daily_hsr = 24
max_power_gen = 160
max_runs_daily_gen = 8
c1 = int(input(" Please enter trace materials/books of rarity 1: "))
c2 = int(input(" Please enter trace materials/books of rarity 2: "))
c3 = int(input(" Please enter trace materials/books of rarity 3: "))

current_trace = trace(c1, c2, c3)

print(diff())

