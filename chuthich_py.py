import os
import re

def remove_all_comments(content, ext):
    """Hàm quét và xóa triệt để mọi loại chú thích trong code"""
    
    # 1. Xóa chú thích HTML: <!-- ... --> (có thể trải dài nhiều dòng)
    content = re.sub(r'<!--[\s\S]*?-->', '', content)
    
    # 2. Xóa chú thích CSS / JS nhiều dòng: /* ... */
    content = re.sub(r'/\*[\s\S]*?\*/', '', content)
    
    # 3. Xóa chú thích dạng dòng đơn: // (xử lý cả trường hợp nằm cuối dòng code như "flex: 1; /* ... */" hoặc "// ...")
    # Đảm bảo không xóa nhầm dấu // trong URL kiểu https://
    content = re.sub(r'(?<![:/])//.*', '', content)
    
    # 4. Tách các dòng, lọc bỏ các dòng trống hoặc chỉ chứa khoảng trắng dư thừa
    cleaned_lines = []
    for line in content.splitlines():
        # Nếu dòng sau khi bỏ comment mà trống rỗng thì bỏ qua luôn
        if line.strip() != '':
            cleaned_lines.append(line)
            
    return '\n'.join(cleaned_lines)

def clean_project_files(target_dir):
    valid_extensions = ['.html', '.htm', '.js', '.css']
    count = 0
    
    for root, _, files in os.walk(target_dir):
        # Bỏ qua thư mục ẩn như .git hoặc node_modules nếu có
        if '.git' in root or 'node_modules' in root:
            continue
            
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in valid_extensions:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    cleaned_content = remove_all_comments(content, ext)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(cleaned_content)
                        
                    print(f"Đã làm sạch triệt để: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Lỗi khi xử lý file {file_path}: {e}")
                    
    print(f"\nHoàn tất! Đã quét và làm sạch tổng cộng {count} file.")

if __name__ == "__main__":
    print("=== TOOL XÓA TRIỆT ĐỂ MỌI CHÚ THÍCH ===")
    path = input("Nhập đường dẫn thư mục dự án (Nhấn Enter luôn nếu để chung thư mục): ").strip()
    
    if not path:
        path = "."
    
    print(f"Đang xử lý thư mục: {os.path.abspath(path)}...\n")
    clean_project_files(path)