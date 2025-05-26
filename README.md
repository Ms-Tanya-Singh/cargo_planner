# cargo_planner
Presented is my simulation of ship and airplane cargo loading


This Python script simulates cargo loading for two types of vehicles:

1. Container Ship
2. Cargo Airplane

It models how cargo affects ship draft and speed, and how airplane speed is reduced by weight. All containers follow standard size and cargo type conventions.

## Features

- Container system with validated types:
  - FF: Frozen Food
  - CG: Consumer Goods
  - PG: Processed Goods
  - RM: Raw Materials
  - IE: Industrial Equipment
- Ship simulation:
  - Speed decreases linearly as draft increases
  - Draft increases linearly with cargo
  - Displays containers in a 4-row stacked layout
- Airplane simulation:
  - Speed drops exponentially with cargo weight
  - Displays a single-row manifest of cargo

## How to Run

Requirements:
- Python 3.x

To run the program:
1. Open terminal or command prompt.
2. Navigate to the folder containing `cargo_planner.py`.
3. Run the command:

   python cargo_planner.py

## Sample Output

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

## File Structure

cargo_planner/
- cargo_planner.py
- README.md

## License

This project is for educational use. You may adapt and reuse with credit.
