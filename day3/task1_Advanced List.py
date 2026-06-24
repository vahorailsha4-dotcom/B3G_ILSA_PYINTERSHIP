price=[100,200,300,400,500,600,700,800,900,1000]
avg_price=sum(price)/len(price)
above_price=[p1 for p1 in price if p1>avg_price]

print("List of prices:",price)
print("Average price:",avg_price)
print("above prices are:",above_price)