def process_order(order):
    try:
        print("Item:",order["item"])
        print("price:",order["price"])
    except KeyError as e:
        print("Error:Missing Key--{e}")
    else:
        print("Order processed successfully")
    finally:
        print("Processing complete")
o1={"item":"Mobile","price":1000000}
o2={"item":"Earbuds","price":700}
process_order(o1)
process_order(o2)