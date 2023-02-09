<?php
    error_reporting(0);
    $file = isset($_GET['page']) ? $_GET['page'] : NULL;
    include("header.php");
    if(isset($file))
    {
        include($file);
    }
    else
    {
        include("./home.php");
    }
    include("footer.php");
?>