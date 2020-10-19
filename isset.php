<?php

$emptyString = '';

if (isset($emptyString)) {
	echo "This var is set so I will print."; // True
}

$null = null;

if (isset($null)) {
	echo "This var i null so no print";
}

?>