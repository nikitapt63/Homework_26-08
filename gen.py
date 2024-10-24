from random import randint


def gen_house_list() -> list[dict]:
    house_list = []
    for _ in range(30):
        house = {"price": f"{randint(10_000, 200_000)}$",
                 "square": f"{randint(30, 100)}m2"}
        house_list.append(house)
    return house_list


def gen_customer() -> dict:
    customer = {"account": f"{randint(10_000, 200_000)}$",
                "full_name": "Walter White"}
    return customer