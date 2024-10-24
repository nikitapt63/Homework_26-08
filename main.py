def get_recs(house_list: list[dict], customer: dict):
    amount = int(customer['account'][:-1])
    f_houses = []
    print(customer)
    # filtered_houses = list(filter(lambda x: int(x['price'][:-1]) <= amount, house_list))
    for house in house_list:
        house_price = int(house['price'][:-1])
        if house_price <= amount:
            f_houses.append(house)
    f_houses.sort(key=lambda x: int(x['square'][:-2]), reverse=True)
    return f_houses
