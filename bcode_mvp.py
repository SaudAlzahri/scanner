import streamlit as st


 ## WEB CONFIG
st.set_page_config(layout="wide", page_title="scanner",menu_items={'About': 'google.com'})
st.header("scanner")

x = '<p>fs</p>'

st.markdown(str(x), unsafe_allow_html=True)
x = '<p>fsdd</p>'




########################################################################PART 1: DEFINITIONS
person = 0
#needed for scan function
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint



#implement time keeping later (history printing)
import datetime
hours, minutes, trash = str(datetime.datetime.now().time()).split(':')
time =str(hours + ":" + minutes)

def scan_fprint():

    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('Initilization error: ' + str(e))
        exit(1)

    ## Tries to search the finger and calculate hash
    try:
        positionNumber = -1
        ## Wait that finger is read
        while positionNumber == -1:
          while ( f.readImage() == False ):
              pass

          ## Converts read image to characteristics and stores it in charbuffer 1
          f.convertImage(0x01)

          ## Searchs template
          result = f.searchTemplate()

          positionNumber = result[0]
          accuracyScore = result[1]

          if ( positionNumber == -1 ):
              print('No match found!')
        
        return positionNumber
    except Exception as e:
        print('Error: ' + str(e))
        exit(1)

def bcode_act():
      ########################################################################PART 3: BCODE ACTION (ENTER/TAKE)
       
  if bcode_reality == True:

    # DEFINING KEYS FOR LIBRARY TRANSPORTATION
    group = bcode_lib[bcode]['Group']
    fat = bcode_lib[bcode]['Fat']
    fiber = bcode_lib[bcode]['Fiber']
    sugars = bcode_lib[bcode]['Sugars']
    energy_kcal = bcode_lib[bcode]['Energy-kcal']
    protein = bcode_lib[bcode]['Protein']
    carbohydrates = bcode_lib[bcode]['Carbohydrates']
    saturated_fat = bcode_lib[bcode]['Saturated-fat']


        #Get the current item from the item directory
    current_item = (bcode_lib[bcode]['Item'])

            #Putting the item in the user contents


    for account in accounts:
        if account == person:
            user_data = accounts[account]['access_lib']
            user_history = accounts[account]['access_h']
            try:                        #Add 1 to count of the user's belly
                user_data[bcode]['Count'] += 1
                user_history[bcode]['Count'] += 1
                user_history[bcode]['Time'] += str(time)
            except KeyError:            #adding item with count of 1
                user_data[bcode] = {'Item': current_item, "Group": group, "Count": 1, "Fat": fat, 'Fiber': fiber, "Sugars": sugars, "Energy-kcal": energy_kcal, "Protein": protein, "Carbohydrates": carbohydrates, "Saturated-fat": saturated_fat}
                user_history[bcode] = {'Item': current_item, "Count": 1, "Time": [str(time)]} 


    else: pass
  else: pass

import datetime






bcode_lib = {
  6294001819226: {"Item": "Snickers", "Group": "Ultraprocessed", "Fat": 6.2, "Fiber":   0.5, "Sugars":  12.4, "Energy-kcal": 124, "Protein": 7, "Carbohydrates":       12.4, "Saturated-fat":  2.5},
  5000159366243: {"Item": "Twix",  "Group": "Ultraprocessed", "Fat":    23.7, "Fiber":  1.1, "Sugars": 48.8, "Energy-kcal": 495, "Protein": 4.5, "Carbohydrates":     64.6, "Saturated-fat":  13.7},
  1: {"Item": "Apple", "Group": "Fruit", "Fat": 0, "Fiber": 4.4, "Sugars": 19, "Energy-kcal": 95, "Protein": 1, "Carbohydrates": 25, "Saturated-fat": 0},
  2: {"Item": "Orange", "Group": "Fruit", "Fat": 0, "Fiber":  3.1, "Sugars": 12, "Energy-kcal": 60, "Protein": 1, "Carbohydrates": 15.4, "Saturated-fat": 0},
  3: {"Item": "Strawberries (1 cup or 166 grams)", "Group": "Fruit", "Fat": 0, "Fiber": 3.3, "Sugars": 7, "Energy-kcal": 53, "Protein": 1.11, "Carbohydrates": 12.7, "Saturated-fat": 0},
  0o00307444: {"Item": "Trader Joe's Canadian White Bread (1 slice)", "Group": "Grain", "Fat": 2, "Fiber": 0, "Sugars": 0, "Energy-kcal": 110, "Protein": 3, "Carbohydrates": 0, "Saturated-fat": 0},
  967787396: {"Item": "Wholesome Harvest Wheat Bread (1 slice)", "Group": "Grain", "Fat": 1.5, "Fiber": 3, "Sugars": 2, "Energy-kcal": 100, "Protein": 5, "Carbohydrates": 17, "Saturated-fat": 0},
  4: {"Item": "Potato (100 grams)", "Group": "Vegetable", "Fat": 0.1, "Fiber": 2.2, "Sugars": 0.8, "Energy-kcal": 77, "Protein": 2, "Carbohydrates": 17, "Saturated-fat": 0},
  5: {"Item": "Carrot (61 grams)", "Group": "Vegetable", "Fat": 0.1, "Fiber": 1.7, "Sugars": 2.9, "Energy-kcal": 25, "Protein": 0.6, "Carbohydrates": 6, "Saturated-fat": 0},
  6: {"Item": "85% Lean Ground Beef Broiled (100g)", "Group": "Meat", "Fat": 15, "Fiber": 0, "Sugars": 0, "Energy-kcal": 250, "Protein": 26, "Carbohydrates": 0, "Saturated-fat": 6},
  7: {"Item": "Banana", "Group": "Fruit", "Fat": 0, "Fiber": 4, "Sugars": 15, "Energy-kcal": 110, "Protein": 1, "Carbohydrates": 28, "Saturated-fat": 0},
  8: {"Item": "Broccoli (100g)", "Group": "Vegetable", "Fat": 0, "Fiber": 2.6, "Sugars": 1.7, "Energy-kcal": 38, "Protein": 3, "Carbohydrates": 7, "Saturated-fat": 0},
  6281055001424: {"Item": "Harvest Coconut Water (330 mL)", "Group": "Beverage", "Fat": 0, "Fiber": 0, "Sugars": 0, "Energy-kcal": 62, "Protein": 0, "Carbohydrates": 0, "Saturated-fat": 0},
  6281007120401: {"Item": "Almarai Fresh Milk (1 serving, 250 mL)", "Group": "Dairy", "Fat": 8, "Fiber": 0, "Sugars": 12, "Energy-kcal": 152, "Protein": 8.2, "Carbohydrates": 12, "Saturated-fat": 4.7}
}



data_lib = {
    #User Data
    'saud_data': {
    5000159366243: {'Item': 'Twix', "Group": "Ultraprocessed", 'Count': 1, 'Fat': 23.7, 'Fiber': 1.1, "Sugars":   48.8, "Energy-kcal":    495, "Protein":   4.5, "Carbohydrates":   64.6, "Saturated-fat":  13.7},
    6: {"Item": "85% Lean Ground Beef Broiled (100g)", "Group": "Meat", "Count": 1, "Fat": 15, "Fiber": 0, "Sugars": 0, "Energy-kcal": 250, "Protein": 26, "Carbohydrates": 0, "Saturated-fat": 6},
    4: {"Item": "Potato (100 grams)", "Group": "Vegetable", "Count": 1, "Fat": 0.1, "Fiber": 2.2, "Sugars": 0.8, "Energy-kcal": 77, "Protein": 2, "Carbohydrates": 17, "Saturated-fat": 0},
    2: {"Item": "Orange", "Group": "Fruit", "Count": 2, "Fat": 0, "Fiber": 3.1, "Sugars": 12, "Energy-kcal": 60, "Protein": 1, "Carbohydrates": 15.4, "Saturated-fat": 0},
    967787396: {"Item": "Wholesome Harvest Wheat Bread (1 slice)", "Group": "Grain", "Count": 3, "Fat": 1.5, "Fiber": 3, "Sugars": 2, "Energy-kcal": 100, "Protein": 5, "Carbohydrates": 17, "Saturated-fat": 0},
    3: {"Item": "Strawberries (1 cup or 166 grams)", "Group": "Fruit", "Count": 3, "Fat": 0, "Fiber": 3.3, "Sugars": 7, "Energy-kcal": 53, "Protein": 1.11, "Carbohydrates": 12.7, "Saturated-fat": 0}
    },
    'basma_data': {
    5000159366243: {'Item': 'Twix', "Group": "Ultraprocessed", 'Count': 4, 'Fat': 23.7, 'Fiber':1.1, "Sugars":   48.8, "Energy-kcal":    495, "Protein":   4.5, "Carbohydrates":   64.6, "Saturated-fat":  13.7},
    6294001819226: {"Item": "Snickers", "Group": "Ultraprocessed", "Count": 5, "Fat":     6.2, "Fiber":   0.5, "Sugars":  12.4, "Energy-kcal":    124, "Protein": 7, "Carbohydrates":       12.4, "Saturated-fat":  2.5}
    },
    'bedbed_data': {
    6294001819226: {"Item": "Snickers", "Group": "Ultraprocessed", "Count": 1, "Fat":     6.2, "Fiber":   0.5, "Sugars":  12.4, "Energy-kcal":    124, "Protein": 7, "Carbohydrates":       12.4, "Saturated-fat":  2.5}
    },
    'mohammad_data': {},
    'sara_data': {
    5000159366243: {'Item': 'Twix', "Group": "Ultraprocessed", 'Count': 4, 'Fat': 23.7, 'Fiber':1.1, "Sugars":   48.8, "Energy-kcal":    495, "Protein":   4.5, "Carbohydrates":   64.6, "Saturated-fat":  13.7}
    },

}



history_lib = {

    #User History
    'saud_history': {
    5000159366243: {'Item': 'Twix', 'Count': 1, "Time": ['5:40']},
    6: {"Item": "85% Lean Ground Beef Broiled (100g)", "Count": 1, 'Time': ['5:30']},
    4: {"Item": "Potato (100 grams)", "Count": 1, 'Time': ['7:45']},
    2: {"Item": "Orange", "Count": 2, "Time": ['9:03', '11:30']},
    967787396: {"Item": "Wholesome Harvest Wheat Bread (1 slice)", "Count": 3, "Time": ['6:50', '12:07', '12:53']},
    3: {"Item": "Strawberries (1 cup or 166 grams)", "Count": 3, "Time": ['6:30', '12:57', '16:53']}

    },

    'basma_history': {
    5000159366243: {'Item': 'Twix', 'Count': 4, "Time": ["3:15", "3:30", '4:18', '5:50']},
    6294001819226: {"Item": "Snickers","Count": 5, "Time": ["18:53", "19:17", '20:03', "20:07", "22:31"]}},
    'bedbed_history': {
    6294001819226: {"Item": "Snickers",  "Count": 1, "Time": ['13:18']}},
    'mohammad_history': {},
    'sara_history': {
    5000159366243: {'Item': 'Twix', 'Count': 4, 'Time': ['3:45', '14:45', '17:30', '8:23']}
    },

}



accounts = {
  'Saud': {'Password': '1234', 'f_print' : 0, 'access_lib': data_lib['saud_data'], 'access_h': history_lib['saud_history']}, 
  'Basma': {'Password': '1234', 'f_print' : 1, 'access_lib': data_lib['basma_data'], 'access_h': history_lib['basma_history']}, 
  'Bedbed': {'Password': '1234', 'f_print' : 2, 'access_lib': data_lib['bedbed_data'], 'access_h': history_lib['bedbed_history']}, 
  'Mohammad': {'Password': '1234', 'f_print' : 3, 'access_lib': data_lib['mohammad_data'], 'access_h': history_lib['mohammad_history']}, 
  'Sara': {'Password': '1234', 'f_print' : 4, 'access_lib': data_lib['sara_data'], 'access_h': history_lib['sara_history']}}








########################################################################PART 2: GETTING BCODE (CAMERA AND BARCODE SCANNER)
#getting bcode from camera
#if nothng detected, get from barcode scanner

f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
import cv2
import torch
from skimage import io

# Capturing video through channel 0
video = cv2.VideoCapture(0)

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


from PIL import Image
from pyzbar.pyzbar import decode
print('SCAN NOW')
#In this while loop shall be part 2, 3
try:
    while True:
        positionNumber = scan_fprint()


        for account in accounts:
            if positionNumber == accounts[account]['f_print']:
                person = account
                print('hi', person)
        
        while f.readImage() == False:

            #bcode verification
            bcode_reality = True

            check, frame = video.read()

            # Inference
            results = model(frame)
            print(results)

            #Get barcode (replace with scalable lib method)
            if 'banana' in str(results):
                bcode = 7
                bcode_act()
            elif 'apple' in str(results):
                bcode = 1
                bcode_act()
            elif 'orange' in str(results):
                bcode = 2
                bcode_act()
            elif 'broccoli' in str(results):
                bcode = 8
                bcode_act()
            elif 'carrot' in str(results):
                bcode = 5
                bcode_act()
            else:


                # use camera to detect barcodes


                decoded_list = decode(frame)
                print(decoded_list)
                count = 0
                while (count + 1) <= len(decoded_list) and len(decoded_list) != 0:
                    trash, bcode, trash, trash, trash, trash, trash = str(decoded_list[count]).split("'")
                    print(bcode)
                    bcode_act()
                    count +=1

except KeyboardInterrupt:   #CLOSING (CTR-C)    #Now do part 4, 5 & 6
    video.release()
    cv2.destroyAllWindows()


