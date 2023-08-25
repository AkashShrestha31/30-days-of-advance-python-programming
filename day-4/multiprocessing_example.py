import multiprocessing



if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()
    print("All processes have finished.", cpu_count)
