<?php
// Connect to database
$servername = "db";
$username = "vsec";
$password = "pass";
$dbname = "users_db";

$db = mysqli_connect($servername, $username, $password, $dbname);

$authorized = false;

// Get user input
if (!empty($_POST)) {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    // Validate user
    $query = 'SELECT * FROM users WHERE username="'.$user.'" AND password="'.$pass.'"';
    $result = mysqli_query($db, $query);
    if (!$result) {
        $error = mysqli_error($db);
    } else if (mysqli_num_rows($result) > 0) {
        $authorized = true;
        $rows = mysqli_fetch_assoc($result);
        $user = $rows['username'];
        $pass = $rows['password'];
    } else {
        $query = 'SELECT * FROM users WHERE username="'.$user.'"';
        $result = mysqli_query($db, $query);
        if (!$result || mysqli_num_rows($result) == 0) {
            $error = "Invalid username.";
        } else {
            $error = "Invalid password.";
        }
    }
    // Close database connection
    mysqli_close($db);
}
?>

<!-- Render HTML-->
<!DOCTYPE html>
<html>
<head>
<style>
* {
    margin: 0;
    padding: 0;
}
body {
    background: blue;

}

img {
  width: 400px;
  text-align: center;
}
div {
    width: 75%;
    margin-left: auto;
    margin-right: auto;
    background-color: white;
    padding: 50px;
    box-shadow: 0 2px 15px rgba(0,0,0,0.35);
}

form.login {
    display: block;
    width: 400px;
    margin-top: 5%;
    margin-left: auto;
    margin-right: auto;
    padding: 10px;
    background: white;
    color: black;
    border-radius: 10px;
    box-shadow: 0 2px 15px rgba(0,0,0,0.35);
}
h2 {
    font-family:Tahoma, sans-serif;
    font-size: 24px;
    margin-bottom: 18px;
}
h1 {
    font-family:Tahoma, sans-serif;
    font-size: 36px;
    margin-bottom: 30px;
}
p {
    font-family: Tahoma, sans-serif;
    font-size: 15px;
    margin-bottom: 4px;
}
.error {
    margin-top: 12px;
    padding: 4px 6px;
    background-color: red;
    color: white;
    font-weight: bold;
    border-radius: 4px;
}

label {
    display: inline-block;
    width: 90px;
}
input {
    padding: 7px 14px;
    border: none;
    border-radius: 4px;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.35);
}
input[type=submit] {
    background-color: blue;
    color: white;
    font-weight: bold;
    box-shadow: none;
    cursor: pointer;
}
input.logout {
    position: absolute;
    right: 13%;
    top: 50px;
}

form.header{
    display: block;
    width: auto;
    margin-top: 5%;
    margin-left: auto;
    margin-right: auto;
    padding: 20px;
    background: purple;
    color: white;
    border-radius: 10px;
    font-size: 36px;
    text-align: center;
}

.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

</style>
</head>
<body>

<!-- Login page -->
<?php if (!$authorized) { ?>

    <form class= "header">
    <h1> Welcome to lonely krakens! A place for single krakens looking for love</h1>
    <p><img src="https://i.pinimg.com/originals/2a/62/00/2a620034d8e1d4ef924e0ef739437ee3.jpg"></p>
    </form>


    <form class="login" method="POST">
        <h2>Please log in to find your kraken love now!!!!:</h2>
        <p><label>Username:</label><input type="text" name="username" value="<?php if(!empty($user)) echo $user;?>"></p>
        <p><label>Password:&nbsp;</label><input type="password" name="password" value="">&nbsp;
        <input type="submit" value="Go"></p>
        <?php if(!empty($error)) echo '<p class="error">'.$error.'</p>';?>
    </form>



    


<!-- Normal user home page -->
<?php } else {?>
     <div>
        <h1>Krayline is looking for love. </h1>
        <h2>She enjoys eating ships, and long walks on the beach. </h2>
        <p><img src="https://i.postimg.cc/nhB1n15t/finalkrakenlady1.jpg" class="center"></p>
 
        
        <p>&nbsp;</p>
        <form><input class="logout" type="submit" value="Logout"></form>
    </div>

<?php } ?>

</body>
</html>
