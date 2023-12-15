import os
import zhconv

def to_traditional(filenames, directory, prefix=None):
    for filename in filenames:
        # 讀取文件內容
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # 轉換成繁體中文
        traditional_content = zhconv.convert(content, 'zh-hant')

        # 另存為新檔案
        if prefix:
            new_filename = f"{prefix}{filename}"
        else:
            new_filename = f"tw_{filename}"
        
        with open(os.path.join(directory, new_filename), 'w', encoding='utf-8') as new_file:
            new_file.write(traditional_content)

# 使用範例：
# 假設 'srt' 資料夾在當前工作目錄中
# 轉換 'example.srt' 和 'example2.srt'
if __name__ == '__main__':
    to_traditional(
        [
            '第二單元_TC.srt', 
            '第一單元_TC.srt',
            '第三單元_TC.srt', 
        ]
        , 'srt'
    )
