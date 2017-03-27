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
                $dev_type = "osc";
 
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
            Name: <input type="text" name="board_ip" value="<?php echo $board_ip;?>"><br>
            Device type:
            <input type="radio" name="dev_type" <?php if (isset($dev_type) && $dev_type=="osc") echo "checked";?> value="usb">Oscilloscope
            <input type="radio" name="dev_type" <?php if (isset($dev_type) && $dev_type=="multi") echo "checked";?> value="lan">Multimeter
            <input type="radio" name="dev_type" <?php if (isset($dev_type) && $dev_type=="gen") echo "checked";?> value="rs232">Gene<br><br>
            Connection type:<br/>
            <input type="radio" name="con_type" <?php if (isset($con_type) && $con_type=="usb") echo "checked";?> value="usb">USB
            <input type="radio" name="con_type" <?php if (isset($con_type) && $con_type=="lan") echo "checked";?> value="lan">LAN
            <input type="radio" name="con_type" <?php if (isset($con_type) && $con_type=="rs232") echo "checked";?> value="rs232">RS232<br><br>
            <input type="submit" name="submit" value="Submit"></form>
            
            <?php
                $query = "select * from devices";
                $result = pg_query($dbh, $query); 
                $num_fields = pg_num_fields($result);
                $num_rows = pg_num_rows($result);

                echo "</br>";
                echo "Number of register devices:";
                echo $num_rows;
                echo "</br>";
                echo "List of devices:";
                echo "<hr>";

                for ($rows = 0; $rows < $num_rows; $rows++) {
                    $tab = pg_fetch_array($result, $rows, PGSQL_ASSOC);
                    echo "</br>";
                    echo "ID: {$rows} </br>";
                    echo "Manufacturer: {$tab["dev_manufacturer"]}</br>";
                    echo "Name: {$tab["dev_name"]}</br>";
                    echo "Serial: {$tab["dev_serial"]}</br>";
                    echo "Firmware ver: {$tab["dev_firmware_ver"]}</br>";
                    echo "</br>";
                    if ($tab["dev_con_type"] == 'lan  ') {
                        echo "Connection:</br>";
                        echo "Type:{$tab["dev_con_type"]}  IP:{$tab["dev_lan_address"]} Port:{$tab["dev_lan_port"]}";
      
                    } elseif ($tab["dev_con_type"] == 'usb  ') {
                        echo "Connection:</br>";
                        echo "Type:{$tab["dev_con_type"]}  Path:{$tab["dev_usb_path"]}";

                    } elseif ($tab["dev_con_type"] == 'rs232') {
                        echo "Connection:</br>";
                        echo "Type:{$tab["dev_con_type"]}  Path:{$tab["dev_rs232_path"]} Baudrate:{$tab["dev_rs232_baudrate"]}";

                    } else {
                        echo "Cnnection not defined";
                    }
                    echo "<br>";
                    echo "Status:";
                    
                    echo "  
                    <input type=submit name=delete_device value=Delete></form>
    
                    echo "<hr>";
                }
            ?>
        </section>


        </aside>
    </body>
</html>
