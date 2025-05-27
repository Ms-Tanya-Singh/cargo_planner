# Cargo Planner

Presented here is a Python simulation of cargo loading behavior for two transportation systems:

1. **Container Ship** – models cargo stacking, draft, and linear speed reduction.  
2. **Cargo Airplane** – models cargo weight and speed decay using a physics-inspired function.

The simulation uses object-oriented design to represent containers and their effect on transport performance.

---

## Features

### Container System

- Validated cargo types:
  - FF: Frozen Food  
  - CG: Consumer Goods  
  - PG: Processed Goods  
  - RM: Raw Materials  
  - IE: Industrial Equipment  
- Container sizes limited to 1 or 2 TEU (Twenty-foot Equivalent Units)

### Ship Simulation

- Calculates draft as a linear function of cargo volume  
- Speed decreases proportionally with draft  
- Displays container layout in a 4-row, bottom-up stacked grid

### Airplane Simulation

- Speed reduction modeled using an inverse square-root function of cargo weight  
- Reflects physical performance loss with increasing load  
- Minimum operating speed enforced (40% of maximum)  
- Cargo displayed in a single-row manifest

---

## Getting Started

### Requirements

- Python 3.x

### To Run the Simulation

Run this in your terminal:

python cargo_planner.py

---

## Example Output

CONTAINER SHIP SIMULATION  
Cargo: 8 TEU  
Draft: 9.00 meters  
Speed: 18.75 knots  
Composition:  
PG PG  
CG CG  
FF IE  
RM FF  

AIRPLANE CARGO SIMULATION  
Cargo: 10 TEU  
Speed: 258.20 knots  
Manifest:  
FF | CG | PG | IE | FF

---

## File Structure

cargo_planner/  
├── cargo_planner.py   - Main simulation code  
└── README.md          - Documentation

---

## License

This project is provided for educational and academic use. You may adapt and reuse it with attribution.

