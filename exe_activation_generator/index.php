<?php
//$con = mysqli_connect('localhost', 'id21136245_supratim0707','#SUpratim@0707');
//mysqli_select_db($con, 'id21136245_mceactivation');
//$con = mysqli_connect('localhost', 'root','','login');
$con = mysqli_connect('sql201.infinityfree.com', 'if0_34799485','qHVg8EPV8li','if0_34799485_mceactivation');
if (!$con) {
?>
    <script type="text/javascript">
        alert('Error Found')
    </script>
<?php
    }
?>
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-image: url('Scr.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        body::before {
            content: "";
            min-height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8); /* Semi-transparent black overlay */
            z-index: -1; /* Place the overlay behind the content */
        }   
        ::-webkit-scrollbar {
            width: 0px;
        }

        ::-webkit-scrollbar-track {
            background-color: black;
        }

        ::-webkit-scrollbar-thumb {
            background-color: #333; /* Dark gray color */
            border-radius: 6px;
        }

        #container {
            background-color: #d2dae2;
            border-radius: 10px;
            box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
            z-index: 5;

            padding: 35px;
            padding-top: 40px;
            padding-bottom: 40px;
            width: 60%;
            max-width: 400px;
           
            
            box-sizing: border-box;
        }
        #github{
            display: block;
            background-color: #000;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
            width: 40%;
            font-size: 15px;
            max-width: 300px;
            max-height: 530px;
            min-height: 530px;
            border: 4px solid #d2dae2;
            border-right: none;
            padding-top: 0;
            overflow-y: scroll;
            overflow-x: hidden;

        }
        #loghead{
            position: sticky;
            top: 0;
            left: 0;
            background-color: #d2dae2;
            padding: 5px;
            color: #000;

        }
        #log{
            display: block;
            overflow-y: scroll;
            overflow-x: hidden;
            padding: 15px;
            text-align: left;
            color: #fff;           
        }
        #file_link{
            position: sticky;
            bottom: 0;
            left: 0;
            background-color: #d2dae2;
            padding: 5px;
            color: #000;

        }
        h1 {
            margin: 0 0 5x;
            margin-top: 0;
            font-size: 20px;
            text-align: left;
        }       
        h2 {
            margin: 0 0 10px;
            position: relative;
            top: -10px;
            text-align: left;
        }
        #mb{
            display: none;
            margin: auto;
            width: 80%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        button:hover {
            background-color: #0056b3;
        }
        
        link{
            font-size: 15px;

        }
        footer {
            text-align: right;
            background-color: transparent;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 95%;
            margin: auto;
        }
        
        footer p {
            margin: 0;
            font-size: 14px;
            color: #d2dae2;
        }
        .heart {
            color: #d2dae2;
        }

        @media(max-width: 450px){
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-image: none;
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
            }
            #mb{
                display: block;
                margin: auto;
                width: 80%;
                position: absolute;
                color: #d2dae2;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }              

            #container {
                display: none;
                background-color: #d2dae2;
                border-radius: 5px;
                box-shadow: 0 0 0px rgba(0, 0, 0, 0.1);
                padding: 20px;
                padding-top: 40px;
                padding-bottom: 40px;
                width: 90%;
                margin: 5%;
                max-width: 400px;
                min-width: 300px;
                box-sizing: border-box;
            }
            #github{
                display: none;
            }
            footer{
                display: none;
            }
        }

    </style>
    <title>Activation Key Generator</title>
</head>
<body>
    <div id="mb">
        <h3>&#128534 This content is only visible on desktop!</h3>
        <p style="font-size: 10px;">Explore the Magnetocaloric mcepy project on GitHub: <a style="color:#d2dae2;" href="https://github.com/supratimdasinfo/magnetocaloric.mcepy">Magnetocaloric mcepy Repository</a></p>        
    </div>
    
    <div id="github">
        <div id="loghead">
            <p id="audit" style="margin: 0; font-weight: bold;"> &#x274D; audit log</p>

        </div>
        <div id="log">
            <?php
                $sql = "SELECT * FROM mceaccessrec";
                $result = mysqli_query($con, $sql);

                if ($result && mysqli_num_rows($result) > 0) {

                    $data = [];
                    while ($row = mysqli_fetch_assoc($result)) {
                        $data[] = $row;
                    }

                    // Loop through the array in reverse order
                    for ($i = count($data) - 1; $i >= 0; $i--) {
                        echo "--: " . $data[$i]["email"] . " tried to generate a " . $data[$i]["validity"] . " days activation key on " . $data[$i]["date"] . "<br>Status: " . $data[$i]["status"] . "<br>";
                    }
                } else {
                    echo "No records found.";
                }
            mysqli_close($con);
            ?>  
        </div>  
        <div id="file_link">
            <p style="margin:0px; font-size: 12px;">Download the Latest Version – Click to Access on Google Drive <a style="color: #000; font-size: 13px;" href="" class="download-button">&#x1F4C1; magnetocaloric.exe</a></p>
            

        </div>

    </div>
    <div id="container">
        <h1>&#x1F15C; magnetocaloric.exe<h2>
        <h2>Activation Key Generator</h2><br>
        
        <form id="contact-form" action="access.php" method="post">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="example@gmail.com" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" placeholder="MAgneto@4321" required>

            <label for="date">Valid Until:</label>
            <input type="date" id="date" name="date" required>
            <p>The generated activation key will remain active until the specified date of tenure.</p>
            
            <br><button type="submit" name="submit">Generate Activation Key</button>
            <p style="font-size: 10px;">Explore the Magnetocaloric mcepy project on GitHub: <a href="https://github.com/supratimdasinfo/magnetocaloric.mcepy">Magnetocaloric mcepy Repository</a></p>
        </form>

    </div>
    <footer>
        
	    <p>&#169 2023 Supratim Das. All Rights Reserved</p>	
    </footer>
 
</body>
</html>
