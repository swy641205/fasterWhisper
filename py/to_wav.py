from pathlib import Path
from pydub import AudioSegment


def convert_to_wav(source_folder, target_folder):
    source_folder = Path(source_folder)
    target_folder = Path(target_folder)
    target_folder.mkdir(parents=True, exist_ok=True)

    # 想要匹配的擴展名列表
    extensions = ['*.mkv', '*.mp4', '*.m4a', '*.mov', '*.mp3']

    # 使用列表推導式和 glob 方法來獲取所有匹配的檔案
    files = [file for ext in extensions for file in source_folder.glob(ext)]

    for file in files:
        sound = AudioSegment.from_file(file)
        target_path = target_folder / f'{file.stem}.wav'
        sound.export(target_path, format='wav')
        print(f'Converted {file.name} to WAV format.')


if __name__ == '__main__':
    source_folder = '.'
    target_folder = '.'
    convert_to_wav(source_folder, target_folder)
