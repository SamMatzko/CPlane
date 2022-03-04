"""A module for displaying things on a mathematical coordinate plane.
This uses tkinter.Canvas, but, unlike tkinter.Canvas, it has (0, 0) in
the center of the plane."""

import tkinter

class CPlane(tkinter.Canvas):
    """The coordinate plane."""
    
    def __init__(self, *args, rangex=200, rangey=200, **kwargs):
        tkinter.Canvas.__init__(self, *args, **kwargs)
        
        # Our ranges; defaults to w×h 200×200
        self.rangex = rangex
        self.rangey = rangey
        
        # Our size (in pixels); is updated with all calls to self.__adjust
        self.width = self.cget("width")
        self.height = self.cget("height")
        
        # The text to show the coords for the mouse
        self.coords_text = self.create_text(100, 100, text="Hello!")
        
        # Bind our adjust function to whenever the canvas is resized
        self.bind("<Configure>", self.__adjust)
        self.bind("<Motion>", self.__show_coords)
        
    def __adjust(self, event):
        """Update all necessary variables/display items when the canvas is changed."""
        
        # Set the new width and height
        self.width, self.height = event.width, event.height
        
        # Call self.__draw_axes to update the plane
        self.__draw_axes()
        
    def __draw_axes(self):
        """Draw the axes and the grid for the coordinate plane."""

        # Clear the canvas
        self.delete("deletable")
        
        # Create the axis lines
        self.create_line(0, self.height / 2, self.width, self.height / 2, fill="#000000", width=2, tag="deletable")
        self.create_line(self.width / 2, 0, self.width / 2, self.height, fill="#000000", width=2, tag="deletable")
        
    def __show_coords(self, event):
        coords = self.convertc_pix((event.x, event.y))
        self.moveto(self.coords_text, event.x + 10, event.y)
        self.itemconfigure(self.coords_text, text=f"({coords[0]}, {coords[1]})")
        self.tag_raise(self.coords_text)

    def convertc_pix(self, coords):
        """Return cplane (x, y) for canvas (x, y) COORDS, in pixels, using the
        below formula:
        
        x2 = (ax)(x1) - ox
        y2 = -((ay)(y1) - oy)
        
        Where:
            x1 = x of canvas point (in pixels)
            y1 = y of canvas point (in pixels)
            """
        
        # The scale factors for x and y
        ax = self.rangex / self.width
        ay = self.rangey / self.height
        
        # The offsets for x and y
        ox = self.rangex / 2
        oy = self.rangey / 2
        
        # Calculate the x and y separately
        px = (ax * coords[0]) - ox
        py = -((ay * coords[1]) - oy)
        
        return (int(px), int(py))