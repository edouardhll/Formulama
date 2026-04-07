<!DOCTYPE html>
<head>
    <title>Formulama</title>
    <meta charset="UTF-8">
</head>
<body>
    <form action="informationsPersonnelles.php" method="post">


<!-- déclarant -->

    <div class="champFormulaire">
        <label>Nom (acte de naissance)</label>
        <input id="nom" type="text" value="<?php echo $_POST['nom']?>" placeholder="Dupont" name="nom">
    </div>

    <div class="champFormulaire">
        <label>Nom de famille</label>
        <input id="nomUsage" type="text" value="" placeholder= "Dupont" name="nomUsage">
    </div>

    <div class="champFormulaire">
        <label>Prénom</label>
        <input id="prenom" type="text" value="" placeholder= "Jean" name="prenom">
    </div>

    <div class="champFormulaire">
        <label>Date de naissance</label>
        <input id="dateNaissance" type="date" value="" placeholder= "Date de naissance" name="dateNaissance">
    </div>

<!-- RAJOUTER LE GENRE AVEC BALISE OPTION -->
    <div class="champFormulaire">
        <label>Civilité</label>
        <select class="champFormulaire" id="sexe" name="sexe">
            <option value="" disabled selected>Sélectionner</option>
            <option>Homme</option>
            <option>Femme</option>
        </select>
    </div>

    <div class="champFormulaire">
        <label>Commune ou ville de naissance</label>
        <input id="communeNaissance" type="text" value="" placeholder= "Nantes" name="communeNaissance">
    </div>

    <div class="champFormulaire">
        <label>Code postal de la ville de naissance</label>
        <input id="codePostalNaissance" type="text" value="" placeholder= "44200" name="codePostalNaissance">
    </div>

    <div class="champFormulaire">
        <label>Pays de naissance</label>
        <input id="paysNaissance" type="text" value="" placeholder= "France" name="paysNaissance">
    </div>


<!-- DOMICILE -->

    <div class="champFormulaire">
        <label>Numéro de votre adresse</label>
        <input id="numeroAdresse" type="text" value="" placeholder= "12" name="numeroAdresse">
    </div>

    <div class="champFormulaire">
        <label>Type de voie</label>
        <select class="champFormulaire" id="typeVoieAdresse" name="typeVoieAdresse">
            <option value="" disabled selected>Sélectionner</option>
            <option>Rue</option>
            <option>Avenue</option>
            <option>Boulevard</option>
            <option>Allée</option>
            <option>Impasse</option>
            <option>Place</option>
            <option>Chemin</option>
            <option>Route</option>
        </select>
    </div>

    <div class="champFormulaire">
        <label>Nom de la voie</label>
        <input id="nomVoieAdresse" type="text" value="" placeholder= "Nom de la voie" name="nomVoieAdresse">
    </div>

    <div class="champFormulaire">
        <label>Code postal</label>
        <input id="codePostal" type="text" value="" placeholder= "Code postal" name="codePostal">
    </div>

    <div class="champFormulaire">
        <label>Ville / Commune</label>
        <input id="commune" type="text" value="" placeholder= "Votre ville ou commune" name="commune">
    </div>

    <div class="champFormulaire">
        <label>Pays</label>
        <input id="pays" type="text" value="" placeholder= "Votre Pays" name="pays">
    </div>

<!-- CARACTERISTIQUE DU TITRE -->

    <div class="champFormulaire">
        <label>CNI / Passeport</label>
        <select class="champFormulaire" id="perteIdentite" name="perteIdentite">
            <option value="" disabled selected>Sélectionner</option>
            <option>CNI</option>
            <option>Passeport</option>
        </select>
    </div>

    <div class="champFormulaire">
        <label>N° document</label>
        <input id="documentNumero" type="text" value="" placeholder= "T7X62TZ79" name="documentNumero">
    </div>

    <div class="champFormulaire">
        <label>Date de délivrance</label>
        <input id="documentDate" type="date" placeholder= "" name="documentDate">
    </div>


<!-- CIRCONSTANCES DE LA PERTE -->

    <div class="champFormulaire">
        <label>Date de perte</label>
        <input id="datePerte" type="date" name="datePerte">
    </div>

    <div class="champFormulaire">
        <label>Lieu de perte</label>
        <input id="lieuPerte" type="text" placeholder="Gare de nantes" name="lieuPerte">
    </div>

    <div class="champFormulaire">
        <label>Circonstances de la perte</label>
        <input id="circonstancesPerte" type="text" value="" placeholder= "Mon sac est resté ouvert..." name="circonstancesPerte">
    </div>

    <div class="champFormulaire">
        <label>Délivré par</label>
        <input id="delivrePar" type="text" value="" placeholder= "Préfecture de la Loire-Atlantique" name="delivrePar">
    </div>

        <input type="submit">
        <input type="reset">
    </form>
</body>