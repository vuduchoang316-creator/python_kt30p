# Câu 1: Khởi động - Tính tiền thanh toán (3 điểm) 
# Viết chương trình tính tiền mua hàng cho khách.
# Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
# Tính Tổng tiền = Đơn giá * Số lượng.
# Áp dụng logic khuyến mãi:
# Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
# Nếu Tổng tiền < 1.000.000, không giảm giá.
# In ra màn hình số tiền cuối cùng khách phải thanh toán.

price = int(input("Nhập đơn giá của sản phẩm: "))
stock = int(input("Số lượng sản phẩm cần mua :  "))
total = price * stock
if total >= 1000000:
    total = total*0.9
else:
    total 

print(f"Tổng tiền: {total}")