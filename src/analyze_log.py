import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        with open(path_to_file, "r") as f:
            reader = csv.reader(f)
            data = [row for row in reader]
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    customers = set()
    meals = set()
    days = set()
    maria_meals = dict()
    arnaldo_hamburguer = dict()
    joao_meals = set()
    joao_days = set()

    for entry in data:
        customer, meal, day = entry
        customers.add(customer)
        meals.add(meal)
        days.add(day)
        _collect_data(
            entry, maria_meals, arnaldo_hamburguer, joao_meals, joao_days
        )
    maria_most_common_meal = max(maria_meals, key=maria_meals.get)

    joao_never_had_meals = meals - joao_meals
    joao_never_visited_days = days - joao_days

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(f"{maria_most_common_meal}\n")
        f.write(f"{arnaldo_hamburguer[meal]}\n")
        f.write(f"{joao_never_had_meals}\n")
        f.write(f"{joao_never_visited_days}\n")


def _collect_data(
    entry, maria_meals, arnaldo_hamburguer, joao_meals, joao_days
):
    customer, meal, day = entry
    if customer == "maria":
        if meal in maria_meals:
            maria_meals[meal] += 1
        else:
            maria_meals[meal] = 1
    if customer == "arnaldo" and meal == "hamburguer":
        arnaldo_is_a_lone_wolf(meal, arnaldo_hamburguer)
    if customer == "joao":
        joao_meals.add(meal)
        joao_days.add(day)


def arnaldo_is_a_lone_wolf(meal, arnaldo_hamburguer):
    if meal in arnaldo_hamburguer:
        arnaldo_hamburguer[meal] += 1
    else:
        arnaldo_hamburguer[meal] = 1
