from pathlib import Path
from tqdm import tqdm
from faster_whisper import WhisperModel
from translate_srt import to_traditional

# stander srt
TIMESTAMP = '{h:02}:{m:02}:{s:02},{ms:03}'
CAPTION = '{num}\n{start_time} --> {end_time}\n{transcript}\n\n'
# custom srt
# TIMESTAMP = '{h:02}:{m:02}:{s:02};{ms:03}'
# CAPTION = {start_time} {end_time} {transcript}\n')


def format_time(seconds):
    """將秒轉換為 SRT 格式的時間字串"""
    ms = int((seconds % 1) * 1000)
    s = int(seconds)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return TIMESTAMP.format(ms=ms, s=s, m=m, h=h)

def convert2srt(source_folder, srt_folder, model_name='large-v3', language=None, traditional=True):
    
    model = WhisperModel(model_name, device="cuda", compute_type="float16")

    # 想要匹配的擴展名列表
    extensions = ['*.mkv', '*.mp4', '*.m4a', '*.wav', '*.mp3']

    # 使用列表推導式和 glob 方法來獲取所有匹配的檔案
    files = [file for ext in extensions for file in source_folder.glob(ext)]
    
    for wav_file in tqdm((files), desc='Converting Audio to SRT'):
        segments, info = model.transcribe(
            str(wav_file), beam_size=5, vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=1000),
            language=language
        )
        print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
        segments = list(segments)
        
        srt_path = srt_folder / f'{wav_file.stem}.srt'
        with open(srt_path, 'w') as file:
            for i, segment in enumerate(segments):
                start_time = format_time(segment.start)
                end_time = format_time(segment.end)
                transcript = segment.text
                caption = CAPTION.format(
                    num=i+1, start_time=start_time, 
                    end_time=end_time, transcript=transcript
                )
                file.write(caption)
        
        if traditional:
            to_traditional(
                [
                    f"{wav_file.stem}.srt"
                ]
                , 'srt'
            )


if __name__ == '__main__':
    source_folder = Path('audio')
    srt_folder = Path('srt')
    srt_folder.mkdir(exist_ok=True)
    
    convert2srt(source_folder, srt_folder)
