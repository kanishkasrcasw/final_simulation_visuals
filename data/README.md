# 📊 Final Simulation Visuals – Scheduler Project (M4)

This repo contains finalized simulation visuals for the intelligent job scheduling system.

---

## ✅ Visuals Included

### 1. Efficiency Over Time
Shows job execution efficiency across the day.

### 2. Resource Utilization
CPU, Memory, and DB usage plotted with threshold lines:
- CPU threshold: 85%
- Memory threshold: 80%
- DB threshold: 90%

### 3. Average Execution Time
- High Priority API: 120ms  
- Medium Task: 450ms  
- Batch Job: 1500ms  
- Background Sync: 2100ms  

### 4. Job Timeline (Gantt Style)
Visualizes start time and duration of jobs on resources.

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python generate_visuals.py
