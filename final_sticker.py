current_eps = float(input("What is current EPS? "))
growth_rate= float(input("What is growth rate? "))
pe = float(input(("What is historic avg PE? ")))
if pe < 2*growth_rate:
    pass
else:
    pe = 2*growth_rate

future_eps = current_eps*((growth_rate/100 + 1)**10)
future_price = future_eps*pe
sticker_price = future_price/4
MOS = sticker_price/2

print(f"sticker price = {sticker_price} | MOS Price = {MOS}")