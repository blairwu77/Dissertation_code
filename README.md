# ✈️ Flight Route Visualization with Basemap

This project visualizes global flight routes and airport locations on a world map using Python's `matplotlib` and `Basemap`. It demonstrates how to work with geospatial data and produce professional visual outputs.

## 📁 Project Structure

```
Organized_Dissertation_Code/
├── data/                  # Contains input datasets
├── draw/                  # Contains the main visualization script
├── output/                # Output directory for saved maps
├── requirements.txt       # Required Python packages
└── README.md              # Project overview and usage guide
```

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Place the following CSV files in the `data/` folder:
   - `Full_Merge_of_All_Unique_Airports.csv`
   - `DRAW_ROUTES.csv`

2. Run the script:

```bash
python draw/draw_routes.py
```

3. Output will be saved to:

```
output/flight_routes.png
```

## 📌 Features

- Airport scatter plotting.
- Great-circle flight route visualization.
- Clean, reusable code with modular functions.
- Saves publication-quality output images.

## 🧠 Skills Demonstrated

- Geospatial data visualization
- Modular programming
- Clean documentation for GitHub projects
