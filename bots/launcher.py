import multiprocessing
import time
from open_browser import open

NUM_ROBOTS = 10

def start_robot(index):
    open()

if __name__ == "__main__":
    processes = []

    for i in range(NUM_ROBOTS):
        p = multiprocessing.Process(target=start_robot, args=(i,))
        p.start()
        processes.append(p)
        time.sleep(0.3)  # pequena pausa para estabilidade

    for p in processes:
        p.join()
