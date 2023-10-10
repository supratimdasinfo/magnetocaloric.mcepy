<?php
    $db_host = getenv('DB_HOST');
    $db_user = getenv('DB_USER');
    $db_pass = getenv('DB_PASS');
    $db_name = getenv('DB_NAME');

    //Hiding Sensitive Information of Database Connection

    $con = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
    if (!$con) {
    ?>
        <script type="text/javascript">
            alert('Error Found')
        </script>
    <?php
    
    }else {
        $email = $_POST["email"];
        $password = $_POST["password"];
        $end_date = $_POST["date"];
        $ac = "SELECT * FROM `mceaccess` WHERE email = '$email' && password = '$password'";
        $timestampdb = date("Y-m-d H:i:s");
        $result = mysqli_query($con, $ac);
        $num = mysqli_num_rows($result);
        if ($num >= 1){
            $key_nd_dif = generateActivationKey($end_date);
            $activationKeys = $key_nd_dif[0][0] . ", " . $key_nd_dif[0][1];
            $num_day = $key_nd_dif[1];
            $status = "Key Generated Successfully!";
            $rec = "INSERT INTO `mceaccessrec`(`email`, `validity`, `date`, `status`) VALUES ('$email', '$num_day', '$timestampdb', '$status')";
            $str = mysqli_query($con, $rec);
            echo '<div class="confirmation">
              <p>Activation Key Generated Successfully!</p>
              <span class="tick-mark">&#9996;</span>
              <p>Activation Keys : <span>' . $activationKeys . '</span></p>
          </div><style>.confirmation {position: absolute; top: 50%; left: 50%;transform: translate(-50%, -50%); width: 50%; margin: auto; text-align: center;background-color: #f2f2f2;border: 1px solid #ccc;padding: 20px;border-radius: 10px;} .tick-mark {font-size: 36px;color: #00a300;}</style>';
        }else{
            $key_nd_dif = generateActivationKey($end_date);
            $num_day = $key_nd_dif[1];
            $status = "Authentication failed!";
            $rec = "INSERT INTO `mceaccessrec`(`email`, `validity`, `date`, `status`) VALUES ('$email', '$num_day', '$timestampdb', '$status')";
            $str = mysqli_query($con, $rec);
            echo '<div class="confirmation">
              <p>Authentication failed!</p>
              <span class="tick-mark">&#128546;</span>
              </div><style>.confirmation {position: absolute; top: 50%; left: 50%;transform: translate(-50%, -50%); width: 50%; margin: auto; text-align: center;background-color: #f2f2f2;border: 1px solid #ccc;padding: 20px;border-radius: 10px;} .tick-mark {font-size: 36px;color: red;}</style>';
        }      
    }
    function generateActivationKey($end_date) {

        //Concealing the Activation Key Generation Process

    }

?>