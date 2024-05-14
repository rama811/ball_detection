import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model_pose = YOLO('yolov8n-pose.pt')
pretrained_model = YOLO('models/best.pt')

# Open the video file
video_path = "video_test/Real_Madrid_vs_Barcelona_2016_2017_acortado.mp4"
cap = cv2.VideoCapture(video_path)

# Configura el tamaño del video y el codec
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter('video_results/output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        #result_pose = model_pose.track(frame, persist=True)
        pretrained_result = pretrained_model.track(frame, persist=True)

        # Visualize the results on the frame
        #annotated_frame = result_pose[0].plot()
        annotated_frame = pretrained_result[0].plot()

        # Escribe el frame en el video de salida
        out.write(annotated_frame)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()