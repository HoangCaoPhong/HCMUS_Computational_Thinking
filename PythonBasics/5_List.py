# ### List – thao tác cơ bản

# Tạo list chứa tên 5 quốc gia.

# Sau đó:

# - In tên quốc gia thứ 3
# - Thêm một quốc gia mới ở cuối
# - Thay thế quốc gia thứ 2 bằng một quốc gia khác
# - Xóa quốc gia đầu tiên
# - In ra list cuối cùng

countryList = ["China", "Vietnam", "Lao", "Campodia", "Thailand"]

print(countryList[2])

countryList.append("Cuba")

countryList[1] = "USA"

countryList.pop(0)

print(countryList)
