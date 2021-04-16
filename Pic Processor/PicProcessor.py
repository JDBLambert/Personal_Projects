# Screenshot Processor for DoorDash

import os
import re
from PIL import Image
from datetime import datetime as dt
import sys
import pytesseract
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

timestart = time.time()
bad_char_list = ['-', '«', '+', '~', '°', '¢', '€']

# get all files from repository
f = open('CompletedPhotos.txt', 'r+')
f_data = f.readlines()
processedPics = [files.strip() for files in f_data]
processedPics = [files.split('\t')[0] for files in processedPics]

# get all pics from pic directory
os.chdir("C:/Users/Jacob/Downloads/Screenshots")
allFiles = os.listdir()
allFiles = [x for x in allFiles if ".jpg" in x]
allFiles = [x for x in allFiles if not x in processedPics]

# image must be cropped to be read well with tesseract
crop_4_pay = [(400, 2260, 1050, 2460), (400, 2260, 1050, 2385), (400, 2270, 900, 2490)]
crop_4_miles = [(40, 2125, 600, 2200), (700, 2390, 1050, 2475)]

processed_count = 0

for pic in allFiles:
    processed_count += 1
    print(pic)

    # get the pay
    cropped_pic = Image.open(pic).crop(crop_4_pay[0])
    pic_pay = pytesseract.image_to_string(cropped_pic, config='--psm 7').split('\n')
    pic_pay = pic_pay[0]

    if '$' not in pic_pay:
        # the first crop setting failed because of different format in pic
        # rerun cropping with different setting
        cropped_pic = Image.open(pic).crop(crop_4_pay[1])
        pic_pay = pytesseract.image_to_string(cropped_pic, config='--psm 11').split('\n')
        pic_pay = pic_pay[0]

    if '$' not in pic_pay:
        # the first crop setting failed because of different format in pic
        # rerun cropping with different setting
        cropped_pic = Image.open(pic).crop(crop_4_pay[2])
        pic_pay = pytesseract.image_to_string(cropped_pic, config='--psm 13').split('\n')
        pic_pay = pic_pay[0]

    #cleaning the data
    for bad_char in bad_char_list:
        pic_pay = pic_pay.replace(bad_char, '')
    for c in pic_pay:
        if c.isalpha():
            pic_pay = '!!Error!!'
            break
    pic_pay = pic_pay.strip()
    print(pic_pay)

    #get the mileage
    cropped_pic = Image.open(pic).crop(crop_4_miles[0])
    pic_miles = pytesseract.image_to_string(cropped_pic, config='--psm 6')
    pic_miles = re.split("[{0-9} ]*(item)s?|-?[0-9]?\.?[0-9]*(mi)", pic_miles)
    if len(pic_miles) < 4:
        # the first crop setting failed because of different format in pic
        # rerun cropping with different setting
        cropped_pic = Image.open(pic).crop(crop_4_miles[1])
        pic_miles = pytesseract.image_to_string(cropped_pic, config='--psm 6').split()

    #cleaning the data
    #extract the element with the mileage
    for element in pic_miles:
        if element is None:
            continue
        #filter out non-numbers
        if (bool(re.match(".?\d\.?\d*", element.strip()))):
            for bad_char in bad_char_list:
                element = element.replace(bad_char, '')
            pic_miles = element.strip()

    for element in pic_miles:
        if element is None:
            continue
        if element.isalpha():
            pic_miles = '!!Error!!'
    print(pic_miles)

    pic_creation = dt.strptime(pic[11:-11], '%Y%m%d-%H%M%S')
    # print(f'{pic}\t{pic_creation}\t{pic_pay}\t{pic_miles}\t{config}\n')
    f.write(f'{pic}\t{pic_creation}\t{pic_pay}\t{pic_miles}\n')
f.close()
print(f'It took {round(time.time()-timestart)} seconds to process {processed_count} pictures.')
