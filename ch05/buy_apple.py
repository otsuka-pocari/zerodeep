from layer_native import *

apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

#backward
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print("price:", int(price))                 #支払い金額 #220
print("dApple:", dapple)                    #リンゴの値段に関する支払い金額の微分 #2.2
print("dApple_num:", int(dapple_num))       #リンゴの個数に関する支払い金額の微分 #110
print("dTax:", dtax)                        #消費税に関する支払い金額の微分       #200
