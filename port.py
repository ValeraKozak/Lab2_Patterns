from typing import TYPE_CHECKING
from i_port import IPort

if TYPE_CHECKING:
    from ship import Ship


class Port(IPort):
    """
    A class representing a port where ships can dock, and containers are stored.

    Attributes:
        port_id (int): The unique identifier for the port.
        latitude (float): The latitude of the port.
        longitude (float): The longitude of the port.
        containers (list): A list of containers currently stored at the port.
        history (list): A list of ships that have docked at the port at any time.
        current_ships (list): A list of ships currently docked at the port.
    """

    def __init__(self, port_id, latitude, longitude):
        """
        Initializes the Port object with a unique ID, latitude, and longitude.

        Args:
            port_id (int): The unique identifier for the port.
            latitude (float): The latitude coordinate of the port.
            longitude (float): The longitude coordinate of the port.
        """
        self.port_id = port_id
        self.latitude = latitude
        self.longitude = longitude
        self.containers = []
        self.history = []
        self.current_ships = []

    def incoming_ship(self, ship: 'Ship'):
        """
        Registers an incoming ship at the port.

        Args:
            ship (Ship): The ship arriving at the port.

        The function adds the ship to the current ships if it's not already there
        and also records it in the port's history if it has never docked here before.
        """
        if ship not in self.current_ships:
            self.current_ships.append(ship)
        if ship not in self.history:
            self.history.append(ship)

    def outgoing_ship(self, ship: 'Ship'):
        """
        Registers an outgoing ship leaving the port.

        Args:
            ship (Ship): The ship departing from the port.

        The function removes the ship from the list of currently docked ships.
        """
        if ship in self.current_ships:
            self.current_ships.remove(ship)

    def get_distance(self, other_port: 'Port') -> float:
        """
        Calculates the distance between the current port and another port.

        Args:
            other_port (Port): The other port to which the distance is calculated.

        Returns:
            float: The distance in kilometers between the current port and the specified other port.

        The function uses the Haversine formula to compute the great-circle distance 
        between two points on the Earth’s surface given their latitude and longitude.
        """
        from math import radians, sin, cos, sqrt, atan2
        R = 6371  # Radius of the Earth in kilometers
        lat1, lon1 = radians(self.latitude), radians(self.longitude)
        lat2, lon2 = radians(other_port.latitude), radians(other_port.longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c  # Distance in kilometers
