# import pyflac # python venv setup needed ig

filename = "file"
ffmpeg_cmd = f"ffmpeg -i ${filename} -f s16le -acodec pcm_s16le output.raw"


