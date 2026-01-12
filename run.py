from cli.main import start
from core.scanner import FileScanner

if __name__ == "__main__":
    start()

scanner = FileScanner()
#scanner.scan_path("C:/Users") 
scanner.scan_path("C:/test_files") # teste com pasta pequena
print(scanner.summary())
