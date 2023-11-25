import time

seconds=input("enter the time in seconds:")
def countdown_timer(seconds):
    mins=int(seconds/60)
    secs=int(seconds%60)

    timer=f'{mins}:{secs}'
    print(timer)
    seconds-=1
    print("times up")

countdown_timer(int(seconds))