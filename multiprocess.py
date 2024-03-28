import multiprocessing
import time


def perform_operation(numbers_queue, result_queue):
    while not numbers_queue.empty():
        try:
            # Try to get numbers from the queue; if it's empty, catch the Empty exception
            a, b = numbers_queue.get_nowait()
        except multiprocessing.queues.Empty:
            break

        # Perform an arithmetic operation (addition in this case)
        result = a + b

        # Simulate some work by sleeping
        time.sleep(1)

        # Put the result back in the result queue
        result_queue.put(result)


if __name__ == "__main__":
    # Create two queues: one for the numbers to add, and one for the result
    numbers_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    # Put tuples of numbers into the numbers queue
    for _ in range(10):
        numbers_queue.put((10, 20))

    # Create and start 10 subprocesses
    processes = [multiprocessing.Process(target=perform_operation, args=(numbers_queue, result_queue)) for _ in
                 range(10)]
    for process in processes:
        process.start()

    # Wait for all subprocesses to finish
    for process in processes:
        process.join()

    # Retrieve and sum the results from the result queue
    total_result = 0
    while not result_queue.empty():
        total_result += result_queue.get()

    print(f"The total result is: {total_result}")
