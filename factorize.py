from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from math import fabs
from datetime import datetime
import logging


def timer_handler(func):
    def wrapper(*args):
        start_time = datetime.now()
        func(*args)
        logging.debug(f"Execution time: {datetime.now() - start_time}")

    return wrapper


def divisible_without_remainder(number):
    number = int(fabs(number))
    outcome = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            outcome.append(i)
    outcome.append(number)
    return outcome


@timer_handler
def factorize(*number):
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        return list(executor.map(divisible_without_remainder, list(number)))


@timer_handler
def factorize_synchro(*number):
    numbers = list(number)
    return [divisible_without_remainder(number) for number in numbers]


# execution time test with slightly larger numbers than in the exercise
# to show the difference and to give the multiprocessing solution a chance
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    factorize(128128128, 255255255, 999999999, 106510600)
    factorize_synchro(128128128, 255255255, 999999999, 106510600)
