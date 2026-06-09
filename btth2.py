atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    """
    Display account balance and ATM cash balance.

    Parameters:
        None

    Returns:
        None
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Deposit money into the account and ATM vault.

    Parameters:
        amount (int): Amount of money to deposit.

    Returns:
        bool: True if deposit succeeds.
    """
    global user_account_balance, atm_vault_balance

    user_account_balance += amount
    atm_vault_balance += amount
    return True


def check_withdrawal_rules(amount):
    """
    Check whether a withdrawal request is valid.

    Parameters:
        amount (int): Amount of money requested for withdrawal.

    Returns:
        tuple:
            ("OK", total_deduction, fee) if valid.
            ("INSUFFICIENT_FUNDS", None, None) if account balance is insufficient.
            ("ATM_OUT_OF_CASH", None, None) if ATM lacks enough cash.
    """
    fee = 1100
    total_deduction = amount + fee

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", None, None

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", None, None

    return "OK", total_deduction, fee


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Execute withdrawal transaction.

    Parameters:
        total_deduction (int): Total amount deducted from account.
        amount_to_dispense (int): Cash dispensed to customer.

    Returns:
        None
    """
    global user_account_balance, atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense


def main():
    """
    Main ATM program loop.

    Parameters:
        None

    Returns:
        None
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        if choice == "1":
            display_balances()

        elif choice == "2":
            print("\n--- NẠP TIỀN ---")

            try:
                amount = int(input("Nhập số tiền muốn nạp: "))

                if amount <= 0:
                    print("Số tiền không hợp lệ")
                    continue

                if deposit_money(amount):
                    print(
                        f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND."
                    )

            except ValueError:
                print("Số tiền không hợp lệ")

        elif choice == "3":
            print("\n--- RÚT TIỀN ---")

            try:
                amount = int(input("Nhập số tiền cần rút: "))

                if amount <= 0:
                    print("Số tiền không hợp lệ")
                    continue

                if amount % 50000 != 0:
                    print("Số tiền rút phải là bội số của 50,000")
                    continue

                status, total_deduction, fee = check_withdrawal_rules(amount)

                if status == "INSUFFICIENT_FUNDS":
                    print("Giao dịch thất bại: Số dư tài khoản không đủ.")

                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")

                else:
                    print("Giao dịch đang xử lý...")

                    execute_withdrawal(total_deduction, amount)

                    print(f"Phí giao dịch: {fee:,} VND")
                    print(f"Bạn đã rút thành công {amount:,} VND.")
                    print(
                        f"Số dư tài khoản còn lại: {user_account_balance:,} VND."
                    )

            except ValueError:
                print("Số tiền không hợp lệ")

        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")


main()
