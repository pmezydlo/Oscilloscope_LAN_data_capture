SET DATESTYLE TO 'European';
SET DATESTYLE TO 'SQL';

DROP TABLE measurements CASCADE;

CREATE TABLE measurements
(
	meas_ID             SERIAL,
	meas_manufacturer   char(50),
	meas_name           char(50),
	meas_serial         char(50),
	meas_firmware_ver   char(50),
        meas_address        inet,
        meas_port           int,
        meas_time           timestamp DEFAULT CURRENT_TIMESTAMP,
        meas_channel        char(10),
        one_Vpp             REAL,
        one_Vmax            REAL,
        one_Vmin            REAL,
        CONSTRAINT          PK_dev      PRIMARY KEY(meas_ID)
);

