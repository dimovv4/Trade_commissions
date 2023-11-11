city = input()
sales = float(input())
total_commissions = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        total_commissions = (sales * 5) / 100
    elif 500 < sales <= 1000:
        total_commissions = (sales * 7) / 100
    elif 1000 < sales <= 10000:
        total_commissions = (sales * 8) / 100
    elif sales > 10000:
        total_commissions = (sales * 12) / 100
elif city == "Varna":
    if 0 <= sales <= 500:
        total_commissions = (sales * 4.5) / 100
    elif 500 < sales <= 1000:
        total_commissions = (sales * 7.5) / 100
    elif 1000 < sales <= 10000:
        total_commissions = (sales * 10) / 100
    elif sales > 10000:
        total_commissions = (sales * 13) / 100
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        total_commissions = (sales * 5.5) / 100
    elif 500 < sales <= 1000:
        total_commissions = (sales * 8) / 100
    elif 1000 < sales <= 10000:
        total_commissions = (sales * 12) / 100
    elif sales > 10000:
        total_commissions = (sales * 14.5) / 100
if total_commissions > 0:
    print(f"{total_commissions:.2f}")
else:
    print("error")
