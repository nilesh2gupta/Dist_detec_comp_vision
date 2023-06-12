import cv2
import math
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)

while True:
    ret, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)
    x1,x2,y1,y2=0,0,0,0
    if len(faces) > 0:
        face1 = faces[0]
        point1=face1[145]
        x1=point1[0]
        y1=point1[1]
        
        cv2.circle(img, point1, 5, (25, 255, 55), cv2.FILLED)

    if len(faces) > 1:
        face2 = faces[1]
        point2=face2[374]
        x2=point2[0]
        y2=point2[1]
        cv2.circle(img, point2, 5, (25, 255, 55), cv2.FILLED)
        cv2.line(img, face1[145], face2[374], (255, 0, 255), 3)
    p1=(x1+x2)//2
    p2=(y1+y2)//2
    diff1=(x1-x2)**2
    diff2=(y1-y2)**2
    total=diff1+diff2
    distance=math.sqrt(total)
    cv2.putText(img,org=(p1,p2),fontScale=0.5,color=(255,25,0),thickness=1,lineType=cv2.LINE_AA,text="Distance="+str(distance)
                ,fontFace=cv2.FONT_ITALIC)   

    
   
    cv2.imshow("ImageFrane", img)

    if cv2.waitKey(25) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
