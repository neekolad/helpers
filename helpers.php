<?php
// this is the collection of helper functions for php scripts

function techo($str)
{
    echo "[" .date("d-m-Y H:i:s") . "] " . rtrim($str) . "\n";
}

?>