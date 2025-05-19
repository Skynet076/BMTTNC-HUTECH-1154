import math

# Nhập bán kính từ người dùng
ban_kinh = float(input("Nhập bán kính của hình tròn: "))

# Tính diện tích của hình tròn
dien_tich = math.pi * (ban_kinh ** 2)

# In diện tích của hình tròn ra màn hình
print(f"Diện tích của hình tròn là: {dien_tich:.2f}")
