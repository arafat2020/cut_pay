# Alternative Dockerfile using Alpine-based FFmpeg with ARM64 support
# This eliminates the platform warning on Apple Silicon Macs
FROM linuxserver/ffmpeg:latest

WORKDIR /data

# Container receives:
#   - input video mounted into /data
#   - timestamps from FastAPI
#   - output clips saved in /data/output
