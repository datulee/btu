class Health:
    def __init__(self, age, sex, heartbeat):
        self.age = age
        self.sex = sex
        self.heartbeat = heartbeat

    def __str__(self):
        return f"Age: {self.age}, sex: {self.sex}, heartbeat: {self.heartbeat}"

    def avg_length_of_life(self):
        minutes_of_life = 2600000000 / self.heartbeat
        years_of_life = minutes_of_life / 525600

        return int(years_of_life)

    def max_heartbeat(self):
        if self.sex == "F":
            max_heartbeat = 226 - (0.9 * self.age)
        elif self.sex == "M":
            max_heartbeat = 223 - (0.9 * self.age)
        else:
            print("Incorrect value of sex")

        return max_heartbeat

    def max_heartbeat_while_training(self, factor):
        if factor == 0.8:
            max_heartbeat_training = round((self.max_heartbeat() - self.heartbeat)*factor + self.heartbeat, 2)
            return f"you are intense trainer, your max heartbeat will be {max_heartbeat_training}"
        elif factor == 0.6:
            max_heartbeat_training = round((self.max_heartbeat() - self.heartbeat)*factor + self.heartbeat, 2)
            return f"you are average DATVIRTVA trainer, your max heartbeat will be {max_heartbeat_training}"
        elif factor == 0.5:
            max_heartbeat_training = round((self.max_heartbeat() - self.heartbeat)*factor + self.heartbeat, 2)
            return f"you are beginner trainer, your max heartbeat will be {max_heartbeat_training}"


h = Health(18, 'F', 60)
print(h.max_heartbeat_while_training(0.5))
print(h.max_heartbeat())
print(f"ANI SHEN ICOCXLEB {h.avg_length_of_life()} WELI")
print(h)
