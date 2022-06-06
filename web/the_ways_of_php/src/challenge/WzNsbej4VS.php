<?php 
    $FLAG = 'n00bz{D0nt_c0mb1n3_wh4t5_n0t_m34nt_t0_b3_c0mb1n3d}';
    $rp = 'idnthaveanypassword';
    $key = 'GamingChair';
    $hash_function = "sha256";

    if (isset($_POST['u']) && isset($_POST['p'])){
        if (md5($_POST['u']) === '21232f297a57a5a743894a0e4a801fc3'){
            $hash = password_hash(hash_hmac("sha256", $rp, $key, true), PASSWORD_BCRYPT);

            if(password_verify(hash_hmac("sha256", $_POST['p'], $key, true), $hash)){
                print $FLAG;
                exit;
            }
        }
        $msg = 'Incorrect!';
    }
?>
<!DOCTYPE html>
<html lang="en">
 
<head>
<!-- Required meta tags -->
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,
    initial-scale=1, shrink-to-fit=no" />

<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous" />
<link href="https://fonts.googleapis.com/css2?family=Inconsolata&display=swap" rel="stylesheet"> 
<style>
    body {
        font-family: "Inconsolata", monospace;
    }
    h1 {
    font-size: 5rem !important;
    }
</style>
</head><body>

<div class="container">
    <div class="text-center jumbotron">
        <h1>Login</h1>
        <h3>Be careful - only 1 request every 15 seconds!</h3>
        <h6>(For anti bruteforcing)</h6>
        <form method="POST">
            <div class="form-group row justify-content-center">
                <div class="">
                    <input type="username" class="form-control form-control-lg" placeholder="Username" name="u">
                </div>
            </div>
            <div class="form-group row justify-content-center">
                <div class="">
                    <input type="password" class="form-control form-control-lg" placeholder="Password" name="p">
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        <br>
        <h5> <?php if (isset($msg)){ print $msg; $msg = ''; } ?> </h5>
    </div>
</div>
</body>