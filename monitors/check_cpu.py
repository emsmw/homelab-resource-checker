import psutil
import math
logical_cpu_cores = psutil.cpu_count(logical=True)
BAR_LENGTH = 50

#CPU
core_use_percentages = psutil.cpu_percent(interval=1, percpu=True)

print("=" * 70)
print("                        CPU USAGE PER CORE                        ")
print("=" * 70)

for core_num, percentage in enumerate(core_use_percentages, start=1):

    bar_filled_length = int((math.ceil(percentage) / 100) * BAR_LENGTH)
    bar = "█" * bar_filled_length + " " * (BAR_LENGTH - bar_filled_length)
    print(f"Core {core_num:2} [{bar}] {math.ceil(percentage):5.0f}%")

print("=" * 70)
