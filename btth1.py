inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    """
    Tang so luong hang hoa trong kho bang cach cap nhat bien toan cuc inventory_stock.
    
    Args:
        amount (int): So luong hang hoa muon nhap them.
        
    Returns:
        bool: True neu nhap hang thanh cong, False neu so luong khong hop le.
    """
    global inventory_stock
    if amount <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return False
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")
    return True

def process_sale(quantity):
    global inventory_stock
    if quantity <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return False
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return False
    return True

def calculate_final_price(quantity, price):
    if price <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return None
    
    subtotal = quantity * price
    discount = 0.0
    if subtotal >= 1000:
        discount = subtotal * 0.10
        
    tax = (subtotal - discount) * 0.08
    final_total = (subtotal - discount) + tax
    
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${price:.1f}")
    print(f"Tạm tính: ${subtotal:.1f}")
    print(f"Giảm giá (10%): ${discount:.1f}")
    print(f"Thuế VAT (8%): ${tax:.1f}")
    print(f"Tổng thanh toán: ${final_total:.1f}")
    
    return final_total

def print_report():
    """
    In ra bao cao chi tiet ve trang thai cua kho hang va tong doanh thu hien tai.
    
    Args: None
    Returns: None
    """
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.1f}")

def main():
    global inventory_stock, total_revenue
    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-4): ").strip()
        
        if choice == "1":
            print("\n--- NHẬP HÀNG ---")
            try:
                amount_input = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                add_stock(amount_input)
            except ValueError:
                print("Vui lòng chỉ nhập số nguyên hợp lệ!")
                
        elif choice == "2":
            print("\n--- BÁN HÀNG ---")
            try:
                qty_input = int(input("Nhập số lượng mua: "))
                if process_sale(qty_input):
                    price_input = float(input("Nhập đơn giá ($): "))
                    final_bill = calculate_final_price(qty_input, price_input)
                    if final_bill is not None:
                        inventory_stock -= qty_input
                        total_revenue += final_bill
                        print("Đã bán thành công!")
            except ValueError:
                print("Vui lòng nhập đúng kiểu dữ liệu số!")
                
        elif choice == "3":
            print_report()
            
        elif choice == "4":
            print("\nCảm ơn bạn đã sử dụng hệ thống TechStore!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 4.")

if __name__ == "__main__":
    main()
