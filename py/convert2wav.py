from pathlib import Path
from pydub import AudioSegment

def convert_to_wav(source_folder, target_folder):
    source_folder = Path(source_folder)
    target_folder = Path(target_folder)
    target_folder.mkdir(parents=True, exist_ok=True)

    for audio_file in source_folder.glob('*.*'):
        if audio_file.suffix == file_suffix:
            sound = AudioSegment.from_file(audio_file)
            target_path = target_folder / f'{audio_file.stem}.wav'
            sound.export(target_path, format='wav')
            print(f'Converted {audio_file.name} to WAV format.')

# 使用範例
source_folder = '.'
target_folder = '.'
# TODO: Support all audio formats
file_suffix = '.mkv'
convert_to_wav(source_folder, target_folder)
