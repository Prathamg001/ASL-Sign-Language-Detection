import gradio as gr
import cv2 as cv
from signlang import process_frame


def process_video(video_path):
    print(f"Received video path: {video_path}")

    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video")
        return "Could not open video"

    results = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        result = process_frame(frame)
        results.append(result)  # Append the label
    cap.release()

    print(f"Results: {results}")

    if results:
        most_common_result = max(set(results), key=results.count)
        print(f"Most common result: {most_common_result}")
        return most_common_result
    return "No result"


iface = gr.Interface(fn=process_video, inputs=gr.Video(label="Webcam"), outputs="label")
iface.launch()