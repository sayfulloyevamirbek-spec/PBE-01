from database import default_database_info, finance_info, sell_product_database_info
from historiy_section import sell_action
from decarators import log_decarator

default_database=default_database_info()
sell_product_database=sell_product_database_info()
finance=finance_info()



@log_decarator
def sell_product(product_family,product_name,quantity,price):
    if product_family in default_database.keys() and product_name in default_database[product_family].keys():
        if default_database[product_family][product_name]["quantity"]>=quantity and quantity>0:
            default_database[product_family][product_name]["quantity"]-=quantity
            default_database[product_family][product_name]["sold"]+=quantity
            finance["income"]+=quantity*price
            finance["profit"]=finance["income"]-finance["expense"]
            if product_family not in sell_product_database:
                sell_product_database[product_family] = {}
            sell_product_database[product_family][product_name] = {
                "quantity":quantity,
                "price":price,
                "total":quantity*price
            }
            sell_action("sell", product_name, quantity, price)
        else:
            print("mahsulot miqdiori xato kiritildi")
    else:
        print("mahsulot mavjud emas")
    
        

            



      
