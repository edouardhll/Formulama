import easyocr
reader = easyocr.Reader(['fr','en'])
result = reader.readtext('lectureDocument/carteIdentite.jpg')
# result2= reader.readtext('lectureDocument/carteIdentite2.jpg')

# #============== ORDRE INFOS ==============#

# # COIN HAUT GAUCHE 
# # COIN HAUT DROIT
# # COIN BAS DROIT
# # COIN BAS GAUCHE

for i in range(len(result)):
     print(result[i][1])
print(result)


with open('lectureDocument/cni.txt', 'w', encoding='utf-8') as f:
    f.write(str(result))