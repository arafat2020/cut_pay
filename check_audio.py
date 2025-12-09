import av
import sys

try:
    container = av.open("videos/sample.mp4")
    print(f"Streams: {len(container.streams)}")
    for stream in container.streams:
        print(f"Stream: {stream.type}")
    
    audio_streams = [s for s in container.streams if s.type == 'audio']
    if not audio_streams:
        print("❌ No audio stream found!")
    else:
        print(f"✅ Found {len(audio_streams)} audio streams")
except Exception as e:
    print(f"Error: {e}")
