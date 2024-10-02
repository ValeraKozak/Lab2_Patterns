import json
from port import Port
from ship import Ship
from container import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer

def print_port_info(ports):
    """
    Outputs information about the ports, including their containers and the ships docked at each port.

    Args:
        ports (dict): A dictionary of Port objects where the key is the port ID and the value is the Port instance.

    For each port, the function retrieves:
        - Latitude and longitude of the port.
        - Lists of containers categorized by type (basic, heavy, refrigerated, liquid).
        - Ships currently at the port, including details of their fuel and categorized containers on board.

    The output is printed in a structured JSON format for easy readability.
    """
    output = {}
    for port_id, port in ports.items():
        port_info = {
            "lat": round(port.latitude, 2),
            "lon": round(port.longitude, 2),
            "basic_container": [],
            "heavy_container": [],
            "refrigerated_container": [],
            "liquid_container": []
        }

        # Sort containers by type at the port
        for container in port.containers:
            if isinstance(container, BasicContainer):
                port_info["basic_container"].append(container.container_id)
            elif isinstance(container, RefrigeratedContainer):
                port_info["refrigerated_container"].append(container.container_id)
            elif isinstance(container, LiquidContainer):
                port_info["liquid_container"].append(container.container_id)
            elif isinstance(container, HeavyContainer):
                port_info["heavy_container"].append(container.container_id)

        # Sort container IDs in ascending order
        port_info["basic_container"].sort()
        port_info["heavy_container"].sort()
        port_info["refrigerated_container"].sort()
        port_info["liquid_container"].sort()

        # Add information about ships currently docked at the port
        for ship in port.current_ships:
            ship_info = {
                "fuel_left": round(ship.fuel, 2),
                "basic_container": [],
                "heavy_container": [],
                "refrigerated_container": [],
                "liquid_container": []
            }

            # Sort containers on each ship by type
            for container in ship.containers:
                if isinstance(container, BasicContainer):
                    ship_info["basic_container"].append(container.container_id)
                elif isinstance(container, RefrigeratedContainer):
                    ship_info["refrigerated_container"].append(container.container_id)
                elif isinstance(container, LiquidContainer):
                    ship_info["liquid_container"].append(container.container_id)
                elif isinstance(container, HeavyContainer):
                    ship_info["heavy_container"].append(container.container_id)

            # Sort container IDs on ships
            ship_info["basic_container"].sort()
            ship_info["heavy_container"].sort()
            ship_info["refrigerated_container"].sort()
            ship_info["liquid_container"].sort()

            port_info[f"ship_{ship.ship_id}"] = ship_info

        output[f"Port {port_id}"] = port_info

    print(json.dumps(output, indent=4))


def main():
    """
    Main function that orchestrates the reading of input data, creation of port, ship, and container objects, 
    and prints the port information.

    The function:
    - Reads configuration data from 'input.json'.
    - Creates instances of Port, Ship, and Container objects based on the input data.
    - Adds containers to the ports and ships.
    - Calls print_port_info() to output the structured information.

    Handles:
    - FileNotFoundError if 'input.json' is not found.
    - JSONDecodeError if there's an issue with the syntax of the JSON input.
    """
    try:
        # Read configuration from the input JSON file
        with open('input.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Файл 'input.json' не знайдено. Будь ласка, перевірте його наявність.")
        return
    except json.JSONDecodeError:
        print("Помилка в структурі JSON-файлу. Перевірте синтаксис.")
        return

    # Create port objects from the data
    ports = {}
    for port_data in data["ports"]:
        port = Port(port_data["id"], port_data["latitude"], port_data["longitude"])
        ports[port_data["id"]] = port

    # Create ship objects from the data
    ships = {}
    for ship_data in data["ships"]:
        port = ports[ship_data["current_port"]]
        ship = Ship(
            ship_data["id"],
            ship_data["fuel"],
            port,
            ship_data["max_weight"],
            ship_data["max_containers"],
            ship_data["fuel_consumption_per_km"]
        )
        ships[ship_data["id"]] = ship
        port.incoming_ship(ship)

    # Create container objects from the data
    containers = {}
    for container_data in data["containers"]:
        if container_data["type"] == "basic":
            container = BasicContainer(container_data["id"], container_data["weight"])
        elif container_data["type"] == "heavy":
            container = HeavyContainer(container_data["id"], container_data["weight"])
        elif container_data["type"] == "refrigerated":
            container = RefrigeratedContainer(container_data["id"], container_data["weight"])
        elif container_data["type"] == "liquid":
            container = LiquidContainer(container_data["id"], container_data["weight"])
        containers[container_data["id"]] = container

    # For demonstration purposes, add containers to a specific port
    for container in containers.values():
        ports[1].containers.append(container)  # Example: all containers are in port 1

    # Print port and ship information
    print_port_info(ports)


if __name__ == "__main__":
    main()
