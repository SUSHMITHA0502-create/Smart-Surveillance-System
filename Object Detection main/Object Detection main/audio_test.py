import winsound
import os

# Path to the alarm sound file
ALARM_SOUND = r'F:\project\object detection using yolo\Object Detection main\alarm.mp3'

# Check if the file exists before playing it
if os.path.exists(ALARM_SOUND):
    print(f"Alarm sound file found at: {ALARM_SOUND}")
    try:
        winsound.PlaySound(ALARM_SOUND, winsound.SND_FILENAME)
        print("Alarm sound played successfully.")
    except Exception as e:
        print(f"Error playing sound: {e}")
else:
    print("Error: Alarm sound file not found.")
