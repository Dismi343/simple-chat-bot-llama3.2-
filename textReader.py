#from PIL import Image
import pytesseract
import cv2
# import ollama
import numpy as np

image_name = str(input("Enter image name.exe: "))
image=cv2.imread(image_name)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

kernel = np.ones((1, 1), np.uint8)
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
gray = cv2.fastNlMeansDenoising(gray, h=30)
text = pytesseract.image_to_string(gray)
print(text)


# response = ollama.chat(model='llama3.2:1b', messages=[
#         {'role': 'user', 'content': text}
#     ])

# print(response['message']['content'])

#print(pytesseract.image_to_string(Image.open(image_name)))