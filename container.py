class Container:
    """
    A base class representing a container.

    Attributes:
        container_id (int): The unique identifier for the container.
        weight (float): The weight of the container in tons.
    """

    def __init__(self, container_id, weight):
        """
        Initializes the container with a given ID and weight.

        Args:
            container_id (int): The unique identifier for the container.
            weight (float): The weight of the container in tons.
        """
        self.container_id = container_id
        self.weight = weight

    def consumption(self):
        """
        Calculates the fuel consumption for the container.

        Returns:
            float: The fuel consumption based on the weight of the container.
        """
        return self.weight * 2.5  # Basic fuel consumption for a standard container

    def __eq__(self, other):
        """
        Checks equality between two containers based on their ID and weight.

        Args:
            other (Container): Another container object to compare against.

        Returns:
            bool: True if the container ID and weight are the same, False otherwise.
        """
        return (self.container_id == other.container_id) and (self.weight == other.weight)


class BasicContainer(Container):
    """
    A class representing a basic container. Inherits from Container.

    This container type has the same fuel consumption formula as the base class.
    """

    def consumption(self):
        """
        Calculates the fuel consumption for the basic container.

        Returns:
            float: The fuel consumption for the basic container.
        """
        return self.weight * 2.5  # Fuel consumption remains the same as base container


class HeavyContainer(Container):
    """
    A class representing a heavy container. Inherits from Container.

    This container type has a higher fuel consumption than the basic container.
    """

    def consumption(self):
        """
        Calculates the fuel consumption for the heavy container.

        Returns:
            float: The fuel consumption for the heavy container, which is higher due to its weight.
        """
        return self.weight * 3.0  # Higher consumption due to heavy load


class RefrigeratedContainer(HeavyContainer):
    """
    A class representing a refrigerated container. Inherits from HeavyContainer.

    This container type has an even higher fuel consumption due to refrigeration needs.
    """

    def consumption(self):
        """
        Calculates the fuel consumption for the refrigerated container.

        Returns:
            float: The fuel consumption for the refrigerated container, which is higher due to refrigeration equipment.
        """
        return self.weight * 5.0  # Higher consumption due to refrigeration requirements


class LiquidContainer(HeavyContainer):
    """
    A class representing a liquid container. Inherits from HeavyContainer.

    This container type has a different consumption rate compared to heavy and refrigerated containers.
    """

    def consumption(self):
        """
        Calculates the fuel consumption for the liquid container.

        Returns:
            float: The fuel consumption for the liquid container, which is higher due to its contents.
        """
        return self.weight * 4.0  # Higher consumption for transporting liquids
