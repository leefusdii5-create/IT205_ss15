available_seats = 50
flight_revenue = 0.0

BASE_PRICE = 2000.0
MAX_CAPACITY = 50


def calculate_booking_cost(ticket_quantity, seat_class):
    """
    Calculate total booking cost including airport service fee.

    Parameters:
        ticket_quantity (int): Number of tickets.
        seat_class (int): 1 for Economy, 2 for Business.

    Returns:
        float: Final payment amount including 5% service fee.
    """
    if seat_class == 1:
        ticket_price = BASE_PRICE
    else:
        ticket_price = BASE_PRICE * 1.5

    subtotal = ticket_price * ticket_quantity
    service_fee = subtotal * 0.05

    return subtotal + service_fee


def book_tickets(ticket_quantity, total_cost):
    """
    Process ticket booking and update system data.

    Parameters:
        ticket_quantity (int): Number of tickets.
        total_cost (float): Total booking cost.

    Returns:
        bool: True if booking succeeds, otherwise False.
    """
    global available_seats, flight_revenue

    if ticket_quantity > available_seats:
        return False

    available_seats -= ticket_quantity
    flight_revenue += total_cost

    return True


def cancel_tickets(ticket_quantity):
    """
    Cancel tickets and process refund.

    Parameters:
        ticket_quantity (int): Number of tickets to cancel.

    Returns:
        float: Refund amount.
    """
    global available_seats, flight_revenue

    refund_amount = ticket_quantity * BASE_PRICE * 0.8

    available_seats += ticket_quantity
    flight_revenue -= refund_amount

    return refund_amount


def display_flight_status():
    """
    Display flight status report.

    Report Format:
        - Maximum capacity
        - Booked seats
        - Available seats
        - Current flight revenue

    Returns:
        None
    """
    booked_seats = MAX_CAPACITY - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_CAPACITY}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")


def main():
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("\n1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("==============================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            print("\n--- ĐẶT VÉ MÁY BAY ---")

            try:
                quantity = int(input("Nhập số lượng vé: "))

                if quantity <= 0:
                    print("Số lượng vé không hợp lệ.")
                    continue

                seat_class = int(
                    input("Chọn hạng vé (1: Economy, 2: Business): ")
                )

                if seat_class not in [1, 2]:
                    print("Hạng vé không hợp lệ.")
                    continue

                if quantity > available_seats:
                    print(
                        f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống."
                    )
                    continue

                if seat_class == 1:
                    class_name = "Economy"
                    ticket_price = BASE_PRICE
                else:
                    class_name = "Business"
                    ticket_price = BASE_PRICE * 1.5

                subtotal = ticket_price * quantity
                service_fee = subtotal * 0.05
                total_cost = calculate_booking_cost(
                    quantity, seat_class
                )

                print("-> Xác nhận đặt chỗ:")
                print(
                    f"Số lượng: {quantity} | Hạng: {class_name}"
                )
                print(f"Tạm tính: ${subtotal}")
                print(f"Phí dịch vụ (5%): ${service_fee}")
                print(f"Tổng thanh toán: ${total_cost}")

                if book_tickets(quantity, total_cost):
                    print(
                        f"Đặt vé thành công! Ghế trống còn lại: {available_seats}"
                    )

            except ValueError:
                print("Dữ liệu nhập không hợp lệ.")

        elif choice == "2":
            print("\n--- HỦY VÉ & HOÀN TIỀN ---")

            try:
                quantity = int(
                    input("Nhập số lượng vé muốn hủy: ")
                )

                if quantity <= 0:
                    print("Số lượng vé không hợp lệ.")
                    continue

                if available_seats + quantity > MAX_CAPACITY:
                    print(
                        "Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra."
                    )
                    continue

                refund = cancel_tickets(quantity)

                print(
                    f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund} (80% giá cơ bản)."
                )
                print(
                    f"Ghế trống hiện tại: {available_seats}"
                )

            except ValueError:
                print("Dữ liệu nhập không hợp lệ.")

        elif choice == "3":
            display_flight_status()

        elif choice == "4":
            print(
                "Hệ thống đã đóng. Cảm ơn đã sử dụng SKYBOOKING SYSTEM!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ.")


main()
