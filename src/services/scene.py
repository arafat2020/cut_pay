"""Scene Detection Service"""
from pathlib import Path
from typing import List, Tuple
from scenedetect import open_video, SceneManager, ContentDetector

class SceneDetectionService:
    @staticmethod
    def detect_scenes(video_path: Path, threshold: float = 27.0) -> List[Tuple[float, float]]:
        """
        Detect scenes in a video using PySceneDetect.
        Returns a list of (start_time, end_time) tuples in seconds.
        """
        if not video_path.exists():
            raise FileNotFoundError(f"Video file not found: {video_path}")

        video = open_video(str(video_path))
        scene_manager = SceneManager()
        
        # Add ContentDetector algorithm (detects fast cuts)
        scene_manager.add_detector(ContentDetector(threshold=threshold))
        
        # Detect scenes
        scene_manager.detect_scenes(video, show_progress=True)
        
        # Get scene list
        scene_list = scene_manager.get_scene_list()
        
        # Convert to seconds
        scenes = []
        for scene in scene_list:
            start, end = scene
            scenes.append((start.get_seconds(), end.get_seconds()))
            
        return scenes
