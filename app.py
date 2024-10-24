from gen import gen_customer, gen_house_list
from main import get_recs


def app():
    global res
    try:
        c = gen_customer()
        h = gen_house_list()
        res = get_recs(house_list=h, customer=c)
    except Exception:
        return ValueError("Что-то не так.")
    else:
        return res



print(app())