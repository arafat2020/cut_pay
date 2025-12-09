import sys
from pathlib import Path
import traceback

# Add src to path
sys.path.append(".")

from src.services.scene import SceneDetectionService
from src.services.transcription import TranscriptionService
from src.services.analysis import AnalysisService

VIDEO_PATH = Path("videos/sample.mp4")
MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

def test_pipeline():
    print(f"Testing pipeline with {VIDEO_PATH}")
    
    if not VIDEO_PATH.exists():
        print("Video not found!")
        return

    try:
        print("\n1. Testing Scene Detection...")
        scene_service = SceneDetectionService()
        scenes = scene_service.detect_scenes(VIDEO_PATH)
        print(f"✅ Detected {len(scenes)} scenes")
    except Exception:
        print("❌ Scene Detection Failed")
        traceback.print_exc()
        return

    try:
        print("\n2. Testing Transcription...")
        transcription_service = TranscriptionService(model_size="base")
        transcript = transcription_service.transcribe(VIDEO_PATH)
        print(f"✅ Transcribed {len(transcript)} segments")
    except Exception:
        print("❌ Transcription Failed")
        traceback.print_exc()
        return

    try:
        print("\n3. Testing Analysis...")
        if not Path(MODEL_PATH).exists():
            print(f"⚠️ Model not found at {MODEL_PATH}, skipping analysis test")
            return
            
        analysis_service = AnalysisService(model_path=MODEL_PATH)
        result = analysis_service.analyze_content(transcript, scenes, 30.0)
        print("✅ Analysis Complete")
        print(result)
    except Exception:
        print("❌ Analysis Failed")
        traceback.print_exc()
        return

if __name__ == "__main__":
    test_pipeline()
