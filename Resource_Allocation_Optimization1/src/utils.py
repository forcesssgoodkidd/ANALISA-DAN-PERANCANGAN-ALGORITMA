import time
import tracemalloc

def analyze_performance(func, tasks, resources):
    """
    Mengukur waktu eksekusi dan penggunaan memori
    """
    tracemalloc.start()
    start_time = time.time()

    result = func(tasks, resources)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = round(end_time - start_time, 6)
    memory_usage = round(peak / 1024, 2)  # KB
def compare_cpu_gpu(allocation):
    cpu_energy = 0
    gpu_energy = 0

    for item in allocation:
        if item["resource"] == "CPU":
            cpu_energy += item["energy"]
        elif item["resource"] == "GPU":
            gpu_energy += item["energy"]

    return cpu_energy, gpu_energy
   

    return result, execution_time, memory_usage
