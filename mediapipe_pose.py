import mediapipe as mp
import cv2
import glob2
import os

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_face_mesh = mp.solutions.face_mesh

TRIM_VID_PATH = 'trim_data'
POSE_PATH = 'pose_data'

def read_vidnames():
    vid_path = glob2.glob(f'{TRIM_VID_PATH}/*.*')
    return vid_path

def videoto_pose():
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
 
  if (os.path.exists(POSE_PATH)):
    print("Success")
  else:
    os.mkdir(POSE_PATH)

  for vid in read_vidnames():
    cap = cv2.VideoCapture(f"{vid}")
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        
        while cap.isOpened():
            ret, frame = cap.read()
            
            # Recolor Feed
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Make Detections
            results = holistic.process(image)
            # print(results.face_landmarks)
            
            # face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
            
            # Recolor image back to BGR for rendering
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Draw face landmarks
            mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS)
            
            # Right hand
            mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Left Hand
            mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

            # Pose Detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
                            
            cv2.imshow('Raw Webcam Feed', image)

            # if cv2.waitKey(10) & 0xFF == ord('q'):
            #     break

videoto_pose()
# cap.release()
# cv2.destroyAllWindows()