import sys
import time
import threading
name = "Aidan"
number = "nee"

def callMe(name, number):
    print("&: Hello?")
    time.sleep(1)
    print("&: Who's there?")
    time.sleep(1)
    print("#: It's me "+ name)
    time.sleep(1)
    print("&:Hi "+ name+ " i'm sorry i'm busy right now can i call you back?")
    time.sleep(1)
    print("#: sure thing.")
    time.sleep(1)
    print("&: What's your number?")
    time.sleep(1)
    print("#it's "+number)
    time.sleep(1)
    print("&: Got it! call you later, Bye!")
    time.sleep(1)
    print("#: Bye!")
    time.sleep(1)
    print("click...")

thread1 = threading.Thread(target=callMe)
thread1.start()
