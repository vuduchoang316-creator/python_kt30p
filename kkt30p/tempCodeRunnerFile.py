box = 0 
product = 0 

while True:

    input_product = int(input("Nhập số lượng sản phẩm: "))
    if input_product == 0: 
        print("Thoát")
        break
    elif input_product < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này!")
        continue 
    else:
        product += input_product
        box += 1 
    
print(f"Tổng sổ thùng: {box}")
print(f"Tổng số lượng hàng: {product}")