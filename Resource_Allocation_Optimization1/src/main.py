import time
import tracemalloc
import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =====================================================
# ALGORITMA RESOURCE ALLOCATION (ENERGY AWARE)
# =====================================================
def resource_allocation(tasks, cpu_power, gpu_power):
    allocation = []
    operation_count = 0

    for task in tasks:
        operation_count += 1

        cpu_energy = task / cpu_power
        gpu_energy = task / gpu_power

        if cpu_energy <= gpu_energy:
            allocation.append({
                "task": task,
                "resource": "CPU",
                "energy": cpu_energy
            })
        else:
            allocation.append({
                "task": task,
                "resource": "GPU",
                "energy": gpu_energy
            })

    return allocation, operation_count


# =====================================================
# ANALISIS PERFORMA
# =====================================================
def analyze(tasks, cpu_power, gpu_power):
    tracemalloc.start()
    start_time = time.time()

    allocation, ops = resource_allocation(tasks, cpu_power, gpu_power)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return allocation, ops, end_time - start_time, peak / 1024


# =====================================================
# GUI
# =====================================================
def run_gui():
    # ---------------- WINDOW ----------------
    window = tk.Tk()
    window.title("Resource Allocation Optimization")
    window.geometry("1000x600")
    window.resizable(True, True)

    style = ttk.Style()
    style.theme_use("clam")

    # ---------------- LAYOUT ----------------
    main_frame = ttk.Frame(window)
    main_frame.pack(fill="both", expand=True, padx=15, pady=15)

    left = ttk.Frame(main_frame)
    left.pack(side="left", fill="both", expand=True, padx=10)

    right = ttk.Frame(main_frame)
    right.pack(side="right", fill="both", expand=True, padx=10)

    # ---------------- TITLE ----------------
    title = ttk.Label(
        left,
        text="Resource Allocation Optimization\nEfisiensi Energi CPU vs GPU",
        font=("Segoe UI", 15, "bold")
    )
    title.pack(pady=10)

    # ---------------- INPUT ----------------
    input_frame = ttk.LabelFrame(left, text="Input")
    input_frame.pack(fill="x", pady=10)

    ttk.Label(input_frame, text="Tasks").grid(row=0, column=0, sticky="w", pady=5)
    entry_tasks = ttk.Entry(input_frame)
    entry_tasks.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="CPU Power").grid(row=1, column=0, sticky="w", pady=5)
    entry_cpu = ttk.Entry(input_frame)
    entry_cpu.insert(0, "2")
    entry_cpu.grid(row=1, column=1, padx=5)

    ttk.Label(input_frame, text="GPU Power").grid(row=2, column=0, sticky="w", pady=5)
    entry_gpu = ttk.Entry(input_frame)
    entry_gpu.insert(0, "5")
    entry_gpu.grid(row=2, column=1, padx=5)

    # ---------------- OUTPUT ----------------
    output_frame = ttk.LabelFrame(left, text="Output")
    output_frame.pack(fill="both", expand=True, pady=10)

    output_text = tk.Text(
        output_frame,
        font=("Consolas", 10),
        bg="#ecf0f1"
    )
    output_text.pack(fill="both", expand=True, padx=5, pady=5)

    # ---------------- GRAPH ----------------
    fig = Figure(figsize=(4.5, 4))
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=right)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # ---------------- SIMULATION ----------------
    def run_simulation():
        try:
            tasks = list(map(int, entry_tasks.get().split(",")))
            cpu_power = float(entry_cpu.get())
            gpu_power = float(entry_gpu.get())

            allocation, ops, exec_time, memory = analyze(tasks, cpu_power, gpu_power)

            # OUTPUT TEXT
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "HASIL ALOKASI RESOURCE\n")
            output_text.insert(tk.END, "-" * 40 + "\n")

            cpu_energy = 0
            gpu_energy = 0

            for item in allocation:
                output_text.insert(
                    tk.END,
                    f"Task {item['task']:>3} → {item['resource']} | Energy {item['energy']:.2f}\n"
                )
                if item["resource"] == "CPU":
                    cpu_energy += item["energy"]
                else:
                    gpu_energy += item["energy"]

            output_text.insert(tk.END, "\nANALISIS\n")
            output_text.insert(tk.END, "-" * 40 + "\n")
            output_text.insert(tk.END, f"Operasi       : {ops}\n")
            output_text.insert(tk.END, f"Waktu Eksekusi: {exec_time:.6f} detik\n")
            output_text.insert(tk.END, f"Memori        : {memory:.2f} KB\n")

            # GRAPH UPDATE
            ax.clear()
            ax.bar(["CPU", "GPU"], [cpu_energy, gpu_energy])
            ax.set_title("Perbandingan Energi CPU vs GPU")
            ax.set_ylabel("Total Energy")
            canvas.draw()

        except Exception:
            messagebox.showerror(
                "Error",
                "Pastikan input benar!\nContoh Tasks: 10,20,30"
            )

    # ---------------- BUTTON ----------------
    ttk.Button(
        left,
        text="▶ Jalankan Simulasi",
        command=run_simulation
    ).pack(pady=10)

    window.mainloop()


# =====================================================
# MAIN
# =====================================================
if __name__ == "__main__":
    run_gui()
