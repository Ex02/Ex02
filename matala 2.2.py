from Tkinter import *

import csv
import sqlite3
import math
    
def NMEAtoCSV():

    from datetime import datetime
    #put your path to nmea file .
    INPUT_FILENAME = "C:/Users/david/Desktop/stockholm_walk.nmea"
    with open(INPUT_FILENAME, 'r') as input_file:
        reader = csv.reader(input_file)
        conn = sqlite3.connect('nmea_to_db.db')
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS info')
        #flag will tell us if the GPGGA is good if yes continue to the GPRMC
        flag = 0
        # Create table
        c.execute('''CREATE TABLE info
                         (date text,time text,speed float, latitude text, latitude_direction text, longitude text, longitude_direction text,fix text,horizontal_dilution text,altitude text,direct_of_altitude text,altitude_location text)''')
        # create a csv reader object from the input file (nmea files are basically csv)
        for row in reader:
            # skip all lines that do not start with $GPGGA
            if not row:
                continue
            elif row[0].startswith('$GPGGA') and row[6]=='1':
                time = row[1]
                latitude = row[2]
                lat_direction = row[3]
                longitude = row[4]
                lon_direction = row[5]
                fix = row[6]
                horizontal = row[7]
                altitude = row[8]
                direct_altitude = row[9]
                altitude_location = row[10]
                flag = 1
            elif row[0].startswith('$GPRMC') and flag==1:
                speed = row[7]
                date = row[9]
                warning = row[2]
                if warning == 'V':
                    continue
                c.execute("INSERT INTO info VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(date,time,speed, latitude, lat_direction, longitude, lon_direction,fix,horizontal,altitude,direct_altitude,altitude_location))
            # Save (commit) the changes
                conn.commit()
                flag=0
            else:
                continue
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def DBtoCSV():
    conn = sqlite3.connect("C:/Python27/Projects/nmea_to_db.db") #open db in path for file 
    cursor = conn.cursor() #cursor to the db
    cursor.execute("select * from info;") # execute a sql script

    with open("out.csv", "wb") as csv_file: #writing to csv
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description]) # write headers
        csv_writer.writerows(cursor)
#GUI for nmea 2 DB && DB 2 csv ...        
root = Tk()
root.title("doodi")
root.geometry("600x400")
app = Frame(root)
app.grid()

DoodiRunButton = Button(app , text = "DB load NMEA" , command = NMEAtoCSV)
DoodiRunButton.pack()

DoodiRunButton = Button(app , text = "convert form DB to csv" , command = DBtoCSV)
DoodiRunButton.pack()

DoodiRunButton = Button(app , text = "convert from DB to kml" , command = NMEAtoCSV)
DoodiRunButton.pack()

mainloop()
