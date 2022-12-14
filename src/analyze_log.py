import csv
from src.track_orders import TrackOrders


def get_orders(path_to_file):
    with open(path_to_file, "r") as file:
        file_data = csv.reader(file)
        orders = [*file_data]
    return orders


def create_track(orders):
    tracker_orders = TrackOrders()

    for name, order, day in orders:
        tracker_orders.add_new_order(name, order, day)

    return tracker_orders


def generate_log_file(log_file, path_to_save):
    with open(path_to_save, "w") as file:
        file.write(log_file)


def analyze_log(path_to_file):
    orders = get_orders(path_to_file)

    orders_trackables = create_track(orders)

    maria_most_ordered = orders_trackables.get_most_ordered_dish_per_customer(
        "maria"
    )
    arnaldo_order_hamburguer = (
        orders_trackables.get_order_quantity_per_customer(
            "arnaldo", "hamburguer"
        )
    )
    joao_never_ask = orders_trackables.get_never_ordered_per_customer("joao")
    joao_never_went = orders_trackables.get_days_never_visited_per_customer(
        "joao"
    )

    data_to_save = (
        f"{maria_most_ordered}\n"
        f"{arnaldo_order_hamburguer}\n"
        f"{joao_never_ask}\n"
        f"{joao_never_went}\n"
    )

    generate_log_file(data_to_save, "data/mkt_campaign.txt")
