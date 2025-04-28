"""Data models for the camera and user specification."""
from dataclasses import dataclass

@dataclass
class Camera:
    """
    Data model for a simple pinhole camera.
    
    References: 
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """
    fx : float
    fy : float
    cx : float
    cy : float
    sensor_size_x_mm : float # single pixel size * number of pixels in X dimension
    sensor_size_y_mm : float # single pixel size * number of pixels in Y dimension
    image_size_x_px : int
    image_size_y_px : int
    pass

@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """
    overlap : float
    sidelap : float
    height : float # 100 ft
    scan_dimension_x : int
    scan_dimension_y : int
    exposure_time_ms : int # 1/500 exposure time
    pass


@dataclass
class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """
    pass