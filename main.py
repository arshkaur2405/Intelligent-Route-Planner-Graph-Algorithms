import os
from datetime import datetime

from src.graph import Graph
from src.router import Router
from src.visualizer import Visualizer


def load_city_network():

    city = Graph()

    # Nodes
    city.add_node("Airport", 12.9716, 77.5946)
    city.add_node("Tech Park", 12.9785, 77.6408)
    city.add_node("Downtown", 12.9592, 77.5913)
    city.add_node("Metro Station", 12.9423, 77.5684)
    city.add_node("Suburb East", 12.9912, 77.6821)
    city.add_node("Harbor Area", 12.9105, 77.6254)
    city.add_node("Industrial Zone", 12.9012, 77.5212)
    city.add_node("Central Hospital", 12.9644, 77.5344)

    # Roads
    city.add_edge("Airport", "Tech Park", 15, 80)
    city.add_edge("Airport", "Central Hospital", 12.5, 60)

    city.add_edge("Tech Park", "Suburb East", 5.2, 40)
    city.add_edge("Tech Park", "Downtown", 8, 50)

    city.add_edge("Central Hospital", "Downtown", 6.4, 40)
    city.add_edge("Central Hospital", "Industrial Zone", 9.8, 50)

    city.add_edge("Downtown", "Metro Station", 4.5, 35)
    city.add_edge("Downtown", "Harbor Area", 11.2, 60)

    city.add_edge("Metro Station", "Industrial Zone", 5, 40)

    city.add_edge("Harbor Area", "Suburb East", 18.5, 70)
    city.add_edge("Harbor Area", "Industrial Zone", 14, 60)

    return city


def save_route_report(summary):

    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/route_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "INTELLIGENT ROUTE PLANNER REPORT\n"
        )

        file.write("=" * 50 + "\n")

        file.write(
            f"\nGenerated: {datetime.now()}\n\n"
        )

        file.write(
            f"Route: {' -> '.join(summary['path'])}\n"
        )

        file.write(
            f"Distance: {summary['distance']} km\n"
        )

        file.write(
            f"Travel Time: {summary['time']} min\n"
        )

        file.write(
            f"Optimized By: {summary['optimized_by']}\n"
        )

    print(
        "\n[✓] Report saved in outputs/route_report.txt"
    )


def display_locations(city):

    print("\nAVAILABLE LOCATIONS")
    print("-" * 30)

    for node in city.nodes:
        print(node)


def display_city_information(city):

    print("\nROAD NETWORK")
    print("-" * 40)

    for source in city.adjacency_list:

        print(f"\n{source}")

        for neighbor, dist, speed in city.get_neighbors(source):

            print(
                f"  -> {neighbor}"
                f" | Distance={dist} km"
                f" | Speed={speed} km/h"
            )


def show_menu():

    print("\n")
    print("=" * 50)
    print("INTELLIGENT ROUTE PLANNER")
    print("=" * 50)

    print("1. View Locations")
    print("2. View Road Network")
    print("3. BFS Traversal")
    print("4. DFS Traversal")
    print("5. Find Shortest Route")
    print("6. Visualize Graph")
    print("7. Exit")


def main():

    city = load_city_network()

    latest_path = None

    while True:

        show_menu()

        choice = input(
            "\nEnter Choice: "
        ).strip()

        try:

            if choice == "1":

                display_locations(city)

            elif choice == "2":

                display_city_information(city)

            elif choice == "3":

                display_locations(city)

                start = input(
                    "\nStart Node: "
                ).strip()

                end = input(
                    "Destination Node: "
                ).strip()

                path = city.bfs(start, end)

                print("\nBFS Result")
                print(path)

            elif choice == "4":

                display_locations(city)

                start = input(
                    "\nStart Node: "
                ).strip()

                end = input(
                    "Destination Node: "
                ).strip()

                path = city.dfs(start, end)

                print("\nDFS Result")
                print(path)

            elif choice == "5":

                display_locations(city)

                start = input(
                    "\nSource: "
                ).strip()

                end = input(
                    "Destination: "
                ).strip()

                if start not in city.nodes:

                    print(
                        "\nInvalid Source Node"
                    )

                    continue

                if end not in city.nodes:

                    print(
                        "\nInvalid Destination Node"
                    )

                    continue

                print("\nOptimization Mode")
                print("1. Distance")
                print("2. Travel Time")

                mode = input(
                    "Select: "
                ).strip()

                optimize_by = (
                    "time"
                    if mode == "2"
                    else "distance"
                )

                path, cost = Router.shortest_path(
                    city,
                    start,
                    end,
                    optimize_by
                )

                if path is None:

                    print(
                        "\nNo route found!"
                    )

                    continue

                latest_path = path

                summary = Router.route_summary(
                    city,
                    path,
                    optimize_by
                )

                print("\n")
                print("=" * 50)
                print("OPTIMIZED ROUTE")
                print("=" * 50)

                print(
                    "\nRoute:"
                )

                print(
                    " -> ".join(path)
                )

                print(
                    f"\nDistance: "
                    f"{summary['distance']} km"
                )

                print(
                    f"Travel Time: "
                    f"{summary['time']} min"
                )

                print(
                    f"Optimized By: "
                    f"{summary['optimized_by']}"
                )

                save_route_report(
                    summary
                )

            elif choice == "6":

                if latest_path:

                    Visualizer.draw(
                        city,
                        latest_path
                    )

                else:

                    Visualizer.draw(city)

            elif choice == "7":

                print(
                    "\nThank you for using Route Planner."
                )

                break

            else:

                print(
                    "\nInvalid Choice!"
                )

        except Exception as error:

            print(
                f"\n[ERROR]: {error}"
            )


if __name__ == "__main__":
    main()