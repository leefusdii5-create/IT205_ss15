cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n" + "="*50)
    print("          SHOPEE CART MANAGEMENT SYSTEM          ")
    print("="*50)
    print("[1] Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("[2] Thêm sản phẩm mới / Cộng dồn số lượng")
    print("[3] Cập nhật số lượng của một sản phẩm")
    print("[4] Xóa sản phẩm khỏi giỏ hàng")
    print("[5] Thoát chương trình")
    print("="*50)
    choice = int(input("Mời bạn chọn chức năng (1-5): "))
        
    if choice == 1:
        print("\n" + "-"*30 + " CHI TIẾT GIỎ HÀNG " + "-"*30)
        print(f"{'STT':<5} | {'Mã SP':<7} | {'Tên Sản Phẩm':<25} | {'SL':<5} | {'Đơn Giá':<12} | {'Thành Tiền'}")
        print("-"*85)
        
        total_quantity = 0
        total_amount = 0
        
        for index, item in enumerate(cart_items, start=1):
            product_id = item[0]
            product_name = item[1]
            quantity = item[2]
            price = item[3]
            
            subtotal = quantity * price
            total_quantity += quantity
            total_amount += subtotal
            
            print(f"{index:<5} | {product_id:<7} | {product_name:<25} | {quantity:<5} | {price:,.0f}đ{'' :<4} | {subtotal:,.0f}đ")
            
        print("-"*85)
        print(f"⇒ Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
        print(f"⇒ TỔNG TIỀN THANH TOÁN: {total_amount:,.0f}đ")
        print("-" * 85)

    elif choice == 2:
        product_id = input("Nhập mã sản phẩm: ")
        product_name = input("Nhập tên sản phẩm: ")

        quantity = int(input("Nhập số lượng: "))
        price = int(input("Nhập đơn giá: "))

        if quantity <= 0 or price < 0:
            print("Lỗi: Số lượng phải > 0 và đơn giá không được âm.")
            continue

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] += quantity
                found = True
                print(f"\nSản phẩm {product_id} đã tồn tại.")
                print(f"Đã cộng dồn thêm {quantity} sản phẩm.")
                break

        if not found:
            cart_items.append([product_id, product_name, quantity, price])
            print("\nThêm sản phẩm mới thành công!")

        print(f"Tổng số sản phẩm hiện có trong giỏ: {len(cart_items)}")
        
    elif choice == 3:
        check_code_product = input("Nhập mã sản phẩm cần cập nhật số lượng: ")

        isValid = False;

        for index, value in enumerate(cart_items, start = 0):
            if check_code_product == value[0]:
                change_quantity = int(input(f"Nhập số lượng mới cho sản phẩm {value[1]}: "))
                isValid = True;
                if change_quantity > 0:
                    value[2] = change_quantity
                    print(f"Đã cập nhật số lượng mới cho sản phẩm {value[1]}")
                    break;
                else:
                    print("Số lượng sản phẩm mới không hợp lệ!")
                    break;
    
        if isValid == False:
            print("Không tìm thấy sản phẩm cần tìm")
    
    elif choice == 4:
        check_code_product = input("Nhập mã sản phẩm cần xóa: ")

        isValid = False;

        for index, value in enumerate(cart_items, start = 0):
            if check_code_product == value[0]:
                del cart_items[index]
                isValid = True
                print(f"Đã xóa thành công sản phẩm {value[1]}!")

                break;
                
        if isValid == False:
            print("Không tìm thấy sản phẩm cần tìm")
        
    elif choice == 5:
        print("\nThoát chương trình!")
        break
