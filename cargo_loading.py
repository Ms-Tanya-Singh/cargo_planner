# Defines a cargo container with size and cargo type
class Container:
    VALID_CARGO_TYPES = {'FF', 'CG', 'PG', 'RM', 'IE'}

    def __init__(self, size, cargo_type):
        # Validate container size (must be 1 or 2 TEU)
        if size not in {1, 2}:
            raise ValueError("Size must be 1 or 2 TEU.")
        # Validate cargo type against allowed types
        if cargo_type.upper() not in self.VALID_CARGO_TYPES:
            raise ValueError(f"Invalid cargo type: {cargo_type}")
        self.size = size
        self.cargo_type = cargo_type.upper()

    def get_size(self):
        return self.size

    def get_cargo_type(self):
        return self.cargo_type


# Models a container ship with cargo, draft, and speed calculation
class ContainerShip:
    def __init__(self, max_capacity, max_speed, min_draft, max_draft):
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.min_draft = min_draft
        self.max_draft = max_draft
        self.containers = []

    def get_cargo(self):
        # Returns the total cargo size on the ship
        return sum(c.get_size() for c in self.containers)

    def get_draft(self):
        # Calculates current draft based on cargo load
        cargo = self.get_cargo()
        return self.min_draft + (cargo / self.max_capacity) * (self.max_draft - self.min_draft)

    def get_speed(self):
        # Calculates ship speed based on draft
        draft = self.get_draft()
        loading_fraction = (draft - self.min_draft) / (self.max_draft - self.min_draft)
        speed_drop = loading_fraction * 0.5 * self.max_speed
        return self.max_speed - speed_drop

    def add_container(self, container):
        # Adds a container if within capacity
        if self.get_cargo() + container.get_size() <= self.max_capacity:
            self.containers.append(container)
            return True
        else:
            print("Exceeded ship capacity")
            return False

    def remove_container(self, container):
        # Removes a specific container if it exists
        if container in self.containers:
            self.containers.remove(container)
            return True
        else:
            print("Container not found")
            return False

    def print_ship(self):
        # Displays ship cargo, draft, speed, and container layout
        cargo = self.get_cargo()
        draft = self.get_draft()
        speed = self.get_speed()

        print(f"Cargo: {cargo} TEU")
        print(f"Draft: {draft:.2f} meters")
        print(f"Speed: {speed:.2f} knots")
        print("Composition:")

        # Setup stacking grid: 4 rows, left-to-right, bottom-up
        stack_height = 4
        cargo_symbols = [c.get_cargo_type() for c in self.containers]
        num_columns = (len(cargo_symbols) + stack_height - 1) // stack_height
        grid = [["  " for _ in range(num_columns)] for _ in range(stack_height)]

        for idx, symbol in enumerate(cargo_symbols):
            col = idx // stack_height
            row = stack_height - 1 - (idx % stack_height)
            grid[row][col] = symbol

        for row in grid:
            print(" ".join(row))


# Models cargo airplane with physics-inspired speed decay
class AirplaneCargo:
    def __init__(self, max_weight, max_speed):
        # max_weight: maximum weight capacity in TEU (or similar unit)
        # max_speed: aircraft’s theoretical maximum speed at minimal load
        self.max_weight = max_weight
        self.max_speed = max_speed
        self.containers = []

    def get_cargo(self):
        # Returns the total cargo weight in TEU units
        return sum(c.get_size() for c in self.containers)

    def get_speed(self):
        # Speed decreases with increasing weight.
        # Formula is based on an inverse square-root relationship:
        # speed = max_speed / sqrt(1 + (load / max_weight))
        # This simulates the effect of reduced thrust-to-weight performance.

        load = self.get_cargo()
        if load == 0:
            return self.max_speed

        weight_fraction = load / self.max_weight
        speed = self.max_speed / (1 + weight_fraction) ** 0.5

        # Ensure speed does not fall below 40% of max speed
        return max(speed, 0.4 * self.max_speed)

    def add_container(self, container):
        # Adds a container if total cargo does not exceed max weight
        if self.get_cargo() + container.get_size() <= self.max_weight:
            self.containers.append(container)
            return True
        else:
            print("Exceeded airplane capacity")
            return False

    def remove_container(self, container):
        # Removes a specific container if it exists
        if container in self.containers:
            self.containers.remove(container)
            return True
        else:
            print("Container not found")
            return False

    def print_airplane(self):
        # Displays current cargo weight and computed speed
        cargo = self.get_cargo()
        speed = self.get_speed()

        print(f"Cargo: {cargo} TEU")
        print(f"Speed: {speed:.2f} knots")
        print("Manifest:")

        row = [c.get_cargo_type() for c in self.containers]
        print(" | ".join(row) if row else "(empty)")


# Main program for demonstration
if __name__ == "__main__":
    print("CONTAINER SHIP SIMULATION")
    ship = ContainerShip(max_capacity=20, max_speed=25, min_draft=5, max_draft=15)

    # Add 8 containers to the ship
    for ct in ['FF', 'CG', 'PG', 'RM', 'IE', 'FF', 'CG', 'PG']:
        ship.add_container(Container(1, ct))

    ship.print_ship()

    print("\nAIRPLANE CARGO SIMULATION")
    plane = AirplaneCargo(max_weight=10, max_speed=600)

    # Add 5 containers to the airplane
    for ct in ['FF', 'CG', 'PG', 'IE', 'FF']:
        plane.add_container(Container(2, ct))

    plane.print_airplane()
