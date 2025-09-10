import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("data/simulation_metrics.csv")

def plot_efficiency():
    plt.figure(figsize=(8, 4))
    plt.plot(df['hour'], df['efficiency'], marker='o', color='green')
    plt.title("Efficiency Over Time")
    plt.xlabel("Hour of Day")
    plt.ylabel("Efficiency (%)")
    plt.grid(True)
    plt.savefig("charts/efficiency_over_time.png")
    plt.close()

def plot_resource_utilization():
    plt.figure(figsize=(8, 5))
    plt.plot(df['hour'], df['cpu_usage'], label='CPU Usage', color='red')
    plt.plot(df['hour'], df['memory_usage'], label='Memory Usage', color='blue')
    plt.plot(df['hour'], df['db_usage'], label='DB Usage', color='purple')
    plt.axhline(85, color='gray', linestyle='--', label='CPU Threshold')
    plt.axhline(80, color='gray', linestyle='--', label='Memory Threshold')
    plt.axhline(90, color='gray', linestyle='--', label='DB Threshold')
    plt.title("Resource Utilization Over Time")
    plt.xlabel("Hour")
    plt.ylabel("Usage (%)")
    plt.legend()
    plt.grid(True)
    plt.savefig("charts/resource_utilization.png")
    plt.close()

def plot_execution_times():
    job_types = ['High Priority API', 'Medium Task', 'Batch Job', 'Background Sync']
    exec_times = [120, 450, 1500, 2100]

    plt.figure(figsize=(8, 5))
    sns.barplot(x=job_types, y=exec_times, palette="muted")
    plt.title("Average Job Execution Time")
    plt.ylabel("Execution Time (ms)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("charts/job_execution_times.png")
    plt.close()

def plot_gantt_chart():
    jobs = ['J1', 'J2', 'J3', 'J4']
    start_times = [0, 3, 7, 10]
    durations = [3, 4, 2, 5]
    resources = ['R1', 'R2', 'R1', 'R2']

    plt.figure(figsize=(10, 4))
    for i in range(len(jobs)):
        plt.barh(resources[i], durations[i], left=start_times[i], label=jobs[i])
        plt.text(start_times[i] + 0.2, i % 2 + 0.1, jobs[i], fontsize=8)

    plt.xlabel("Time")
    plt.title("Job Schedule Timeline (Gantt Style)")
    plt.grid(True)
    plt.savefig("charts/job_schedule_timeline.png")
    plt.close()

# Run all
if __name__ == "__main__":
    plot_efficiency()
    plot_resource_utilization()
    plot_execution_times()
    plot_gantt_chart()
    print("✅ All charts saved in /charts/")
