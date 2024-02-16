import random
import string

import threading
import time
import psutil
import logging

logger = logging.getLogger("")


def stress_function(sleep_period):
    # For each level unit of stress, generate 100MB of data and store it in the memory
    logger.info("creating a memory consumer")
    mem_consumer = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=100_000_000))

    logger.info(f"CPU % usage: {psutil.cpu_percent()}")
    logger.info(f"Memory usage: {psutil.virtual_memory()}")

    logger.info(f"Memory % usage: {psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}")

    time.sleep(sleep_period)
    logger.info(f"Removing memory consumer of size {len(mem_consumer.encode('utf-8'))}")


def generate_tasks(amount, sleep_period):
    tasks = []

    for _ in amount:
        tasks.append(
            threading.Thread(target=stress_function, args=(sleep_period,)),
        )

    return tasks


def run_tasks(tasks):
    for idx, t in enumerate(tasks, 1):
        logger.info(f"Starting task no. {str(idx)}")
        t.start()
        logger.info(f"Done starting task no. {str(idx)}")


def perform_stress_test(stress_level: int):
    tasks = generate_tasks(range(stress_level), 100)
    run_tasks(tasks)
