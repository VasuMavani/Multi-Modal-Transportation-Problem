import pandas as pd
import numpy as np

# Load Distance matrix
distance_df = pd.read_csv("Data.csv", index_col=0)

# Define demand
demand = {
    'Guwhathi': 26, 'Srinagar': 32.1, 'Chandigarh': 28.6, 'Delhi': 244.3,
    'Rudrapur': 38, 'NaviMumbai': 287.7, 'Vijaywada': 27.7, 'Varanasi': 32.6,
    'Kharagpur': 21.7, 'Indore': 54.3, 'Belgaum': 43.4, 'Bangalore': 211.7,
    'Rajkot': 38, 'Ahmedabad': 149.3, 'Ludhiana': 43.4, 'Rourkela': 40.2,
    'Hyderabad': 184.8, 'Nagpur': 65.1, 'Coimbatore': 43.4, 'Kolkata': 121.9
}

# Define supply
supply = {
    'Kolkata': 31.6, 'Haldia': 51, 'Paradeep': 239, 'Vizag': 131.1, 'Chennai': 225,
    'Chidambaram': 331.5, 'Kochi': 78.9, 'Mangalore': 98, 'Mormugaon': 63.4,
    'JNPT': 217.6, 'DeenDayal': 267.1, 'Kharagpur': 0, 'Chandigarh': 0, 'Delhi': 0, 'Bangalore': 0
}

# Filter out sources and destinations with zero supply/demand
supply = {k: v for k, v in supply.items() if v > 0}
demand = {k: v for k, v in demand.items() if v > 0}

# Ensure distance_df only includes relevant sources and destinations
cost_matrix = distance_df.loc[supply.keys(), demand.keys()].fillna(0)

# Convert to numpy arrays
supply_vals = supply.copy()
demand_vals = demand.copy()
allocation = pd.DataFrame(0, index=supply.keys(), columns=demand.keys())

# North West Corner Method
supply_idx = list(supply_vals.keys())
demand_idx = list(demand_vals.keys())
i = j = 0

while i < len(supply_idx) and j < len(demand_idx):
    source = supply_idx[i]
    dest = demand_idx[j]
    s = supply_vals[source]
    d = demand_vals[dest]
    alloc = min(s, d)
    
    allocation.loc[source, dest] = alloc
    supply_vals[source] -= alloc
    demand_vals[dest] -= alloc
    
    if supply_vals[source] == 0:
        i += 1
    if demand_vals[dest] == 0:
        j += 1

# Calculate total cost
total_cost = (allocation * cost_matrix).sum().sum()
cost_final = 35 * total_cost
# Print output
print("Initial Basic Feasible Solution (Allocation Matrix):")
print(allocation)
print(f"\nTotal Transportation Cost: {cost_final}")

# Round to 1 decimal place and save
allocation_rounded = allocation.round(1).astype(float)

# Save the rounded allocation matrix to CSV
allocation_rounded.to_csv("North_West_Allocation.csv")