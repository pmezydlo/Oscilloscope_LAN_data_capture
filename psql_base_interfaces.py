import sys
import time
import os
import psycopg2

class psql_connection():
    def __init__(selfbase)
        self.connect = None 
        self.database = None
        self.user = None

    def psql_connect(self, database, user)
        try:
            self.database = database
            self.user = user
            self.connect = psycopg2.connect(database=self.database, user=self.user)     
        except psycopg2.DatabaseError, e:
            print('Database error {}'.format(e));
            sys.exit(1)
        finally:
            if self.connect:
                self.connect.close()
                
    def psql_disconnect(self)
        self.connect.close()

    def psql_push_measure_device(device_type, device_manufacturer, device_name, device_serial_number,
                                    device_firmware_ver)
        try:
            cur = self.connect.cursor()
            query = "INSERT INTO measurements VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, DEFAULT)"
            data = (ids[0],  ids[1],  ids[2], ids[3], osc_ip, port, channel)
            cur.execute(query, data)
            self.connect.commit()
        except psycopg2.DatabaseError, e:
            print('Database error {}'.format(e));
            sys.exit(1)
        finally:
            if self.connect:
                self.connect.close()

