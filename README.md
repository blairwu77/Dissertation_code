# ✈️ Flight Network Analysis & Visualization with PageRank

This project combines network science and geospatial visualization to analyze global airport connectivity using a custom implementation of the PageRank algorithm and map visualizations. It is implemented in Python and designed with clarity and reproducibility in mind.

---

## 🗂️ Project Structure

```
Dissertation_code-main/
├── data/
│   ├── Comparison_of_results.xlsx      # Result comparison sheet
│   └── final_ranking.csv               # Ranked output (PageRank or metrics)
│
├── draw/
│   ├── draw_routes.py                  # Main visualization script
│   ├── main.py                         # Alternative plotting script
│   └── README.md                       # (Optional) subfolder readme
│
├── Networkx_PageRank/
│   ├── PageRank_refactored.py          # Clean implementation of PageRank algorithm
│   ├── Read_data.py                    # Route & node data preparation script
│   ├── main.py                         # Original minimal PageRank script
│
├── requirements.txt                    # Required Python libraries
└── README.md                           # Project overview and documentation
```

---

## 📌 Project Goals

- 🧠 Analyze airport connectivity via PageRank
- 🌐 Visualize flight routes and airport distributions on a world map
- 📈 Combine geospatial insight with network centrality metrics

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: `Basemap` may require manual installation.
> See: https://matplotlib.org/basemap/users/installing.html

---

### 2. Visualize Global Routes

```bash
python draw/draw_routes.py
```

- Reads airport and route data from CSV
- Projects routes on a shaded-relief world map
- Output image is saved to `/output/`

---

### 3. Run PageRank Analysis

```bash
python Networkx_PageRank/PageRank_refactored.py
```

- Loads nodes (airports) and edges (routes)
- Constructs directed graph using `pygraph`
- Computes PageRank using damping factor and iteration threshold
- Results printed and optionally saved

---

## 📚 Code Modules

| Module | Description |
|--------|-------------|
| `PageRank_refactored.py` | Custom class-based PageRank implementation using Dask |
| `draw_routes.py`         | Map plotting using `Basemap` and `matplotlib` |
| `Read_data.py`           | Helper for pre-processing airport/route datasets |

---

## 🧠 Skills Demonstrated

- Python (modular, functionally organized)
- Network analysis with PageRank
- Visualization with `matplotlib`, `Basemap`
- Data handling using `pandas` and `dask`
- Git and documentation best practices

---

## 📊 Example Output

- World map with all airports and arcs between routes
- PageRank scores printed per airport node

---

## 📃 License

This project is licensed under the MIT License. Feel free to use and adapt.

---

## 🙋‍♀️ Author

Developed as part of a dissertation project. For questions, feel free to reach out via GitHub issues.
