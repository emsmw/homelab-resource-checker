import psutil
import math

def get_mem_status():
    BAR_LENGTH = 30
    memory_b = psutil.virtual_memory()
    memory_total_gb = memory_b.total / 1024 ** 3
    memory_used_gb = memory_b.used / 1024 ** 3
    memory_free_gb = memory_b.free / 1024 ** 3
    used_memory_percentage = math.floor(memory_used_gb / memory_total_gb * 100)

    bar_filled_length = int((math.ceil(used_memory_percentage) / 100) * BAR_LENGTH)
    bar = "█" * bar_filled_length + " " * (BAR_LENGTH - bar_filled_length)


    print("=" * 70)
    print("                        MEMORY USAGE                       ")
    print("=" * 70)
    print(f"Total Memory: {memory_total_gb:5.1f} GB")
    print(f"Used Memory : {memory_used_gb:5.1f} GB")
    print(f"Free Memory : {memory_free_gb:5.1f} GB")
    print(f"[{bar}] {math.ceil(used_memory_percentage):5.0f}% used")