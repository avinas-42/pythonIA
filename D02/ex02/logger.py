import time
from random import randint
import os
# ... definition of log decorator...


def log(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end = time.time()
        full_time = end - start
        time_string = f'{full_time * 1000:.3f} \
ms' if full_time < 0.0001 else f'{full_time:.3f} s'
        string = f'({os.getlogin()})Running: {f.__name__:19s}[ \
exec-time = ' + time_string + ' ]\n'
        fd = open("machine.log", "a")
        fd.write(string)
        fd.close()
        return ret
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
        self.water_level -= 1
        print(self.boil_water())
        print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
