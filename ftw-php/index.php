<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);  

require_once "router.php";

// function checking status of transfer
function checkTransfer($idTrans) {
    $headers = array("Authorization: Bearer XXXXX");
    $ch = curl_init(); 
    curl_setopt($ch, CURLOPT_URL, "https://api.flutterwave.com/v3/transfers/".$idTrans); 
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, false);   
    $output = curl_exec($ch); 
    curl_close($ch);
}

// function for initiating transfer
function makeTransfer($requestBody) {
    $headers = array("Authorization: Bearer XXXXX","Content-Type: application/json");
    $ch = curl_init(); 
    curl_setopt($ch, CURLOPT_URL, "https://api.flutterwave.com/v3/transfers"); 
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, false);   
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $requestBody);
    $output = curl_exec($ch); 
    curl_close($ch);
}

// route for initiating transfer
route('/initiateTransfer', function () {
    $requestBody = file_get_contents('php://input');
    makeTransfer($requestBody);
});
// route for checking status of transfer
route('/checkStatus/(.+)/?', function ($idTrans) {
    checkTransfer($idTrans);
});

$action = $_SERVER['REQUEST_URI'];
dispatch($action);