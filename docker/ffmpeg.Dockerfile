# FFmpeg base image
# Note: This image is AMD64 only. On Apple Silicon (ARM64), Docker will use emulation.
# This is expected and will work correctly, though slightly slower than native ARM64.
FROM jrottenberg/ffmpeg:6.0-ubuntu

WORKDIR /data

# Container receives:
#   - input video mounted into /data
#   - timestamps from FastAPI
#   - output clips saved in /data/output
