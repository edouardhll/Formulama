from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import whitesmoke
import json

c = canvas.Canvas("cerfa_14011-02.pdf", pagesize=A4) #créer l'objet canvas avec son nom et sa taille

with open('bdd.json', 'r') as f:
    data = json.load(f)

page_width, page_height = A4 #mets les valeurs du format A4 dans les deux variables pour les utiliser plus tard

c.drawImage(# image cerfa d'arrière plan
    "cerfaimage.jpg",#nom du fichier d'où vient l'arrière plan
    0, 0,#position de l'image, comme elle fait la taille de la page on la place à l'origine.
    width=page_width,#donne à la largeur de l'image la largeur de la page
    height=page_height#donne à la hauteur de l'image la hauteur de la page
)

#----------------------------------------------------------------------------------------------------------------------------------------------
#DOMICILE
#----------------------------------------------------------------------------------------------------------------------------------------------

nom_valeur = data.get('nom', '') #récupère la valeur associé à la clé 'nom'
c.acroForm.textfield(#acroForm permet de créer des champs
    name="nom",#clé
    x=144,#position horizontale
    y=638, #position verticale
    width=150,#largeur du champ
    height=17,#hauteur du champ
    value=nom_valeur,#valeur
    borderStyle='underlined',#style de la bordure = souligné
    forceBorder=True, # force l'affichage de la bordure du champ
    fillColor=whitesmoke
)

nomUsage_valeur = data.get('nomUsage', '')
c.acroForm.textfield(
    name="nomUsage",
    x=135,
    y=610,
    width=150,
    height=17,
    value=nomUsage_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

prenom_valeur = data.get('prenom', '')
c.acroForm.textfield(
    name="prenom",
    x=124,
    y=585,
    width=300,
    height=17,
    value=prenom_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

dateNaissance_valeur = data.get('dateNaissance', '')
c.acroForm.textfield(
    name="dateNaissance",
    x=107,
    y=560,
    width=110,
    height=15,
    value=dateNaissance_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

communeNaissance_valeur = data.get('communeNaissance', '')
c.acroForm.textfield(
    name="communeNaissance",
    x=280,
    y=560,
    width=250,
    height=17,
    value=communeNaissance_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

codePostalNaissance_valeur = data.get('codePostalNaissance', '')
c.acroForm.textfield(
    name="codePostalNaissance",
    x=125,
    y=542,
    width=80,
    height=17,
    value=codePostalNaissance_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

paysNaissance_valeur = data.get('paysNaissance', '')
c.acroForm.textfield(
    name="paysNaissance",
    x=245,
    y=542,
    width=285,
    height=17,
    value=paysNaissance_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

numeroAdresse_valeur = data.get('numeroAdresse', '')
c.acroForm.textfield(
    name="numeroAdresse",
    x=115,
    y=500,
    width=75,
    height=17,
    value=numeroAdresse_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

typeVoieAdresse_valeur = data.get('typeVoieAdresse', '')
c.acroForm.textfield(
    name="typeVoieAdresse",
    x=200,
    y=500,
    width=75,
    height=17,
    value=typeVoieAdresse_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

nomVoieAdresse_valeur = data.get('nomVoieAdresse', '')
c.acroForm.textfield(
    name="nomVoieAdresse",
    x=300,
    y=500,
    width=220,
    height=17,
    value=nomVoieAdresse_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

codePostal_valeur = data.get('codePostal', '')
c.acroForm.textfield(
    name="codePostal",
    x=130,
    y=475,
    width=60,
    height=17,
    value=codePostal_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

commune_valeur = data.get('commune', '')
c.acroForm.textfield(
    name="commune",
    x=280,
    y=475,
    width=225,
    height=17,
    value=commune_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

pays_valeur = data.get('pays', '')
c.acroForm.textfield(
    name="pays",
    x=110,
    y=455,
    width=375,
    height=17,
    value=pays_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)





#----------------------------------------------------------------------------------------------------------------------------------------------
#CNI
#----------------------------------------------------------------------------------------------------------------------------------------------

perteIdentite_valeur = (data.get('perteIdentite', 'false').lower() == 'cni')
print(perteIdentite_valeur)
if perteIdentite_valeur == True:
    print("CNI")
    c.acroForm.checkbox(
        name="perteIdentite",
        x=340,
        y=774,
        size=13,
        checked=perteIdentite_valeur,
        fillColor=whitesmoke
    )

    documentNumero_valeur = data.get('documentNumero', '')
    c.acroForm.textfield(
        name='documentNumero',
        x=124,
        y=386,
        width=135,
        height=17,
        value=documentNumero_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )
    documentDate_valeur = data.get('documentDate', '')
    c.acroForm.textfield(
        name='documentDate',
        x=121,
        y=365,
        width=135,
        height=17,
        value=documentDate_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    c.acroForm.textfield(
        name='titulaire',
        x=75,
        y=325,
        width=210,
        height=17,
        value= nom_valeur+" "+prenom_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    delivrePar_valeur = data.get('delivrePar', '')
    c.acroForm.textfield(
        name='delivrePar',
        x=90,
        y=280,
        width=150,
        height=17,
        value=delivrePar_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    c.acroForm.textfield(
        name='cniPays',
        x=95,
        y=255,
        width=135,
        height=17,
        value=pays_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

#----------------------------------------------------------------------------------------------------------------------------------------------
#PASSEPORT
#----------------------------------------------------------------------------------------------------------------------------------------------

else:

    print("PASSEPORT")

    pertePasseport_valeur = (data.get('perteIdentite', 'false').lower() == 'passeport')
    c.acroForm.checkbox(
        name="pertePasseport",
        x=460,
        y=774,
        size=13,
        checked=pertePasseport_valeur,
        fillColor=whitesmoke
    )

    documentNumero_valeur = data.get('documentNumero', '')
    c.acroForm.textfield(
        name='documentNumero',
        x=375,
        y=386,
        width=135,
        height=17,
        value=documentNumero_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    documentDate_valeur = data.get('documentDate', '')
    c.acroForm.textfield(
        name='documentDate',
        x=362,
        y=365,
        width=135,
        height=17,
        value=documentDate_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    c.acroForm.textfield(
        name='titulaire',
        x=310,
        y=325,
        width=210,
        height=17,
        value= nom_valeur+" "+prenom_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    delivrePar_valeur = data.get('delivrePar', '')
    c.acroForm.textfield(
        name='delivrePar',
        x=330,
        y=280,
        width=200,
        height=17,
        value=delivrePar_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

    c.acroForm.textfield(
        name='passeportPays',
        x=333,
        y=255,
        width=135,
        height=17,
        value=pays_valeur,
        borderStyle='underlined',
        forceBorder=True,
        fillColor=whitesmoke
    )

#----------------------------------------------------------------------------------------------------------------------------------------------
#ELEMENTS SUR LA DISPARITION DU OU DES TITRES
#----------------------------------------------------------------------------------------------------------------------------------------------

datePerte_valeur = data.get('datePerte', '')
c.acroForm.textfield(
    name="datePerte",
    x=93,
    y=200,
    width=100,
    height=17,
    value=datePerte_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

lieuPerte_valeur = data.get('lieuPerte', '')
c.acroForm.textfield(
    name="lieuPerte",
    x=253,
    y=200,
    width=275,
    height=17,
    value=lieuPerte_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

circonstancesPerte_valeur = data.get('circonstancesPerte', '')
c.acroForm.textfield(
    name="circonstancesPerte",
    x=180,
    y=180,
    width=330,
    height=17,
    value=circonstancesPerte_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

c.acroForm.textfield(
    name="villeCreation",
    x=95,
    y=133,
    width=150,
    height=17,
    value=commune_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

date_valeur = data.get('date', '')
c.acroForm.textfield(
    name="date",
    x=280,
    y=133,
    width=100,
    height=17,
    value=date_valeur,
    borderStyle='underlined',
    forceBorder=True,
    fillColor=whitesmoke
)

#----------------------------------------------------------------------------------------------------------------------------------------------
#CHAMPS À COCHER
#----------------------------------------------------------------------------------------------------------------------------------------------





majeur_valeur = (data.get('majeur', 'false').lower() == 'true')
c.acroForm.checkbox(
    name="majeur",
    x=263.3,
    y=696.4,
    size=13,
    checked=majeur_valeur,
    fillColor=whitesmoke
)

mineur_valeur = (data.get('majeur', 'false').lower() == 'false')
c.acroForm.checkbox(
    name="mineur",
    x=450.9,
    y=696.4,
    size=13,
    checked=mineur_valeur,
    fillColor=whitesmoke
)

homme_valeur = (data.get('homme', 'false').lower() == 'homme')
c.acroForm.checkbox(
    name="homme",
    x=225.95,
    y=658.2,
    size=13,
    checked=homme_valeur,
    fillColor=whitesmoke
)

femme_valeur = (data.get('femme', 'false').lower() == 'true')
c.acroForm.checkbox(
    name="femme",
    x=305.95,
    y=658.2,
    size=13,
    checked=femme_valeur,
    fillColor=whitesmoke
)

c.save()#sauvegarde le pdf