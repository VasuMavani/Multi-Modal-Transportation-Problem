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
cost_matrix = distance_df.loc[supply.keys(), demand.keys()].fillna(2000)

# Initialize variables for Least Cost Method
supply_vals = supply.copy()
demand_vals = demand.copy()
allocation = pd.DataFrame(0, index=supply.keys(), columns=demand.keys())

# Least Cost Method
while supply_vals and demand_vals:
    # Find the cell with the minimum cost in the cost matrix
    min_cost_cell = cost_matrix.stack().idxmin()
    i, j = min_cost_cell  # Extract row (source) and column (destination)
    
    # Allocate as much as possible to the minimum cost cell
    alloc = min(supply_vals[i], demand_vals[j])
    allocation.loc[i, j] = alloc
    
    # Update supply and demand
    supply_vals[i] -= alloc
    demand_vals[j] -= alloc
    
    # If supply at i is exhausted, remove it from the supply dictionary and cost matrix
    if supply_vals[i] == 0:
        del supply_vals[i]
        cost_matrix = cost_matrix.drop(i)
    
    # If demand at j is exhausted, remove it from the demand dictionary and cost matrix
    if demand_vals[j] == 0:
        del demand_vals[j]
        cost_matrix = cost_matrix.drop(columns=[j])
    
    # Recalculate the cost matrix after the update
    cost_matrix = cost_matrix.loc[supply_vals.keys(), demand_vals.keys()]

# Calculate total cost
total_cost = (allocation * distance_df.loc[allocation.index, allocation.columns]).sum().sum()
final_cost = 35 * total_cost 

# Print output
print("Initial Basic Feasible Solution (Allocation Matrix):")
print(allocation)
print(f"\nTotal Transportation Cost: {final_cost}")

# Round to 1 decimal place and save
allocation_rounded = allocation.round(0).astype(int)

# Save the rounded allocation matrix to CSV
allocation_rounded.to_csv("Least_Cost_Allocation.csv")