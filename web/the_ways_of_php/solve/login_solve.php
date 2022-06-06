<?php
$key = 'GamingChair';
$hash_function = "sha256";
$found = [];
$end = fopen('res.txt', 'w');
if ($file = fopen('/usr/share/wordlists/rockyou.txt', 'r')){
    while(!feof($file)) {
        $pw = trim(fgets($file));
        $hash = hash_hmac($hash_function, $pw, $key, true);
        if ($hash[0] === "\0") {
            $found[] = $pw;
        }
    }
    foreach ($found as $f){
        fwrite($end, $f . "\n");
    }
}
fclose($file);
fclose($end);
?>
