from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ship import Ship

class IPort(ABC):
    """
    An abstract base class that defines the interface for a port. Any subclass
    implementing this interface must provide implementations for handling ships
    arriving at and departing from the port.
    """

    @abstractmethod
    def incoming_ship(self, ship: 'Ship'):
        """
        Handles the arrival of a ship at the port.

        Args:
            ship (Ship): The ship that is arriving at the port.

        This method must be implemented by any subclass. It is responsible for
        updating the port's state to reflect that the ship has docked.
        """
        pass

    @abstractmethod
    def outgoing_ship(self, ship: 'Ship'):
        """
        Handles the departure of a ship from the port.

        Args:
            ship (Ship): The ship that is leaving the port.

        This method must be implemented by any subclass. It is responsible for
        updating the port's state to reflect that the ship has departed.
        """
        pass
