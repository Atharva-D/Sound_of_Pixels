import cv2

class PixelSelectorVideo:
    def __init__(self, video_path):
        self.video_path = video_path
        self.selected_pixels = []

    def on_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("Clicked at coordinates (x={}, y={})".format(x, y))
            self.selected_pixels.append((x, y))

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Error: Failed to open video.")
            return

        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        # Create window and set mouse callback
        cv2.namedWindow("Video")
        cv2.setMouseCallback("Video", self.on_click)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Display frame
            for x, y in self.selected_pixels:
                cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)  # Mark the clicked pixel with a red circle
            cv2.imshow("Video", frame)

            key = cv2.waitKey(1000 // fps) & 0xFF
            if key == 27:  # ESC key
                break

        cap.release()
        cv2.destroyAllWindows()

# Path to the video file
video_path = r"F:\Sound_of_Pixels\Dataset\MUSIC_duet_videos\cello acoustic_guitar\What Child Is This   Guitar & Cello.mp4"  # Replace with the path to your video file

# Create PixelSelectorVideo object
selector_video = PixelSelectorVideo(video_path)

# Run the pixel selection process
selector_video.run()
