from time import sleep

from remind_me.schedule_jobs import sched

sched.start()

print(1)
while True:
    sleep(3)
    print(sched.get_jobs())
