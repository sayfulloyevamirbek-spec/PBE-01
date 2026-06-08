from database import default_database_info, finance_info, add_product_database_info
from historiy_section import add_action
from decarators import log_decarator





default_database=default_database_info()
add_product_database=add_product_database_info()
finance=finance_info()

@log_decarator
def add_product(product_family, product_name, quantity, buy_price, sell_price, unit):
    
    if product_family not in default_database.keys():
        default_database[product_family]={
            product_name:{
                "quantity":quantity,
                "buy_price":buy_price,
                "sell_price":sell_price,
                "sold":0,
                "unit":unit
            
            }
        }
        
        add_product_database[product_family]={
            product_name:{
                "quantity":quantity,
                "buy_price":buy_price,
                "sell_price":sell_price,
                "unit":unit
            
            }
        }
        add_action("buy", product_name, quantity, buy_price)
    #agar product family mvjud bo'lib name mavjud bo'lmas
    elif product_name not in default_database[product_family].keys():
        default_database[product_family][product_name]={
            "quantity":quantity,
            "buy_price":buy_price,
            "sell_price":sell_price,
            "sold":0,
            "unit":unit
        }
        add_product_database[product_family][product_name]={
            "quantity":quantity,
            "buy_price":buy_price,
            "sell_price":sell_price,
            "unit":unit
        }
        add_action("buy", product_name, quantity, buy_price)
    #agar name va family mavjud bo'lsa 
    else:
        default_database[product_family][product_name]["quantity"]+=quantity
        add_action("buy", product_name, quantity, buy_price)

        