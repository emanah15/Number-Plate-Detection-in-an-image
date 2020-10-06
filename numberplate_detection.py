import cv2

car = cv2.imread('C:\\Users\\ahmad\\Desktop/car.jpg')

plateCascade = cv2.CascadeClassifier('C:\\Users\\ahmad\\Desktop/haarcascade_russian_plate_number.xml')

# convert it into gray image
imgGray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)

# Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles
numberPlate = plateCascade.detectMultiScale(imgGray)

for (x,y,w,h) in numberPlate: # after detection using bounding boxes
    #area = w*h
    #if area > 500:
        cv2.rectangle(car, (x,y), (x+w, y+h), (0,0,120), 1)
        cv2.putText(car, "number plate", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (123, 124, 255), 1)

        # OPTIONAL: for seeing the number plate separately in another window
        imgROI = car[y:y+h, x: x+w]
        cv2.imshow('number plate', imgROI)

cv2.imshow('car', car)
cv2.waitKey(0)