# Required 'pip install's
- openai-whisper
- pydub
- ffmpeg-python

# Where to Start?
- Right-click your audio file in your File Explorer and click *Copy as Path*.
- Paste that path in `WhisperTranscribe.py`, line 42 just between the quotes for *r""*, make sure there are no double-quotes though.
- `WhisperTranscribe.py` analyzes audio in chunks, and *chunk_length* (line 46) determines how many seconds in each chunk. You can adjust it depending on how long your audio file is, the default is *chunk_length=300* for 5 minutes per chunk.
- Run  `WhisperTranscriber.py`, it will first break the audio down, shown as chunks, then output a text file within the same directory called `_whisper_transcription_chunks.txt`
- 'Resamble' the audio file if the output text is unclear, using `resamble.py`, where you would paste the audio file's path in *r""* line 53 and then use the new audio file outputted by it for `WhisperTranscribe.py`'s new audio file path.