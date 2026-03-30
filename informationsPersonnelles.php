<?php

echo "<pre>";
$BDD = json_encode($_POST);

$dataToJSON = $_POST;
$dataToJSON['date'] = date('d/m/Y');

print_r($dataToJSON);
echo "</pre>";
// $fichier = fopen('bdd_'.date('Ymd').'.json', 'w+');
$fichier = fopen('bdd.json', 'w');
fwrite($fichier, $BDD);
?>