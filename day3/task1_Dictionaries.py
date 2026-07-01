products={"pen": 8,"pencil": 15,"notebook": 40,"bag": 550,"scale": 10}
exp_products={product:price 
        for product,price in products.items() if price>100}
print(exp_products)