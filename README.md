# Multi-Modal-Transportation-Problem
# Transportation Optimization Project

This repository contains two implementations (AMPL and Python) for solving a **balanced transportation problem**, aimed at minimizing total transportation cost between supply cities and ports. The project demonstrates multiple solution techniques including North-West Corner, Least Cost, Vogel's Approximation Method (VAM), Stepping Stone, and MODI method.

---

## 📁 Folder Structure

### 1. AMPL Folder

This folder contains all the necessary files to define, solve, and analyze the transportation model using **AMPL**.

- **`Data.csv`**  
  CSV file showing the distances between ports and supply cities.

- **`Port_city.dat`**  
  Data initialization file for AMPL with supply, demand, and distance data.

- **`Port_city.mod`**  
  Main AMPL model file containing variables, objective function, and constraints.

- **`Port_city.run`**  
  AMPL run script to load the model, data, and solve the problem.

- **`Supply Demand Data.xlsx`**  
  Excel sheet containing city-wise supply and demand values.

- **`Full_flow.csv`**  
  Output file showing the optimal transportation plan from ports to cities.

---

### 2. Python Folder

This folder contains Python scripts and notebooks implementing classical transportation algorithms for finding both **initial feasible** and **optimal solutions**.

#### Input Files:
- **`Data.csv`**  
  Same as in AMPL – distance between ports and supply cities.

- **`Supply Demand Data.xlsx`**  
  Excel sheet containing city-wise supply and demand data.

#### Python Implementations:

- **Initial Feasible Solution Methods:**
  - `North West Corner.py` – Implements the North-West Corner method.
  - `Least Cost Method.py` – Implements the Least Cost method.
  - `VAM.py` – Implements Vogel’s Approximation Method (VAM).

- **Optimal Solution Methods:**
  - `Stepping Stone And Modi Method.ipynb` – Jupyter notebook implementing both Stepping Stone and MODI methods for optimization.

#### Output Files:
- `North_West_Allocation.csv` – Allocation matrix using North-West Corner method.
- `Least_Cost_Allocation.csv` – Allocation matrix using Least Cost method.
- `VAM_Allocation.csv` – Allocation matrix using VAM method.
- `Stepping_Stone_Allocation.csv` – Optimal allocation from Stepping Stone method.
- `MODI_Allocation.csv` – Optimal allocation from MODI method.

---

## 🔍 Objective

The objective of this project is to:
- Minimize transportation cost while meeting supply and demand constraints.
- Compare classical transportation algorithms (MODI, Stepping Stone) with LP-based solutions (AMPL Simplex).
- Demonstrate the implementation of these algorithms in both modeling and programming environments.

---

## 💰 Cost Comparison of Methods

| Method                  | Total Cost (Rs.)     |  
|-------------------------|----------------------|
| North-West Corner       | ₹8,27,25,365.5        |
| Least Cost Method       | ₹4,89,90,220.0        |
| VAM's Approximation     | ₹4,99,56,485.0        |
| Stepping Stone          | ₹4,86,84,781.5        | 
| MODI Method             | ₹4,99,56,485.0        |
| AMPL (Simplex)          | ₹4,65,84,800.0        |

---

## 🛠️ Technologies Used

- **AMPL** – For linear modeling and optimization using the Simplex method.
- **Python** – For implementing algorithmic solutions step-by-step.
- **Pandas, NumPy** – For data handling in Python.
- **Jupyter Notebook** – For interactive execution and explanation of MODI and Stepping Stone methods.

---
