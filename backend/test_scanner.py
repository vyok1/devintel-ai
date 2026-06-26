from app.utils.code_scanner import CodeScanner

scanner = CodeScanner()

issues = scanner.scan_file("sample_bad_code.py")

print(issues)