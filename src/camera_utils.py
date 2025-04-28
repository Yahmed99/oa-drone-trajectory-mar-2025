"""Utility functions for the camera model."""

import numpy as np

from src.data_model import Camera


def compute_focal_length_in_mm(camera: Camera) -> np.ndarray:
    """Computes the focal length in mm for the given camera

    Args:
        camera (Camera): the camera model.

    Returns:
        np.ndarray: [fx, fy] in mm.
    """
    # raise NotImplementedError()
    # Note(Ayush): Solution provided by project leader.
    pixel_to_mm_x = camera.sensor_size_x_mm / camera.image_size_x_px
    pixel_to_mm_y = camera.sensor_size_y_mm / camera.image_size_y_px

    return np.array([camera.fx * pixel_to_mm_x, camera.fy * pixel_to_mm_y])


def project_world_point_to_image(camera: Camera, point: np.ndarray) -> np.ndarray:
    """Project a 3D world point into the image coordinates.

    Args:
        camera (Camera): the camera model
        point (np.ndarray): the 3D world point

    Returns:
        np.ndarray: [u, v] pixel coordinates corresponding to the point.
    """
    X, Y, Z = point
    fx = camera.fx
    fy = camera.fy
    cx = camera.cx
    cy = camera.cy

    x = fx * (X / Z)
    y = fy * (Y / Z)

    u = x + cx
    v = y + cy

    return np.array([u, v], dtype=np.float32)
    # raise NotImplementedError()


def compute_image_footprint_on_surface(
    camera: Camera, distance_from_surface: float
) -> np.ndarray:
    """Compute the footprint of the image captured by the camera at a given distance from the surface.

    Args:
        camera (Camera): the camera model.
        distance_from_surface (float): distance from the surface (in m).

    Returns:
        np.ndarray: [footprint_x, footprint_y] in meters.
    """

    Z = distance_from_surface

    # find X and Y for the top left
    u_top_left = 0
    v_top_left = 0
    X_top_left = (u_top_left - camera.cx) * Z / camera.fx
    Y_top_left = (v_top_left - camera.cy) * Z / camera.fy

    # find X and Y for the bottom right
    u_bottom_right = camera.image_size_x_px
    v_bottom_right = camera.image_size_y_px
    X_bottom_right = (u_bottom_right - camera.cx) * Z / camera.fx
    Y_bottom_right = (v_bottom_right - camera.cy) * Z / camera.fy

    # return the difference for the width and height of the footprint (in meters)
    X = X_bottom_right - X_top_left
    Y = Y_bottom_right - Y_top_left

    return np.array([X, Y])
    # raise NotImplementedError()


def compute_ground_sampling_distance(
    camera: Camera, distance_from_surface: float
) -> float:
    """Compute the ground sampling distance (GSD) at a given distance from the surface.

    Args:
        camera (Camera): the camera model.
        distance_from_surface (float): distance from the surface (in m).

    Returns:
        float: the GSD in meters (smaller among x and y directions).
    """
    #calculate footprint
    footprint = compute_image_footprint_on_surface(camera, distance_from_surface)
    footprint_x, footprint_y = footprint
    
    gsd_x = footprint_x/camera.image_size_x_px
    gsd_y = footprint_y/camera.image_size_y_px

    return min(gsd_x, gsd_y)
    # raise NotImplementedError()
