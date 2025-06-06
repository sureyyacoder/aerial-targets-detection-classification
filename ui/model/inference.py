from ultralytics import YOLO
import cv2
import os
import uuid

model = YOLO("model/best.pt")

def run_inference(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    os.makedirs("static/detections", exist_ok=True)  # klasör yoksa oluştur
    results_list = []
    seen = set()

    # RESİM işleme
    if ext in ['.jpg', '.jpeg', '.png']:
        image = cv2.imread(filepath)
        if image is None:
            return [{"time": "Image", "object": "Could not read image", "confidence": 0, "image_path": ""}]
        
        results = model(image, verbose=False)
        for r in results:
            for box in r.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                if confidence > 0.5:
                    label = model.names[class_id]
                    unique_id = uuid.uuid4().hex[:8]
                    image_name = f"static/detections/image_{unique_id}.jpg"

                    # BBox çiz
                    xyxy = box.xyxy[0].cpu().numpy().astype(int)
                    cv2.rectangle(image, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
                    cv2.putText(image, f"{label} ({confidence:.2f})", (xyxy[0], xyxy[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                    cv2.imwrite(image_name, image)

                    results_list.append({
                        "time": "Image",
                        "object": label,
                        "confidence": round(confidence, 2),
                        "image_path": image_name
                    })

        return results_list if results_list else [{"time": "Image", "object": "No object detected", "confidence": 0, "image_path": ""}]

    # VİDEO işleme
    elif ext in ['.mp4', '.avi', '.mov', '.mkv']:
        cap = cv2.VideoCapture(filepath)
        if not cap.isOpened():
            return [{"time": "00:00", "object": "Video could not be opened", "confidence": 0, "image_path": ""}]
        
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_id = 0
        frame_limit = 150  # İsteğe bağlı sınırlandırma

        while True:
            ret, frame = cap.read()
            if not ret or frame_id > frame_limit:
                break

            frame_id += 1
            seconds = int(frame_id / fps)
            minutes = int(seconds // 60)
            seconds = seconds % 60
            timestamp = f"{minutes:02d}:{seconds:02d}"

            results = model(frame, verbose=False)
            for r in results:
                for box in r.boxes:
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    if confidence > 0.5:
                        label = model.names[class_id]
                        key = (timestamp, label)

                        if key not in seen:
                            seen.add(key)
                            xyxy = box.xyxy[0].cpu().numpy().astype(int)
                            cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (255, 0, 0), 2)
                            cv2.putText(frame, f"{label} ({confidence:.2f})", (xyxy[0], xyxy[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

                            unique_id = uuid.uuid4().hex[:8]
                            image_name = f"static/detections/frame_{unique_id}.jpg"
                            cv2.imwrite(image_name, frame)

                            results_list.append({
                                "time": timestamp,
                                "object": label,
                                "confidence": round(confidence, 2),
                                "image_path": image_name
                            })

        cap.release()
        return results_list if results_list else [{"time": "00:00", "object": "No object detected", "confidence": 0, "image_path": ""}]

    else:
        return [{"time": "00:00", "object": "Unsupported file type", "confidence": 0, "image_path": ""}]

