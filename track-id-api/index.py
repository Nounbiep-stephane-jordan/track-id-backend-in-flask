from flask import Flask,jsonify,request
from flask_cors import CORS
import cv2
import pytesseract
import numpy as np
import base64

app = Flask(__name__)
CORS(app)


def is_valid_base64(string):
    try:
        base64.b64decode(string)
        return True
    except base64.binascii.Error:
        return False

 

def enhance_image(base64_string):
    pytesseract.pytesseract.tesseract_cmd = 'F:\\Tessseract-OCR\\tesseract.exe'
    image_data = base64.b64decode(base64_string)
    np_arr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # img = cv2.imread("C:\\Users\\NJS\\Desktop\\all project\\Track-id\\backend_Flask\\track-id-backend-in-flask\\track-id-api\\sample.jpg")
    # lessnoise = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
    # threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) [1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('process Image gray', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    text = pytesseract.image_to_string(gray)
        
    print('----text',text,"text----")
 
  
    

    
    # # Convert the image to gray scale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # # Performing OTSU threshold
    # ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    
    # # Specify structure shape and kernel size. 
    # # Kernel size increases or decreases the area 
    # # of the rectangle to be detected.
    # # A smaller value like (10, 10) will detect 
    # # each word instead of a sentence.
    # rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    
    # # Applying dilation on the threshold image
    # dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    
    # # Finding contours
    # contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
    #                                                 cv2.CHAIN_APPROX_NONE)
    
    # # Creating a copy of image
    # im2 = img.copy()

    # # Display the  image
    # cv2.imshow('process Image', im2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # # A text file is created and flushed
    # file = open("recognized.txt", "w+")
    # file.write("")
    # file.close()
    
    # # Looping through the identified contours
    # # Then rectangular part is cropped and passed on
    # # to pytesseract for extracting text from it
    # # Extracted text is then written into the text file
    # for cnt in contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
        
    #     # Drawing a rectangle on copied image
    #     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    #     # Cropping the text block for giving input to OCR
    #     cropped = im2[y:y + h, x:x + w]
        
    #     # Open the file in append mode
    #     file = open("recognized.txt", "a")
        
    #     # Apply OCR on the cropped image
    #     text = pytesseract.image_to_string(cropped)
        
    #     print('----text',text,"text----")
    #     # Appending the text into file
    #     file.write(text)
    #     file.write("\n")
        
    #     # Close the file
    #     file.close
    

@app.route("/")
def get():
    return jsonify("api working correctly")

@app.route("/process_image",methods=['POST'])
def process_image():
    data = request.get_json()
    isvalid = is_valid_base64(data['image'])
    if isvalid == True :
       enhance_image(data['image'])
       return jsonify({"message":"data processed sucessfully"})
    else :
       return jsonify({"error":"invalid data cannot process image"})
     

