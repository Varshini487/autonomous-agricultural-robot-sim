import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="🌾 Autonomous Agricultural Robot", layout="wide")
st.title("🌾 Autonomous Agricultural Robot (Simulation)")
st.markdown("Simulates a farm robot patrolling a field, detecting weeds, and planning a targeted spraying route.")

st.sidebar.header("⚙️ Field Settings")
grid_size = st.sidebar.slider("Field Grid Size (N x N)", 5, 15, 8)
weed_density = st.sidebar.slider("Weed Density (%)", 5, 50, 20)
seed = st.sidebar.number_input("Random Seed", value=42)

np.random.seed(seed)
field = (np.random.rand(grid_size, grid_size) < weed_density/100).astype(int)

def boustrophedon_path(n):
    path = []
    for row in range(n):
        cols = range(n) if row % 2 == 0 else range(n-1, -1, -1)
        for col in cols:
            path.append((row, col))
    return path

if st.button("🚜 Run Field Patrol Simulation"):
    path = boustrophedon_path(grid_size)
    weeds_found = [(r, c) for (r, c) in path if field[r, c] == 1]
    sprayed = len(weeds_found)
    total_cells = grid_size * grid_size

    col1, col2, col3 = st.columns(3)
    col1.metric("🌱 Total Cells Scanned", total_cells)
    col2.metric("🚨 Weeds Detected", sprayed)
    col3.metric("💧 Spray Efficiency", f"{(sprayed/total_cells)*100:.1f}% of field targeted")

    fig, ax = plt.subplots(figsize=(6,6))
    ax.imshow(field, cmap="Greens_r", alpha=0.6)
    path_r = [p[0] for p in path]
    path_c = [p[1] for p in path]
    ax.plot(path_c, path_r, color="blue", linewidth=1, alpha=0.5, label="Robot Path")
    if weeds_found:
        wr = [w[0] for w in weeds_found]
        wc = [w[1] for w in weeds_found]
        ax.scatter(wc, wr, color="red", s=80, marker="x", label="Weed Detected / Sprayed")
    ax.set_title("Field Map: Robot Path & Weed Detections")
    ax.legend(loc="upper right")
    ax.invert_yaxis()
    st.pyplot(fig)

    st.markdown("### 📊 Spray Savings vs Blanket Spraying")
    savings_pct = 100 - (sprayed/total_cells)*100
    st.success(f"Targeted spraying covers only {sprayed} of {total_cells} cells — an estimated **{savings_pct:.1f}% reduction** in herbicide use vs spraying the whole field.")

st.markdown("---")
st.caption("Simulated sensors here — swap in a YOLO weed-detection model + real GPS coordinates for physical deployment.")
