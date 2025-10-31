# ### 13. Hàm & Đối số (Arguments)

# Viết một hàm `greet(name, age)` in ra:

# ```
# Xin chào {name}, bạn {age} tuổi.
# ```

# Sau đó gọi hàm với một vài tên và tuổi khác nhau.

def greet(name, age):
    print(f"Xin chào {name}, bạn {age} tuổi.")

greet("Linh", 18)
greet("Hân", 20)