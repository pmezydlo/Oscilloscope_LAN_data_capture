<html>
 <head>
  <title>PHP Test</title>
<style>
section {
  float: left;
}
aside {
  float: right;
}

</style>

 </head>
 <body>

<header>
    <p>This is simple script</p></br>
</header>
<section>

<?php


$board_ip = "192.168.7.2";
$dev_manu = "RIGOL";
$dev_name = "DS1104";
$dev_ip = "";
$dev_port = "";
$con_type = "usb";

 
$dbh = pg_pconnect("dbname=measurement host=localhost user=pmezydlo password=pass1234") or die("Not  connected");

$query = "select * from measurements";
$result = pg_query($dbh, $query);

$num_fields = pg_num_fields($result);
$num_rows = pg_num_rows($result);

echo "<TABLE border width=1>";
echo "<TR>";

for ($fields = 0; $fields < $num_fields; $fields++) {
    echo "<TH>";
    echo pg_field_name($result, $fields);
    echo "</TH>";
}

echo "</TR>";

for ($rows = 0; $rows < $num_rows; $rows++) {
    echo "<TR>";
    for ($fields = 0; $fields < $num_fields; $fields++) {
        echo "<TD>";
        echo pg_fetch_result($result, $rows, $fields);
        echo "</TD>";
    }
    echo "</TR>";
}

echo "</TABLE>";
?>
</section>

<aside>
Register new device:
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  IP: <input type="text" name="board_ip" value="<?php echo $board_ip;?>">
  <br><br>
  Manufacturer: <input type="text" name="dev_manu" value="<?php echo $dev_manu;?>">
  <br><br>
  Device: <input type="text" name="dev_name" value="<?php echo $dev_name;?>">
  <br><br>
  Connection type:<br/>
  <input type="radio" name="con_type" <?php if (isset($con_type) && $con_type=="usb") echo "checked";?> value="usb">USB
  <input type="radio" name="con_type" <?php if (isset($con_type) && $con_type=="lan") echo "checked";?> value="lan">LAN
  <input type="radio" name="con_type" <?php if (isset($con_type) && $con_type=="rs232") echo "checked";?> value="rs232">RS232
  <br><br>
<input type="submit" name="submit" value="Submit"></form>
</aside>


 </body>
</html>
