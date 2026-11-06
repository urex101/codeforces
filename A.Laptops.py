#456A
number_of_laptops = int(input(""))
laptop_pricequalityratio = []
for i in range(number_of_laptops):
    laptop_price, laptop_quality = map(int, input("").split())
    laptop_pricequalityratio.append((laptop_quality/laptop_price ))
happy = False
current_ratio = laptop_pricequalityratio[0]
for ratio in laptop_pricequalityratio:
    if ratio != current_ratio:
        print("Happy Alex")
        happy = True
        break
if not happy:
    print("Poor Alex")
