import whisper
import os

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # "small", "medium", "large" 가능
    result = model.transcribe(audio_path)
    return result["text"]

def transcribe_folder(folder_path):
    if not os.path.exists(folder_path):
        print("폴더가 존재하지 않습니다.")
        return
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".mp3") or file_name.endswith(".m4a"):
            file_path = os.path.join(folder_path, file_name)
            text = transcribe_audio(file_path)
            print(f"{file_name} 변환 완료:\n{text}\n")

if __name__ == "__main__":
    folder_path = "audios"  # 변환할 오디오 파일이 있는 폴더 경로
    transcribe_folder(folder_path)