<?php    
   include("koneksi.php");

   $id_identitas = $_GET['id_identitas'];

   $query = "delete from identitas where id_identitas = $id_identitas";
   
   if(mysqli_query($koneksi, $query)){
       header("Location: index.php");
   }else{
       header("Location: edit.php?id_identitas=$id_identitas");
   }

?>