import whisper
from pydub import AudioSegment

# Load the Whisper model
model = whisper.load_model("base")  # You can also use "small", "medium", or "large"

# Function to split audio into chunks (in seconds)
def split_audio(audio_file, chunk_length=300):  # Default is 5-minute chunks (300 seconds)
    sound = AudioSegment.from_file(audio_file)
    chunks = []
    for i in range(0, len(sound), chunk_length * 1000):
        chunk = sound[i:i + chunk_length * 1000]
        chunks.append(chunk)
    return chunks

# Function to transcribe each chunk
def transcribe_chunk(chunk, chunk_idx):
    # Save chunk as a temporary WAV file
    chunk_file = f"chunk_{chunk_idx}.wav"
    chunk.export(chunk_file, format="wav")
    
    # Transcribe using Whisper
    result = model.transcribe(chunk_file)
    
    return result["text"]

# Main transcription function with chunking
def transcribe_with_whisper_in_chunks(audio_file, chunk_length=300):
    chunks = split_audio(audio_file, chunk_length)
    transcription = ""

    # Transcribe each chunk and combine results
    for i, chunk in enumerate(chunks):
        print(f"Transcribing chunk {i + 1} of {len(chunks)}...")
        chunk_text = transcribe_chunk(chunk, i)
        transcription += f"Chunk {i + 1}:\n{chunk_text}\n\n"
    
    return transcription

# Example usage
if __name__ == "__main__":
    audio_file_path = r"" # ENTER AUDO FILE'S PATH HERE
    
    # Transcribe the audio in chunks
    print("Transcribing audio in chunks...")
    transcription = transcribe_with_whisper_in_chunks(audio_file_path, chunk_length=300)  # 5-minute chunks

    # Save transcription to a text file using UTF-8 encoding
    output_file = audio_file_path.replace(".wav", "_whisper_transcription_chunks.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transcription)

    print(f"Transcription saved to {output_file}")
