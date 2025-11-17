# 10. **Multiple inheritance – “Logger” và “FileWriter”**
    # Tạo lớp `Logger` có phương thức `log(message)`.
    # Tạo lớp `FileWriter` có phương thức `write(text)`.
    # Tạo lớp `LogFileWriter` kế thừa cả hai và thực hiện `log` thông qua `write`. Tạo instance và thử.

class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class FileWriter:
    def write(self, text):
        print(f"Writing to file: {text}")

class LogFileWriter(Logger, FileWriter):
    def log(self, message):
        self.write(f"[LOG]: {message}")


lfw = LogFileWriter()
lfw.log("System started")
lfw.write("Saving configuration...")



