<?php

require_once("config.php");

if(isset($_POST['register'])){

    // filter data yang diinputkan
    $namapengguna = filter_input(INPUT_POST, 'namapengguna', FILTER_SANITIZE_STRING);
    $nohp = filter_input(INPUT_POST, 'nohp', FILTER_SANITIZE_STRING);
    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
    // enkripsi password
    $password = password_hash($_POST["password"], PASSWORD_DEFAULT);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);


    // menyiapkan query
    $sql = "INSERT INTO pengguna (nama_pengguna,email,no_hp_pengguna) 
            VALUES (:namapengguna,:email,:nohp)";
    $sql = "INSERT INTO akun (username,password) 
            VALUES (:username,:password)";
    
    $stmt = $db->prepare($sql);

    // bind parameter ke query
    $params = array(
        ":namapengguna" => $namapengguna,
        ":username" => $username,
        ":password" => $password,
        ":email" => $email
        ":nohp" => $nohp
    );

    // eksekusi query untuk menyimpan ke database
    $saved = $stmt->execute($params);

    // jika query simpan berhasil, maka user sudah terdaftar
    // maka alihkan ke halaman login
    if($saved) header("Location: login.php");
}