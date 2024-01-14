# your code goes here!
import time

def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!', flush=True)
        time.sleep(1)
        number -= 1
    print("HAPPY NEW YEAR!", flush=True)

countdown_with_sleep(5)