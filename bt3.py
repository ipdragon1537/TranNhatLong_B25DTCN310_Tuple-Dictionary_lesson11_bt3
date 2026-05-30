# 1. Khai báo Input / Output
# * Input: 
#   - Lựa chọn menu (1-5), mã SP, tên SP, giá bán, số lượng.
#   - Tất cả đều nhận vào dạng chuỗi (str) từ bàn phím để dễ xử lý bẫy dữ liệu.
# * Output: 
#   - Giao diện menu văn bản.
#   - Danh sách sản phẩm in theo dòng, định dạng chuẩn (Mã | Tên | Giá | SL).
#   - Các câu thông báo kết quả (Thành công / Thất bại / Lỗi nhập liệu).
# 2. Phương pháp xử lý 5 bẫy dữ liệu (Edge Cases)
# * Bẫy 1 (Mã SP dính khoảng trắng, viết thường):
#   - Dùng `raw_id.strip().upper()` để vừa xóa khoảng trắng 2 đầu, vừa in hoa.
# * Bẫy 2 (Trùng mã khi thêm mới):
#   - Dùng vòng lặp `for` quét qua list, nếu `clean_id == prod['product_id']` 
#     thì chặn lại, báo lỗi "Mã sản phẩm bị trùng".
# * Bẫy 3 (Sửa/Xóa mã không tồn tại):
#   - Tạo biến tạm `found = None`. Quét list nếu thấy thì gán sản phẩm vào biến này.
#   - Hết vòng lặp, nếu `found is None` thì báo lỗi "Không tìm thấy...".
# * Bẫy 4 (Giá/Số lượng nhập chữ, số âm, bằng 0):
#   - Dùng `.isdigit()` check chuỗi nhập vào: nếu chứa chữ hoặc dấu trừ (-) sẽ bị 
#     loại ngay từ đầu. Sau đó ép kiểu `int()` và check `> 0` để loại số 0.
# * Bẫy 5 (Nhập sai menu):
#   - Gom toàn bộ code vào `while True`. Nhánh `else` cuối cùng của bộ điều kiện 
#     sẽ bắt các lựa chọn sai, in lỗi và tự động đẩy về đầu vòng lặp để hiện lại menu.
# 3. Luồng xử lý chương trình (Pseudocode ngắn)
# Khởi tạo list chứa 3 dict sản phẩm mẫu.
# Vòng lặp while True:
#   In Menu -> Nhập choice.
#   Choice == 1: Nếu list rỗng -> Báo trống. Ngược lại -> Duyệt list và in.
#   Choice == 2: Nhập thông tin -> Chuẩn hóa mã -> Check trùng -> Check số nguyên dương -> Thêm vào list.
#   Choice == 3: Nhập mã -> Chuẩn hóa -> Tìm kiếm -> Không thấy báo lỗi / Thấy thì nhập thông tin mới -> Check số nguyên dương -> Ghi đè dữ liệu.
#   Choice == 4: Nhập mã -> Chuẩn hóa -> Tìm kiếm -> Không thấy báo lỗi / Thấy thì remove() khỏi list.
#   Choice == 5: In "Thoát" -> break dừng vòng lặp.
#   Ngược lại: In "Lựa chọn không hợp lệ", lặp lại.

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

