SET DATESTYLE TO 'European';
SET DATESTYLE TO 'SQL';

DROP TABLE device CASCADE;
DROP TABLE measurements CASCADE;
DROP TABLE one CASCADE;

CREATE TABLE device
(
	dev_ID          INT         NOT NULL,
	manufacturer    char(50),
	name            char(50),
	serial          char(50),
	firmware_ver    char(50),
        CONSTRAINT      PK_dev      PRIMARY KEY(dev_ID)
);

CREATE TABLE measurements
(
	meas_ID      	INT         NOT NULL,
        meas_comments   TEXT,
        meas_dev_ID     INT         NOT NULL,
        meas_timestamp  TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT      PK_meas_ID  PRIMARY KEY(meas_ID),
        CONSTRAINT      FK_meas_ID  FOREIGN KEY(meas_dev_ID) REFERENCES device(dev_ID) ON UPDATE CASCADE
);

CREATE TABLE one
(	
	one_ID  	INT         NOT NULL,
        one_meas_ID     INT         NOT NULL,
        one_interval    INT         NOT NULL,
        one_Vpp    REAL        NOT NULL,
        one_Vmax   REAL        NOT NULL,
        one_Vmin   REAL        NOT NULL,
        CONSTRAINT      PK_one_meas PRIMARY KEY(one_ID),
        CONSTRAINT      FK_one_meas FOREIGN KEY(one_meas_ID) REFERENCES measurements(meas_ID) ON UPDATE CASCADE
);


