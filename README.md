# NMEA files
In the first part of our project we asked to create NMEA files with our cellphones or using software, and search at the internet special NMEA files (plane, hot air balloon, ship ...).  

We choose a system that can read the NMEA files and produce such.

The system we choose is **- SatGen 3.**

The system allows to read NMEA files and shows the file details on the route – time, final distance, graph of speed, and show the route graph.

In addition the system can read also KML files and show the same details as the NMEA file.

The system can create demo files by two options :
*	Create a route from one point on the map and set the time.
*	Creating a route by selecting points on the map.

After it create the demo file it shows the same details as the NMEA file. 

Here is the software website - ([link to website](http://www.labsat.co.uk/index.php/en/products/satgen-simulator-software)):



# Converting NMEA files to CSV and KML files

In our project we ask to convert NMEA files to CSV and KML files by using python language. We built a system that can do this conversion.

**Options the system offers:**
*	Upload NMEA files to database by MySQL
*	Select the wanted data from the NMEA files (height, speed, time ...).
*	Choose the file type that we want to convert to – KML or CSV – from the database.
*	Create the file requested



#About the system:

The system allows to download NMEA files and save them into a database, also the system allows to make CSV and KML files from the database.

Here is our UML : 








**The system allows:**  
* uploading NMEA files to database (we used MySQL).
* Selecting / filtering the wanted data from the NMEA files (height, velocity, etc ...).
* Choosing the file type to receive from database (KML or CSV).
* producing the selected file.

##Introducing with NMEA (National Marine Electronics Association) files:

In this part of the project we have prepared a collection of NMEA files from the Internet and from our mobile phones:  
LG G3, Samsung 5, Sumsung 4s and iPhone 6s.  
The NMEA files was saved in different conditions: walking, driving in a car, flight and missile that was launched.  
In addition, we selected ***two*** software tools that allow visual display of NMEA files:

1. **VisualGPS 4.2 ([link to website](http://www.visualgps.net/visualgps/)):**  
      VisualGPS display graphically specific NMEA 0183 sentences and show the effects of selective availability (SA).  

      ***Features:***
      1. Azimuth and Elevation Graph: 
        * view all satellites that are in view.
        * plot and print the physical mask angle.
      2. Survey:
        * the survey window displays both position and xDOP (HDOP and VDOP) parameters.
        * monitor Standard Deviation and effects of Selective Availability.  Print the results graphically.
      3. Signal Quality/SNR Window: monitor satellite signal to noise ratios and see them graphically on the screen.
      4. NMEA Command Monitor: view NMEA sentences as they are received.  

2. **SatGen 3 ([link to website](http://www.labsat.co.uk/index.php/en/products/satgen-simulator-software)):**  
      SatGen NMEA is a very powerful, free piece of GPS Simulation software from Racelogic that allows you to create NMEA files and generate real-time NMEA serial streams.  

      ***Features:***
      1. Import NMEA file which contains GGA data directly into the software or alternatively to create a route in Google Earth, or build a profile using simple user commands.
      2. Create a static scenario, where a position can be manually inserted or easily determined using the integrated Google Maps screen.
      3. To draw a route by simply clicking-on a series of locations on the map.

##Planning the system:

In this part of the project we planned a system that allowing to load an NMEA files and save them in database.  
In addition , we added the possibility to produce from the database KML and CSV files.  
[Link to our UML](https://github.com/Most601/SecondExercise/blob/master/UMLmatala2.png)

##Creating the system:

In the final part of the project we created the program.

## Authors:
*	Chen Maman
* Tom Suad
* Doodi Yehezkel
* roi yadayi

