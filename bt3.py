# 1. Khai báo Input / Output
# * Input: Lựa chọn menu (1-5), mã SP, tên SP, giá bán, số lượng.
#   - Tất cả để dạng chuỗi (str) từ bàn phím để check lỗi trước khi ép kiểu.
# * Output: Khung menu text, danh sách sản phẩm (có STT từ 1) và các câu thông báo.


# 2. Cách xử lý 5 bẫy dữ liệu (Edge Cases)
# * Bẫy 1 (Mã SP dính khoảng trắng/viết thường): Dùng `.strip().upper()` chuẩn hóa.
# * Bẫy 2 (Trùng mã khi thêm): Quét list `for`, trùng thì báo "Mã sản phẩm bị trùng".
# * Bẫy 3 (Sửa/Xóa mã không có): Gán biến tạm `target_product = None` để tìm. 
#   Nếu hết vòng lặp vẫn là `None` thì báo lỗi cập nhật/xoá tương ứng.
# * Bẫy 4 (Giá/SL nhập chữ, số âm, bằng 0): Check `.isdigit()` để loại chữ và số âm. 
#   Sau đó ép kiểu `int()` và check `<= 0` để loại số 0. Sai báo "Giá/Số lượng không hợp lệ".
# * Bẫy 5 (Nhập bậy menu): Dùng `while True` với `match-case`. Nhánh `case _` sẽ bắt 
#   hết lựa chọn sai, báo lỗi và tự động lặp lại hiện menu.
# 3. Luồng xử lý chương trình (Pseudocode)
# Khởi tạo list `product_list` chứa 3 sản phẩm mẫu.
# Vòng lặp while True:
#   In Menu -> Nhập choice.
#   Match choice:
#     Case "1": Nếu list rỗng -> Báo trống. Ngược lại -> Duyệt list và in.
#     Case "2": Nhập liệu -> Chuẩn hóa mã -> Check trống -> Check trùng -> Check số nguyên dương -> Append vào list.
#     Case "3": Nhập mã -> Chuẩn hóa -> Tìm kiếm:
#               + Không thấy -> Báo "Không tìm thấy mã sản phẩm cần cập nhật!".
#               + Thấy -> Nhập thông tin mới -> Check số nguyên dương -> Dùng .update().
#     Case "4": Nhập mã -> Chuẩn hóa -> Tìm kiếm:
#               + Không thấy -> Báo "Không tìm thấy mã sản phẩm cần xoá!".
#               + Thấy -> Dùng .remove() xóa khỏi list.
#     Case "5": In "Thoát chương trình." -> break dừng vòng lặp.
#     Case _  : In '"Lựa chọn không hợp lệ", vui lòng nhập lại!'.

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]
while True:
    print("""===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình""")
    choice = input("Nhập lựa chọn của bạn: ")
    match choice:
        case "1":
            print("Danh sách sản phẩm hiện tại: ")
            if not product_list:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                for i,value in enumerate(product_list):
                    print(f"{i+1}. Mã SP: {value['product_id']} |Tên: {value['product_name']} |Giá: {value['price']} |Số lượng: {value['quantity']}")
        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            if product_id == "":
                print("Mã sản phẩm ko đc trống!")
                continue
            is_duplicate = False
            for p in product_list:
                if p["product_id"] == product_id:
                    is_duplicate = True
                    break
            if is_duplicate:
                print("Mã sản phẩm đã tồn tại!")
                continue
            product_name = input("Nhập tên sản phẩm: ")
            if product_name == "":
                print("Tên sản phẩm ko được trống!")
                continue
            price = input("Nhập giá sản phẩm: ")
            if price == "" or not price.isdigit() or int(price) < 0:
                print("Giá ko đc để trống!")
                continue
            quantity = input("Nhập số lượng: ")
            if quantity == "" or not quantity.isdigit() or int(quantity) < 0:
                print("Số lượng ko hợp lệ!")
                continue
            product_list.append({"product_id":product_id,"product_name":product_name,"price":price,"quantity":quantity})
            print("Thêm sản phẩm thành công")
        case "3":
            product_id_change = input("Nhập mã sản phẩm cần thay đổi: ")
            product_id_change = product_id_change.strip().upper()
            if product_id_change == "":
                print("Mã sản phẩm ko đc để trống!")
                continue
            found_product = False
            for i,value in enumerate(product_list):
                if value["product_id"] == product_id_change:
                    found_product = True
                    break
            if found_product:
                product_name_change = input("Nhập tên sản phẩm: ")
                if product_name_change == "":
                    print("Tên sản phẩm ko đc để trống!")
                    continue
                product_price_change = input("Nhập giá sản phẩm: ")
                if product_price_change == "" or not product_price_change.isdigit() or int(product_price_change) < 0:
                    print("Giá ko hợp lệ!")
                    continue
                product_quantity_change = input("Nhập số lượng: ")
                if product_quantity_change == "" or not product_quantity_change.isdigit() or int(product_quantity_change) < 0:
                    print("Số lượng ko hợp lệ!")
                    continue
                product_list[i].update({
                    "product_name": product_name_change,
                    "price": int(product_price_change),
                    "quantity": int(product_quantity_change)
                })
                print("Cập nhật sản phẩm thành công")
            else:
                print("Không tìm thấy mã sản phẩm cần cập nhật!")
        case "4":
            product_id_delete = input("Nhập mã id cần xóa: ").strip().upper()
            if product_id_delete == "":
                print("Mã sản phẩm ko đc trống!")
                continue
            found_product = False
            for i,value in enumerate(product_list):
                if value["product_id"] == product_id_delete:
                    found_product = True
                    break
            
            if not found_product:
                print("Không tìm thấy mã sản phẩm cần xóa!")
            else:
                product_list.pop(i)
                print("Xóa sản phẩm thành công!")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn ko hợp lệ!Vui lòng nhập lại")

