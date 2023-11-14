<?php
    error_reporting(0);
    $file = isset($_GET['page']) ? $_GET['page'] : NULL;
    include("header.php");
    if(isset($file))
    {
        $file = $file.".php";
        $file = substr($file,0,strpos($file,"\0"));
        include($file);
    }
    else
    {
        include("./home.php");
    }
    include("footer.php");
?>
