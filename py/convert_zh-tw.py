import os
import zhconv

def convert_files_to_traditional(filenames, directory):
    for filename in filenames:
        # 讀取文件內容
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()

        # 轉換成繁體中文
        traditional_content = zhconv.convert(content, 'zh-hant')

        # 另存為新檔案
        new_filename = f"zh-tw_{filename}"
        with open(os.path.join(directory, new_filename), 'w', encoding='utf-8') as new_file:
            new_file.write(traditional_content)

# 使用範例：
# 假設 'srt' 資料夾在當前工作目錄中
# 轉換 'example.srt' 和 'example2.srt'
if __name__ == '__main__':
    convert_files_to_traditional(
        [
            # 'ftp_tutorial_seq1.srt', 
             'ark_zh-tw_tutorial_seq2.srt'
        ]
        , 'srt'
    )
