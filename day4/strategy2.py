import datetime

class Entry():
    def __init__(self, dt : datetime, msg: str):
        self.dt = dt
        self.msg = msg

    def __lt__(self, other):
        return self.dt < other.dt

    def __cmp__(self, other):
        return cmp(self.dt, other.dt) 

entries = []   
with open('input.txt', 'r') as f:
    for line in f:
        line = line.replace('[', '')
        line = line.replace(']', '')
        tokens = line.split(' ', 2)
        year = int(tokens[0][0:4])
        month = int(tokens[0][5:7])
        day = int(tokens[0][8:10])
        hour = int(tokens[1][0:2])
        minute = int(tokens[1][3:5])

        msg = tokens[2].rstrip()

        dt = datetime.datetime(year, month, day, hour, minute)
        entry = Entry(dt, msg) 
        entries.append(entry)

entries.sort()

currentGuard = 0
sleepSchedule = dict()
sleepTime = 0

for entry in entries:
    msg = entry.msg
    #new guard shift
    if msg.startswith('G'):
        currentGuard = int(msg.split(' ')[1].replace('#', ''))
        if currentGuard not in sleepSchedule:
            sleepSchedule[currentGuard] = [0] * 60

    #falls asleep
    elif msg.startswith('f'):
        sleepTime = entry.dt.minute

    #wakes up
    elif msg.startswith('w'):
        awakeTime = entry.dt.minute
        for i in range(sleepTime, awakeTime):
            sleepSchedule[currentGuard][i] += 1

sleepiestGuard = None
sleepiestMinute = -1
sleepiestMax = -1

for key, sched in sleepSchedule.items():
    for minute, amount in enumerate(sched):
        if amount > sleepiestMax:
            sleepiestMax = amount
            sleepiestGuard = key
            sleepiestMinute = minute

print(sleepiestGuard * sleepiestMinute)
    