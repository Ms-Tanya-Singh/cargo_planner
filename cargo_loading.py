class Container:
    VALID_CARGO_TYPES = {'FF', 'CG', 'PG', 'RM', 'IE'}

    def __init__(self, size, cargo_type):
        if size not in {1, 2}:
            raise ValueError("Size must be 1 or 2 TEU.")
        if cargo_type.upper() not in self.VALID_CARGO_TYPES:
            raise ValueError(f"Invalid cargo type: {cargo_type}")
        self.size = size
        self.cargo_type = cargo_type.upper()

    def get_size(self):
        return self.size

    def get_cargo_type(self):
        return self.cargo_type


class ContainerShip:
    def __init__(self, max_capacity, max_speed, min_draft, max_draft):
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.min_draft = min_draft
        self.max_draft = max_draft
        self.containers = []

    def get_cargo(self):
        return sum(c.get_size() for c in self.containers)

    def get_draft(self):
        cargo = self.get_cargo()
        return self.min_draft + (cargo / self.max_capacity) * (self.max_draft - self.min_draft)

    def get_speed(self):
        draft = self.get_draft()
        loading_fraction = (draft - self.min_draft) / (self.max_draft - self.min_draft)
        speed_drop = loading_fraction * 0.5 * self.max_speed
        return self.max_speed - speed_drop

    def add_container(self, container):
        if self.get_cargo() + container.get_size() <= self.max_capacity:
            self.containers.append(container)
            return True
        else:
            print("Exceeded ship capacity")
            return False

    def remove_container(self):
        if self.containers:
            return self.containers.pop()
        else:
            print("No containers to remove")
            return None

    def print_ship(self):
        cargo = self.get_cargo()
        draft = self.get_draft()
        speed = self.get_speed()

        print(f"Cargo: {cargo} TEU")
        print(f"Draft: {draft:.2f} meters")
        print(f"Speed: {speed:.2f} knots")
        print("Composition:")

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


class AirplaneCargo:
    def __init__(self, max_weight, max_speed):
        self.max_weight = max_weight
        self.max_speed = max_speed
        self.containers = []

    def get_cargo(self):
        return sum(c.get_size() for c in self.containers)

    def get_speed(self):
        load = self.get_cargo() / self.max_weight
        speed = self.max_speed * (1 - 0.6 * (load ** 1.5))
        return max(speed, 0.3 * self.max_speed)

    def add_container(self, container):
        if self.get_cargo() + container.get_size() <= self.max_weight:
            self.containers.append(container)
            return True
        else:
            print("Exceeded airplane capacity")
            return False

    def remove_container(self):
        if self.containers:
            return self.containers.pop()
        else:
            print("No containers to remove")
            return None

    def print_airplane(self):
        cargo = self.get_cargo()
        speed = self.get_speed()

        print(f"Cargo: {cargo} TEU")
        print(f"Speed: {speed:.2f} knots")
        print("Manifest:")
        row = [c.get_cargo_type() for c in self.containers]
        print(" | ".join(row) if row else "(empty)")


if __name__ == "__main__":
    print("CONTAINER SHIP SIMULATION")
    ship = ContainerShip(max_capacity=20, max_speed=25, min_draft=5, max_draft=15)
    for ct in ['FF', 'CG', 'PG', 'RM', 'IE', 'FF', 'CG', 'PG']:
        ship.add_container(Container(1, ct))
    ship.print_ship()

    print("\nAIRPLANE CARGO SIMULATION")
    plane = AirplaneCargo(max_weight=10, max_speed=600)
    for ct in ['FF', 'CG', 'PG', 'IE', 'FF']:
        plane.add_container(Container(2, ct))
    plane.print_airplane()
