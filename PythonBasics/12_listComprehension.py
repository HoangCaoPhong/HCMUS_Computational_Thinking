# ### 12. List Comprehension

# Cho list: `[1,2,3,4,5,6,7,8,9,10]`.

# Sử dụng list comprehension để tạo một list mới chứa các bình phương (square) của các số chẵn từ list trên.

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = [x * x for x in list1 if x % 2 == 0]

print(list2)

