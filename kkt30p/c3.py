# Câu 3: Nâng cao - Thống kê lô hàng nhập (3 điểm) 
# Giả sử thủ kho đang kiểm đếm một lô hàng gồm nhiều thùng. Hãy viết chương trình cho phép thủ kho nhập liên tục số lượng sản phẩm của từng thùng vào hệ thống.
# Khai báo các biến cần thiết để lưu trữ Tổng số lượng sản phẩm và Số thùng hàng hợp lệ.
# Sử dụng vòng lặp để cho phép người dùng nhập liên tục số lượng của từng thùng.
# Quy tắc xử lý:
# Nếu nhập vào số âm (< 0): In ra "Số lượng không hợp lệ, bỏ qua thùng này!" (Không cộng dồn).
# Nếu nhập vào số 0: Chương trình hiểu là đã kiểm đếm xong và kết thúc quá trình nhập (Sử dụng lệnh break).
# Nếu nhập vào số dương (> 0): Cộng dồn số lượng sản phẩm và tăng biến đếm số thùng hàng.
# Khi kết thúc vòng lặp, in ra màn hình:
# Tổng số thùng hàng hợp lệ đã đếm.
# Tổng số lượng sản phẩm thu được.

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