<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Secure Vault </title>
</head>

<body >
<center><div style=" margin-top:20px;color:#000; font-size:30px; text-align:center"> Welcome To Secure Vault&nbsp;&nbsp;</center><br></div>


<div style="padding-top:10px; font-size:15px;">
 


</div></div>

<div style=" margin-top:10px;color:#FFF; font-size:23px; text-align:center">
<font size="6" color="#000000">
    <head>
        <h1>
            <form method="post" autocomplete="off">
                <center>
                <label for="username" >Username</label>
                <input type="text" name="username" required="" /><br>
                <label for="password" >Password</label>
                <input type="password" name="password"  required="" /><br><br>
                <input type="submit" /></center>
            </form>
        </h1>
    </head>


<?php
if(isset($_POST['username']) && isset($_POST['password'] )){
    $conn = new mysqli('127.0.0.1','root','root','webpage');
    if($conn->connect_error){
        die("connection error". $conn->connect_error);}
$username = $_POST['username'];
$password = $_POST['password'];
$s = " select username,password from users where username= '$username' and password= '$password' ";
$d= $conn->query($s);
$e=$d->fetch_assoc();
if($e){
          echo "You have succesfully logged in";
          echo "<br>";
          echo "<!-- Your Login name: ".$e['username']. "-->" ;
          echo "<br>";
          echo "<!-- Your Login password: ".$e['password']. "-->" ;
          echo "<br>";
      }
else{
          print_r(error_get_last());
          echo "<br>";
          echo "<br>";
          echo "Try again U noobie hacker !!! ";
}

    } 
?>

</font>
</div>
</body>
</html>