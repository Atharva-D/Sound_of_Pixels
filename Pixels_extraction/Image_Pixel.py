import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class PixelSelector:
    def __init__(self, image):
        self.image = image
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(image)
        self.ax.set_title("Click on any part of the image")
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.selected_pixels = []

    def onclick(self, event):
        x, y = int(event.xdata), int(event.ydata)
        if 0 <= x < self.image.shape[1] and 0 <= y < self.image.shape[0]:
            print("Clicked at coordinates (x={}, y={})".format(x, y))
            print("RGB values:", self.image[y, x])  # Image uses (y, x) indexing
            self.selected_pixels.append((x, y))
            self.ax.plot(x, y, 'ro')  # Mark the selected pixel with a red dot
            self.fig.canvas.draw()

    def show(self):
        plt.show()

# Load the image
image_path = r"F:\Sound_of_Pixels\data\frames\clarinet acoustic_guitar\Dave Stewart & Candy Dulfer - Lily Was Here (Cover by The Duo Gitarinet)\000270.jpg"  # Replace with the path to your image
image = mpimg.imread(image_path)

# Create PixelSelector object
selector = PixelSelector(image)

# Show the image and handle clicks
selector.show()
