# 🌾 Autonomous Agricultural Robot (Simulation)

A **simulation of an autonomous farming robot** that patrols a field grid, detects weeds/pests from simulated sensor readings, and plans an efficient spraying route — visualized interactively.

## 🧠 How It Works
1. Field represented as an N×N grid of cells with simulated crop health/weed presence
2. Robot uses a coverage path-planning algorithm (boustrophedon / "lawnmower" pattern) to visit every cell
3. At each cell, a simulated CV model flags "weed detected" or "healthy crop"
4. A greedy route planner prioritizes weed cells nearest to the robot's current position for targeted spraying (reduces chemical use)
5. Dashboard shows the field heatmap, robot path, and spray efficiency stats

## 🛠️ Tech Stack
- Python, Streamlit (interactive dashboard)
- NumPy for grid simulation
- Matplotlib for path/heatmap visualization
- Pluggable with real CV models (YOLO) and real GPS path planners

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/autonomous-agricultural-robot-sim
cd autonomous-agricultural-robot-sim
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Precision agriculture research & prototyping
- Reducing herbicide/pesticide usage via targeted spraying
- Teaching path-planning + CV integration concepts
- Foundation for real robot deployment (swap simulated sensors for camera + GPS)

## 🎤 Interview Talking Points
1. **Coverage path planning vs random search.** A lawnmower/boustrophedon pattern guarantees full field coverage with minimal overlap — critical for not missing weed patches, unlike random walk exploration.
2. **Targeted spraying reduces waste.** Instead of blanket spraying, the robot only sprays cells flagged with weeds, which in the real world cuts herbicide usage 60-90% — a key sustainability and cost argument.
3. **Simulation-first development.** Building the planning + detection logic in simulation first lets you validate algorithms cheaply before deploying to real hardware, and the same code swaps in real YOLO detections and GPS coordinates later.
