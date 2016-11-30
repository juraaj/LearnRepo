import concreteProduct
import license
import product


#second level branch edit
p = concreteProduct.ConcreteProduct()
#cp2 = concreteProduct.ConcreteProduct()

print()
print(product.Product.static_attr)
print(cp.static_attr)

cp.static_attr = "aaaaaaa"
print()
print(product.Product.static_attr)
print(cp.static_attr)

product.Product.static_attr = "bbbbokokokokokokbbb"
print()
print(product.Product.static_attr)
print(cp.static_attr)



