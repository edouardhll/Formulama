import easyocr
#import pillow
#resize()
reader = easyocr.Reader(['fr','en'])
result = reader.readtext('lectureDocument/carteIdentite.jpg')
result2= reader.readtext('lectureDocument/carteIdentite2.jpg')

# #============== ORDRE INFOS ==============#

# # COIN HAUT GAUCHE 
# # COIN HAUT DROIT
# # COIN BAS DROIT
# # COIN BAS GAUCHE

#for i in range(len(result)):
#     print(result[i][1])
#print(f'CNI 1 {len(result)}')
      
for i in range(len(result2)):
     print(result2[i][1])
#print(f'CNI2 {len((result))}')


cni = {"nom": result2[5][1],
       "prenom": result2[8][1],
       "sexe": result2[16][1],
       "nationnalite": result2[14][1],
       "dateNaissance": result2[17][1],
       "lieuNaissance": result2[19][1],
       }


if result2[9][1] != "SEXE / Sex":
     cni["prenom"]+= " "+result2[9][1]

if result2[10][1] != "SEXE / Sex":
     cni["prenom"]+= " "+result2[10][1]

print(f'CNI2 {(cni)}')



with open('lectureDocument/cni.txt', 'w', encoding='utf-8') as f:
    f.write(str(result))


#CHERCHER SI ON PEUT FILTRER PAR TYPO
#IMPRIMER PLUSIEURS CNI POUR LES PRENDRE EN PHOTO AVEC DES ECLAIRAGES DIFFERENTS

#RÉPUBLIQUE FRANÇAISE
# FR
# CARTE NATIONALE D'IDENTITÉ
# IDENTITY CARD
# NOM /Sumname
# CHEVALLIER
# Prenoms / Given names
# Gisèle , Audrey
# SEXE /Sex
# NATIONALITE
# Nationality
# DATE DE NAISS
# Dale ofbrth
# E
# FRA
# 01 04 1995
# LIEU DE NAISSANCE
# Place of birth
# BORDEAUX
# NOM D'USAGE / Altemate name
# vve
# DUBOIS
# N' DU DOCUMENT / Document No
# DATED'EXPIR
# Expiry dale
# T7X62Tz79
# 27 01 2031
# JignAture
# 240220
# RECETIE

