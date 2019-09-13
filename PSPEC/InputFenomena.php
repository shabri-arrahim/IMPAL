<?php
if (isset($_POST['tombol'])) {
    $Judul = $_POST['Judul Fenomena'];
    $tglmulai = $_POST['Tanggal Mulai Fenomena'];
    $tglberakhir = $_POST['Tanggal Berakhir Fenomena'];
    
    $ekstensi_diperbolehkan = array('png','jpg','jpeg','JPG','JPEG');
        $judul $_FILES['foto']['name'];
        $x = explode('.', $nama);
        $ekstensi = strtolower(end($x));
        $file_tmp = $_FILES['foto']['tmp_name'];  
        $nama_baru = "Fenomena".rand(100,1000).".".$ekstensi;
   
        if(in_array($ekstensi, $ekstensi_diperbolehkan) === true){  
            move_uploaded_file($file_tmp, 'assets/images/Fenomena/'.$nama_baru);
              mysqli_query($con, "INSERT INTO `fenomena`('judul_fenomena', 'tgl_mulai_fenomena', 'tgl_berakhir_fenomena') VALUES ('$Judul','$tglmulai','$tglmulai','$nama_baru','$_SESSION[id_pengguna]')");
           

            echo "<script> alert('Fenomena Ditambahkan'); document.location='InputFenomena.php'; </script>";
          
        }
        else{
            echo "<div class='box-body'>
                <div class='alert alert-danger alert-dismissible'>
                  <button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;</button>
                  <h4><i class='icon fa fa-ban'></i>Gagal</h4>
                  File gambar tidak valid. Penyimpanan dibatalkan!
                </div>
              </div>";
        }
}
