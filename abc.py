import os

# Đường dẫn script cần thêm vào trước thẻ </body>
script_tag = '    <script src="js/animation.js"></script>\n'

def add_animation_script():
    # Lấy danh sách tất cả các file trong thư mục hiện tại
    files = os.listdir('.')
    html_files = [f for f in files if f.endswith('.html')]
    
    if not html_files:
        print("Không tìm thấy file HTML nào trong thư mục này!")
        return

    count = 0
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Kiểm tra xem file đã có script này chưa để tránh chèn trùng lặp
        if 'js/animation.js' in content:
            print(link := f"[Bỏ qua] File {filename} đã có sẵn script.")
            continue
            
        # Tìm thẻ đóng </body> và chèn script vào ngay trước đó
        if '</body>' in content:
            new_content = content.replace('</body>', f'{script_tag}</body>')
            
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"[Thành công] Đã thêm script vào: {filename}")
            count += 1
        else:
            print(f"[Cảnh báo] File {filename} không tìm thấy thẻ </body>.")

    print(f"\nHoàn tất! Đã cập nhật thành công {count} file HTML.")

if __name__ == "__main__":
    add_animation_script()