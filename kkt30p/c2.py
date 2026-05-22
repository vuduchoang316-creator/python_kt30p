# Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật (4 điểm) 
# Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình.

pass_word = "123456"
# check_pass = False
count = 0
while True:
    input_pass = input("Nhập mật khẩu của bạn: ")
    if input_pass == pass_word:
        print("Đăng nhập thành công!")
        check_pass = True
        break
    else:
       print("Mật khẩu sai, vui lòng nhập lại!")
       count += 1 
    
    if count == 3:
        print("Tài khoản đã bị khóa!")
        break