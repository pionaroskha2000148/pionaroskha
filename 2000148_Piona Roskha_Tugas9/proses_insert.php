<?php

    include("koneksi.php");

    $nama = $_POST['nama'];
    $alamat = $_POST['alamat'];
    $id_user = $_POST['id_user'];
    $jenis_kelamin = $_POST['jenis_kelamin'];
    $jurusan = $_POST['jurusan'];

    $query = "insert into identitas values ('', '$nama', '$alamat', $id_user, '$jenis_kelamin', '$jurusan')";
    
    if(mysqli_query($koneksi, $query)){
        header("Location: index.php");
    }else{
        header("Location: edit.php?id_identitas=$id_identitas");
    }

?>