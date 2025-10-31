# ### 14. *args và **kwargs

# Viết hàm `describe_person(*args, **kwargs)` mà:

# - `args` nhận một vài sở thích (strings)
# - `*kwargs` nhận các thông tin khác như `name`, `age`, `city`
    
#     Hàm in ra tất cả sở thích và các thông tin từ `kwargs`.

def describe_person(*args, **kwargs):
    print(args)
    print(kwargs)

describe_person("swimming", "play video game", name = "Nguyen Phi Bao", age = 19, city = "HCMC")
