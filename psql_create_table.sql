SET DATESTYLE TO 'European';
SET DATESTYLE TO 'SQL';

DROP TABLE devices CASCADE;

CREATE TABLE devices
(
	dev_ID             SERIAL,
	dev_manufacturer   char(50),
        dev_name           char(50),
        dev_serial         char(50),
	dev_firmware_ver   char(50),
        dev_con_type       char(5),
        dev_lan_address    char(15),
        dev_lan_port       int,
        dev_usb_path      char(50),
        dev_rs232_path    char(50),
        dev_rs232_baudrate int,
        CONSTRAINT         PK_dev      PRIMARY KEY(dev_ID)
);

INSERT INTO devices VALUES (1, 'RIGOL', '', '', '', 'lan', '192.168.15.20', 5555, '', '', NULL);
INSERT INTO devices VALUES (2, 'HP', '', '', '', 'usb', '', NULL, '/dev/usb_tmc1', '', NULL);
INSERT INTO devices VALUES (3, 'KEYSIGHT', '', '', '', 'rs232', '', NULL, '', '/dev/ttyUSB0', 9600);
