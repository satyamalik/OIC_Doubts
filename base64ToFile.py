# Import only b64decode function from the base64 module
from base64 import b64decode

#pre-requisite: Python must be installed on your PC

# create a text file by any name, lets say file.txt #and put the base64 text there. it might appear in a #single line and thats ok
#put the file at same location as this python #executable file
# In line 27 below change the name to whatever you #like, in this example its called BinaryFile.zip

# Please note: this file is not tested, but it should # work without major changes

b64 = """"""
with open('file.txt', 'rb') as binary_file:
    b64 = binary_file.read()


# Decode the Base64 string, making sure that it contains only valid characters
bytes = b64decode(b64, validate=False)

# Perform a basic validation to make sure that the result is a valid PDF file
# Be aware! The magic number (file signature) is not 100% reliable solution to validate PDF files
# Moreover, if you get Base64 from an untrusted source, you must sanitize the PDF contents
#if bytes[0:4] != b'%PDF':
#  raise ValueError('Missing the PDF file signature')

# Write the PDF contents to a local file
f = open('BinaryFile.zip', 'wb')
f.write(bytes)
f.close()