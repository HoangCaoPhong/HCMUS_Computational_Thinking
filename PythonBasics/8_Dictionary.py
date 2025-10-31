### 8. Dictionary – thao tác truy cập & sửa

# Tạo dictionary biểu diễn thông tin một sinh viên:

# ```python
# student = {
#   "name": "An",
#   "age": 21,
#   "major": "Computer Science"
# }

# ```

# Sau đó:

# - In ra tên (name)
# - Sửa tuổi thành 22
# - Thêm khóa `"GPA"` với giá trị `3.5`
# - Xóa khóa `"major"`
# - In dictionary cuối cùng

student = {
   "name": "An",
   "age": 21,
   "major": "Computer Science"
}
print(student["name"])
student["age"] = 22
student["GPA"] = 3.5
del student["major"]

print(student)
