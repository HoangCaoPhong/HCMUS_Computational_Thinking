# ### 7. Set – thao tác và loại bỏ trùng

# Cho list sau: `[1, 2, 2, 3, 4, 4, 5]`.

# - Chuyển list này thành set để loại bỏ các phần tử trùng
# - Thêm số `6` vào set
# - In set ra


thisList = [1, 2, 2, 3, 4, 4, 5]
thisList = set(thisList)

thisList.add(6)

print(thisList)