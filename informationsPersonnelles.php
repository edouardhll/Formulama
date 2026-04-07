<?php

function diffDate($a, $b) {
    $a = date_create_from_format('d/m/Y', $a);
    $b = date_create_from_format('d/m/Y', $b);
    $interval = $a->diff($b);
    $interval = $interval->format("%y");
    return $interval;
}

echo "<pre>";

$dataToJSON = $_POST;
$dataToJSON['date'] = date('d/m/Y');
$dataToJSON['documentDate'] = date_create_from_format('Y-m-d', $dataToJSON['documentDate'])->format("d/m/Y");
$dataToJSON['dateNaissance'] = date_create_from_format('Y-m-d', $dataToJSON['dateNaissance'])->format("d/m/Y");
$dataToJSON['datePerte'] = date_create_from_format('Y-m-d', $dataToJSON['datePerte'])->format("d/m/Y");


$age = diffDate($dataToJSON['dateNaissance'], $dataToJSON['date']);

if ($age > 17)
    {
        $dataToJSON['majeur'] = "True";
        }
        else {
            $dataToJSON['majeur'] = "False";
            }
            
print_r($dataToJSON);
$BDD = json_encode($dataToJSON);
echo "</pre>";
            
$fichier = fopen('bdd.json', 'w');
fwrite($fichier, $BDD);
?>