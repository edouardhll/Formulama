<?php

echo "<pre>";
$BDD = json_encode($_POST);

$dataToJSON = $_POST;
$dataToJSON['date'] = date('d/m/Y');
$documentDate = $dataToJSON['documentDate'];
$documentDate = date_create_from_format('Y-m-d', $documentDate)->format("d/m/Y");
echo $documentDate;
print_r($dataToJSON);
echo "</pre>";
// $fichier = fopen('bdd_'.date('Ymd').'.json', 'w+');
$fichier = fopen('bdd.json', 'w');
fwrite($fichier, $BDD);
?>