# Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))

# Kiểm tra xem số đó có phải số chẵn hay không
if so % 2 == 0:
    print(f"{so} là số chẵn.")
else:
    print(f"{so} không phải là số chẵn.")
