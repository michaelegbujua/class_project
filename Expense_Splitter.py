def calculate_total(bill: float, tip_percent: float) -> float:
    return bill + (bill * (tip_percent / 100))


def split_bill(total: float, people: int) -> float:
    if people <= 0:
        raise ValueError("Number of people must be at least 1.")
    return total / people


def display_receipt(bill: float, tip_pct: float, total: float, per_person: float):
    print("\n--- Expense Summary ---")
    print(f"Base Bill:     ${bill:.2f}")
    print(f"Tip ({tip_pct}%):     ${(total - bill):.2f}")
    print(f"Total Bill:    ${total:.2f}")
    print(f"Per Person:    ${per_person:.2f}")
    print("------------------------\n")


def main():
    while True:
        try:
            bill = float(input("Enter bill amount ($): "))
            tip_pct = float(input("Enter tip percentage (e.g., 15): "))
            people = int(input("Enter number of people splitting: "))

            total = calculate_total(bill, tip_pct)
            per_person = split_bill(total, people)
            display_receipt(bill, tip_pct, total, per_person)
            break
        except ValueError as err:
            print(f"Invalid input: {err}. Please try again.\n")


if __name__ == "__main__":
    main()

