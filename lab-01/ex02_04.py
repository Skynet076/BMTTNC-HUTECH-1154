# Tạo danh sách lưu các số chia hết cho 7 nhưng không chia hết cho 5
ket_qua = []

for so in range(2000, 3201):
    if so % 7 == 0 and so % 5 != 0:
        ket_qua.append(str(so))

# In kết quả, các số cách nhau bằng dấu phẩy
print(','.join(ket_qua))
