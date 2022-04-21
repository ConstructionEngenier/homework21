from logistica_classes import Store, Shop, Request

if __name__ == "__main__":
    shop = Shop()
    shop.add("печеньки", 10)
    shop.add("собачки", 10)
    shop.add("коробки", 10)
    shop.add("арбузы", 10)
    store = Store()
    store.add("арбузы", 10)
    store.add("собачки", 10)

    is_error = True
    while is_error:
        user_req = input(f'Введите запрос по типу: "Доставить (количество) (товар) из (склад/магазин) в '
                         f'(склад/магазин)"\n')
        user_req_lst = user_req.split(" ")

        if not user_req_lst[1].isnumeric():
            print("Введите количество товара для доставки")
        elif "доставить" not in user_req_lst[0].lower():
            print("Введите доставить в начале запроса")
        elif "магазин" not in user_req_lst[4].lower() and "склад" not in user_req_lst[4].lower():
            print("Введите место отправки")
        elif "магазин" not in user_req_lst[6].lower() and "склад" not in user_req_lst[6].lower():
            print("Введите место отправки")
        else:
            is_error = False
            request = Request(user_req)
            if "магазин" in request.from_:
                print("Доставка возможна только со склада")
            elif "склад" in request.from_:
                if request.product in store.get_item():
                    if request.amount <= store.get_item()[request.product]:
                        print("Нужное количество есть на складе")
                        if sum(shop.get_item().values()) + request.amount <= shop.capacity:
                            print(f"Курьер забрал {request.amount} {request.product} со {request.from_}")
                            store.remove(request.product, request.amount)
                            print(f"Курьер везет {request.amount} {request.product} со {request.from_} в {request.to}")
                            print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
                            shop.add(request.product, request.amount)

                        else:
                            print(f"В {request.to} недостаточно места, попробуйте что то другое")
                    else:
                        print("Не хватает на складе, попробуйте заказать меньше")
                else:
                    print("Данный товар отсутствует на складе")

            if store.get_unique_items_count():
                print("В склад хранится:")
                for key, value in store.items.items():
                    print(value, key)
            else:
                print("В складе ничего нет")

            if shop.get_unique_items_count():
                print("В магазин хранится:")
                for key, value in shop.items.items():
                    print(value, key)
            else:
                print("В магазине ничего нет")