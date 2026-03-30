import easyocr
reader = easyocr.Reader(['fr','en'])
result = reader.readtext('lectureDocument/carteIdentite.jpg')
print(result)