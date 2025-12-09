# Docker FFmpeg Setup

## Current Setup

The project uses `jrottenberg/ffmpeg:6.0-ubuntu` as the base image.

### Platform Warning on Apple Silicon

If you see this warning on Apple Silicon (M1/M2/M3) Macs:

```
InvalidBaseImagePlatform: Base image was pulled with platform "linux/amd64",
expected "linux/arm64" for current build
```

**This is normal and safe to ignore.** Docker automatically uses emulation to run AMD64 images on ARM64 Macs.

## Build Commands

### Current Dockerfile (with emulation on ARM64)

```bash
docker build -t ffmpeg-container -f docker/ffmpeg.Dockerfile .
```

### Alternative Multi-Architecture Dockerfile (no warning)

```bash
docker build -t ffmpeg-container -f docker/ffmpeg-multiarch.Dockerfile .
```

## Running the Container

```bash
docker run --rm \
    -v $(pwd)/videos:/data \
    ffmpeg-container \
    -y -i /data/input.mp4 \
    -ss 00:00:10 -to 00:00:20 \
    -c copy /data/output.mp4
```

Or use the provided script:

```bash
./run_ffmpeg.sh input.mp4 00:00:10 00:00:20 output.mp4
```

## Performance Notes

- **AMD64 on ARM64**: Slight performance overhead due to emulation (~5-10% slower)
- **Native ARM64**: Full native performance
- For most video processing tasks, the difference is negligible
