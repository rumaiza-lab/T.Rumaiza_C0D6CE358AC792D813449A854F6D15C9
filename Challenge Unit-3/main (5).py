def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
      if products[i] == target_product:
        indices.append(i)
    return indices
products = ["laptop", "mobile", "laptop", "charger", "laptop"]
target_product = "laptop"

print(linear_search_product(products, target_product))
target_product = "mouse"

print(linear_search_product(products, target_product))