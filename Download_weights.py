import gdown

# Google Drive file ID
file_id = "1A2B3C4D5E6F7G8H9I0J"
url = "https://drive.google.com/file/d/1Pp6cDAKHmy_oURXjTPKWHvgFxjHLsrZN/view?usp=sharing"

output = "yolov5s.pt"

print("Downloading YOLOv5 model weights...")
gdown.download(url, output, quiet=False)

print("Download complete!")
