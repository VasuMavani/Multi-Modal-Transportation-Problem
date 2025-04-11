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

# Initialize variables for VAM
supply_vals = supply.copy()
demand_vals = demand.copy()
allocation = pd.DataFrame(0, index=supply.keys(), columns=demand.keys())

# Function to calculate penalties
def calculate_penalties(matrix, axis=0):
    """
    Calculate penalties for rows (axis=0) or columns (axis=1).
    """
    if axis == 0:  # Row-wise
        penalties = []
        for row in matrix.iterrows():
            row_data = row[1].sort_values()
            penalties.append(row_data.iloc[1] - row_data.iloc[0] if len(row_data) > 1 else 0)
        return penalties
    else:  # Column-wise
        penalties = []
        for col in matrix.columns:
            col_data = matrix[col].sort_values()
            penalties.append(col_data.iloc[1] - col_data.iloc[0] if len(col_data) > 1 else 0)
        return penalties

# Vogel's Approximation Method
while supply_vals and demand_vals:
    # Calculate penalties for both rows and columns
    row_penalties = calculate_penalties(cost_matrix, axis=0)
    col_penalties = calculate_penalties(cost_matrix, axis=1)
    
    # Find the highest penalty
    max_penalty_row = np.argmax(row_penalties)
    max_penalty_col = np.argmax(col_penalties)
    
    # If the row penalty is higher, we select the row, else select the column
    if row_penalties[max_penalty_row] > col_penalties[max_penalty_col]:
        i = cost_matrix.index[max_penalty_row]
        j = cost_matrix.loc[i].idxmin()  # Select the minimum cost in the row
    else:
        j = cost_matrix.columns[max_penalty_col]
        i = cost_matrix[j].idxmin()  # Select the minimum cost in the column
    
    # Allocate as much as possible to the selected cell
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

# Print output
print("Initial Basic Feasible Solution (Allocation Matrix):")
print(allocation)
print(f"\nTotal Transportation Cost: {35 * total_cost}")

# Round to integer and save
allocation_rounded = allocation.round(0).astype(int)

# Save the rounded allocation matrix to CSV
allocation_rounded.to_csv("VAM_Allocation.csv")
