<?php
    session_start();

    if (isset($_REQUEST['f'])) {
        $c = $_REQUEST['f'];
        try {
        foreach (new DirectoryIterator($c) as $f) echo $f->getSize() . "\r";
        } catch (Exception $e) {
            include 'A4UqCitMd2.html';
        }
        exit;
    }

    highlight_string("<?php
    if (isset(\$_REQUEST['f'])) {
        \$c = \$_REQUEST['f'];
        try {
        foreach (new DirectoryIterator(\$c) as \$f) echo \$f->getSize() . '\\r';
        } catch (Exception \$e) {
            include 'A4UqCitMd2.html';
        }
        exit;
    }
?>");
?>