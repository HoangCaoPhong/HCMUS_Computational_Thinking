# 11. **Singleton class – “DatabaseConnection”**
#     Tạo lớp `DatabaseConnection` đảm bảo chỉ có một instance (singleton).
#     Nếu tạo lần thứ hai, raise Exception.
#     Viết `get_instance()` để lấy instance duy nhất.

class DatabaseConnection:
    __instance = None

    def __init__(self):
        if DatabaseConnection.__instance is not None:
            raise Exception("Only one instance of DB Connection allowed")

        self.status = "connected"
        DatabaseConnection.__instance = self

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = DatabaseConnection()
        return cls.__instance
    
    def querry(self, sql):
        print(f"Executing SQL: {sql}")

db0 = DatabaseConnection()

db1 = DatabaseConnection.get_instance()
print(db1.status)

db1.querry("Sum A -> Z")