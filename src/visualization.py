"""Utility to visualize photo plans."""

import typing as T

import plotly.graph_objects as go

from src.data_model import Waypoint


def plot_photo_plan(photo_plans: T.List[Waypoint]) -> go.Figure:
    """Plot the photo plan on a 2D grid.

    Args:
        photo_plans (T.List[Waypoint]): List of waypoints for the photo plan.

    Returns:
        T.Any: Plotly figure object.
    """
    # Retrieve waypoints for plotting
    x_coordinates = [waypoint.x for waypoint in photo_plans]
    y_coordinates = [waypoint.y for waypoint in photo_plans]
    total_waypoints = len(photo_plans)

    #Line setup
    trace = go.Scatter(
        x=x_coordinates,
        y=y_coordinates,
        mode="lines+markers",
        name="Flight Path",
        marker=dict(color="blue"),
    )

    #Graph setup
    layout = go.Layout(
        title=f"Drone Flight Trajectory: {total_waypoints} waypoints at {photo_plans[0].speed:.2f} m/s, {photo_plans[0].z} m in the air",
        xaxis=dict(title="X Coordinates (meters)"),
        yaxis=dict(title="Y Coordinates (meters)"),
        showlegend=True,
        width=800,
        height=500,
    )
    return go.Figure(data=[trace], layout=layout)
    # raise NotImplementedError()
