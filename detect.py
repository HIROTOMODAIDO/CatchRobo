import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
#model = YOLO('best.pt')

video_path = 1
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
	success, frame = cap.read()
	if success:
		results = model(frame)

		imageWidth = results[0].orig_shape[0]
		imageHeight = results[0].orig_shape[1]

		names = results[0].names
		classes = results[0].boxes.cls
		boxes = results[0].boxes
		annotatedFrame = results[0].plot()

		for box, cls in zip(boxes, classes):
			name = names[int(cls)]
			x1, y1, x2, y2 = [int(i) for i in box.xyxy[0]]
			print(f"Object: {name} Coordinates: StartX={x1}, StartY={y1}, EndX={x2}, EndY={y2}")
			cv2.putText(annotatedFrame, f"{x1} {y1} {x2} {y2}", (x1, y1 - 40), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 0), 2, cv2.LINE_AA)
			
			x_center = int((x1+x2)/2)
			y_center = int((y1+y2)/2)
			
			print(f"Object: {name} Coordinates: StartX={x1}, StartY={y1}, EndX={x2}, EndY={y2}")			

			cv2.line(annotatedFrame,(x1, y_center),(x2, y_center) ,color=(255, 0, 0), thickness=2)
			cv2.line(annotatedFrame,(x_center, y1),(x_center, y2) ,color=(255, 0, 0), thickness=2)
			cv2.putText(annotatedFrame, f"{x_center} {y_center}", (x_center-20, y_center - 20), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 0), 2, cv2.LINE_AA)

		cv2.imshow("YOLOv8 Inference", annotatedFrame)
	
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break	
	else: 
		break
        
cap.release()
cv2.destroyAllWindows()