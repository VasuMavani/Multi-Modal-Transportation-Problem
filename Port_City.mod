# Declare sets and parameters
set PORTS;
set CITIES;

param supply {PORTS} >= 0;  # Supply values for ports
param demand {CITIES} >= 0;  # Demand values for cities

param distance {PORTS,CITIES} >= 0 default 2000;  # Handle missing values

param unit_cost = 35;  # Rs/km

# Decision variable: Flow (how much goods are transported from port to city)
var Flow {PORTS, CITIES} >= 0;

# Objective: Minimize transportation cost
minimize Total_Cost:
    sum {p in PORTS, c in CITIES} 35 * distance[p, c] * Flow[p, c];

# Constraints
subject to Supply_Constraint {p in PORTS}:
    sum {c in CITIES} Flow[p, c] <= supply[p];  # Supply constraint

subject to Demand_Constraint {c in CITIES}:
    sum {p in PORTS} Flow[p, c] >= demand[c];  # Demand constraint
