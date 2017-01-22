SET DATESTYLE TO 'European';
SET DATESTYLE TO 'SQL';

DROP TABLE device CASCADE;
DROP TABLE measurements CASCADE;
DROP TABLE one CASCADE;

CREATE TABLE device
(
	dev_ID          SERIAL,
	manufacturer    char(50),
	name            char(50),
	serial          char(50),
	firmware_ver    char(50),
        address         inet,
        port            int,
        CONSTRAINT      PK_dev      PRIMARY KEY(dev_ID)
);

CREATE TABLE measurements
(
	meas_ID      	SERIAL,
        meas_comments   TEXT,
        meas_dev_ID     SERIAL,
        meas_timestamp  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT      PK_meas_ID  PRIMARY KEY(meas_ID),
        CONSTRAINT      FK_meas_ID  FOREIGN KEY(meas_dev_ID) REFERENCES device(dev_ID) ON UPDATE CASCADE
);

CREATE TABLE one
(	
	one_ID  	SERIAL,
        one_meas_ID     SERIAL,
        one_interval    INT,
        one_Vpp         REAL,
        one_Vmax        REAL,
        one_Vmin        REAL,
        CONSTRAINT      PK_one_meas PRIMARY KEY(one_ID),
        CONSTRAINT      FK_one_meas FOREIGN KEY(one_meas_ID) REFERENCES measurements(meas_ID) ON UPDATE CASCADE
);


