import typing as T
import math

import numpy as np

from src.data_model import Camera, DatasetSpec, Waypoint
from src.camera_utils import compute_image_footprint_on_surface, compute_ground_sampling_distance


def compute_distance_between_images(camera: Camera, dataset_spec: DatasetSpec) -> np.ndarray:
    """Compute the distance between images in the horizontal and vertical directions for specified overlap and sidelap.

    Args:
        camera (Camera): Camera model used for image capture.
        dataset_spec (DatasetSpec): user specification for the dataset.

    Returns:
        float: The distance between images in the horizontal direction.
        float: The distance between images in the vertical direction.
    """
    #retrieve footprint data
    footprint = compute_image_footprint_on_surface(camera, dataset_spec.height)
    footprint_x = footprint[0]
    footprint_y = footprint[1]

    #calculate distances
    horizontal_distance = footprint_x * (1- dataset_spec.overlap)
    vertical_distance = footprint_y * (1- dataset_spec.sidelap)
    
    return np.array([horizontal_distance, vertical_distance])
    # raise NotImplementedError()


def compute_speed_during_photo_capture(camera: Camera, dataset_spec: DatasetSpec, allowed_movement_px: float = 1) -> float:
    """Compute the speed of drone during an active photo capture to prevent more than 1px of motion blur.

    Args:
        camera (Camera): Camera model used for image capture.
        dataset_spec (DatasetSpec): user specification for the dataset.
        allowed_movement_px (float, optional): The maximum allowed movement in pixels. Defaults to 1 px.

    Returns:
        float: The speed at which the drone should move during photo capture.
    """
    GSD = compute_ground_sampling_distance(camera, dataset_spec.height) * allowed_movement_px
    time = dataset_spec.exposure_time_ms
    return (GSD/time)*1000
    # raise NotImplementedError()


def generate_photo_plan_on_grid(camera: Camera, dataset_spec: DatasetSpec) -> T.List[Waypoint]:
    """Generate the complete photo plan as a list of waypoints in a lawn-mower pattern.

    Args:
        camera (Camera): Camera model used for image capture.
        dataset_spec (DatasetSpec): user specification for the dataset.

    Returns:
        List[Waypoint]: scan plan as a list of waypoints.

    """
    raise NotImplementedError()
