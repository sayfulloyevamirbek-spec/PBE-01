from database import history_info

history=history_info()
def add_action(type,product,quantity,price,total=None):
    history.append({
        "type":type,
        "product":product,
        "quantity":quantity,
        "price":price,
        "total":quantity*price
    })

def sell_action(type,product,quantity,price,total=None):
    history.append({
        "type":type,
        "product":product,
        "quantity":quantity,
        "price":price,
        "total":quantity*price
    })