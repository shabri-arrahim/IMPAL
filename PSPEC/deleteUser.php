<?php 
  include 'header.php';
  if (isset($_GET['delete'])) {
    $idu = $_GET['idu'];
    
    mysqli_query($con, "DELETE FROM user WHERE id_user = '$idu'");
    echo "<script> alert('User Terhapus'); document.location='akun.php'; </script>";
  }
 ?>
