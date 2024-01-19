from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from math import fabs
from datetime import datetime


def divisible_without_remainder(number):
    number = int(fabs(number))
    outcome = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            outcome.append(i)
    outcome.append(number)
    return outcome


def factorize(*number):
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        return list(executor.map(divisible_without_remainder, list(number)))


def factorize_synchro(*number):
    numbers = list(number)
    return [divisible_without_remainder(number) for number in numbers]


# execution time test with slightly larger numbers than in the exercise
# to show the difference and to give the multiprocessing solution a chance
if __name__ == "__main__":
    start_time = datetime.now()
    factorize(128128128, 255255255, 999999999, 106510600)
    print(f"Czas wykonania w wielu procesach: {datetime.now() - start_time}")

    start_time = datetime.now()
    factorize_synchro(128128128, 255255255, 999999999, 106510600)
    print(f"Czas wykonania w jednym procesie: {datetime.now() - start_time}")
