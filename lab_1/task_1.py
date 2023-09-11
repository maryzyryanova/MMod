import random
from typing import Generator


def simple_event_generator(probability: float, n: int = 10**6) -> Generator[bool, None, None]:
    """

    :param probability:
    :param n:
    :return:
    """
    for _ in range(0, n):
        yield random.uniform(0, 1) <= probability


def simple_event_simulator(probability: float) -> None:
    """

    :param probability:
    :return:
    """
    if 0 <= probability <= 1.0:
        events = list(simple_event_generator(probability))
        practical = events.count(True) / len(events)
        print("Theoretical probability: " + str(probability))
        print("Practical probability: " + str(practical))
        if practical <= probability:
            print("Event has come!")
        else:
            print("Event hasn't come!")
    else:
        raise Exception("The probability is out of range!")