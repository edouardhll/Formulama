<?php

echo "<pre>";

$dataToJSON = $_POST;
$dataToJSON['date'] = date('d/m/Y');

$dataToJSON['documentDate'] = date_create_from_format('Y-m-d', $dataToJSON['documentDate'])->format("d/m/Y");
$dataToJSON['dateNaissance'] = date_create_from_format('Y-m-d', $dataToJSON['dateNaissance'])->format("d/m/Y");
$dataToJSON['datePerte'] = date_create_from_format('Y-m-d', $dataToJSON['datePerte'])->format("d/m/Y");

print_r($dataToJSON);
$BDD = json_encode($dataToJSON);
echo "</pre>";

$fichier = fopen('bdd.json', 'w');
fwrite($fichier, $BDD);
?>