# Import the necessary libraries
import face_recognition
from PIL import Image, ImageDraw

# Load the image file

import face_recognition
from PIL import Image, ImageDraw

# Load the image file
image = face_recognition.load_image_file("./db/245122733179_fsdf.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

# Open the image file
pil_image = Image.fromarray(image)

# Create a ImageDraw object
draw = ImageDraw.Draw(pil_image)

# Iterate over the face locations and draw a rectangle around each face
for face_location in face_locations:
    top, right, bottom, left = face_location
    draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0), width=3)

# Display the image
pil_image.show()

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

# Open the image file
pil_image = Image.fromarray(image)

# Create a ImageDraw object
draw = ImageDraw.Draw(pil_image)

# Iterate over the face locations and draw a rectangle around each face
for face_location in face_locations:
    top, right, bottom, left = face_location
    draw.rectangle(((left, top), (right, bottom)), outline=(255,0,0), width=3)

# Display the image
pil_image.show()
