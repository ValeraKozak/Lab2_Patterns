from typing import TYPE_CHECKING
from i_ship import IShip

if TYPE_CHECKING:
    from container import Container
    from port import Port

class Ship(IShip):
    """
    A class representing a ship that can sail between ports, carry containers, and manage fuel consumption.

    Attributes:
        ship_id (int): The unique identifier for the ship.
        fuel (float): The current amount of fuel in the ship.
        current_port (Port): The current port where the ship is docked.
        max_weight (float): The maximum weight the ship can carry.
        max_containers (int): The maximum number of containers the ship can hold.
        fuel_consumption_per_km (float): The fuel consumed by the ship per kilometer.
        containers (list): A list of containers currently loaded on the ship.
    """

    def __init__(self, ship_id, fuel, current_port, max_weight, max_containers, fuel_consumption_per_km):
        """
        Initializes the Ship object with the provided parameters.

        Args:
            ship_id (int): The unique identifier for the ship.
            fuel (float): The initial amount of fuel in the ship.
            current_port (Port): The port where the ship starts.
            max_weight (float): The maximum weight the ship can carry.
            max_containers (int): The maximum number of containers the ship can hold.
            fuel_consumption_per_km (float): The fuel consumption rate per kilometer.
        """
        self.ship_id = ship_id
        self.fuel = fuel
        self.current_port = current_port
        self.max_weight = max_weight
        self.max_containers = max_containers
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.containers = []

    def sail_to(self, destination_port: 'Port') -> bool:
        """
        Attempts to sail the ship to a new destination port.

        Args:
            destination_port (Port): The port to which the ship is sailing.

        Returns:
            bool: True if the ship has enough fuel and successfully sails to the destination, False otherwise.

        The function calculates the distance between the current port and the destination port,
        checks if there is enough fuel for the journey, and updates the ship's location and fuel levels accordingly.
        """
        distance = self.current_port.get_distance(destination_port)
        required_fuel = distance * self.fuel_consumption_per_km
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            self.current_port.outgoing_ship(self)
            destination_port.incoming_ship(self)
            self.current_port = destination_port
            return True
        return False

    def refuel(self, fuel_amount: float):
        """
        Refuels the ship by a specified amount.

        Args:
            fuel_amount (float): The amount of fuel to add to the ship's current fuel level.
        """
        self.fuel += fuel_amount

    def load_container(self, container: 'Container') -> bool:
        """
        Loads a container onto the ship if the ship has enough capacity.

        Args:
            container (Container): The container to load onto the ship.

        Returns:
            bool: True if the container was successfully loaded, False if the ship has reached its container capacity.
        """
        if len(self.containers) < self.max_containers:
            self.containers.append(container)
            return True
        return False

    def unload_container(self, container: 'Container') -> bool:
        """
        Unloads a container from the ship if it is currently loaded.

        Args:
            container (Container): The container to unload from the ship.

        Returns:
            bool: True if the container was successfully unloaded, False if the container is not on the ship.
        """
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False
