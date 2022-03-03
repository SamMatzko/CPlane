"""A module for displaying things on a mathematical coordinate plane.
This uses tkinter.Canvas, but, unlike tkinter.Canvas, it has (0, 0) in
the center of the plane."""

import tkinter

class CPlane(tkinter.Canvas):
    """The coordinate plane."""
    
    def __init__(self, *args, **kwargs):
        tkinter.Canvas.__init__(self, *args, **kwargs)