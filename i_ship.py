from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from container import Container
    from port import Port

class IShip(ABC):
    """
    An abstract base class that defines the interface for a ship. Any subclass
    implementing this interface must provide methods to sail between ports,
    refuel, and manage containers (loading and unloading).
    """

    @abstractmethod
    def sail_to(self, port: 'Port') -> bool:
        """
        Moves the ship from its current port to a specified destination port.

        Args:
            port (Port): The destination port where the ship will sail to.

        Returns:
            bool: True if the ship has enough fuel and successfully reaches the destination, False otherwise.

        This method must be implemented by any subclass to handle the process of 
        sailing to a new port, including fuel consumption and updating the ship's current port.
        """
        pass

    @abstractmethod
    def refuel(self, fuel_amount: float):
        """
        Adds fuel to the ship's current fuel reserve.

        Args:
            fuel_amount (float): The amount of fuel to add to the ship.

        This method must be implemented by any subclass to handle refueling the ship.
        """
        pass

    @abstractmethod
    def load_container(self, container: 'Container') -> bool:
        """
        Loads a container onto the ship if there is capacity.

        Args:
            container (Container): The container to be loaded onto the ship.

        Returns:
            bool: True if the container is successfully loaded, False otherwise.

        This method must be implemented by any subclass to handle container loading, 
        checking against weight and capacity limits.
        """
        pass

    @abstractmethod
    def unload_container(self, container: 'Container') -> bool:
        """
        Unloads a container from the ship if it is currently loaded.

        Args:
            container (Container): The container to be removed from the ship.

        Returns:
            bool: True if the container is successfully unloaded, False otherwise.

        This method must be implemented by any subclass to handle removing a container 
        from the ship's current load.
        """
        pass
