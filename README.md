# Intimate Partner Violence in the United States: An Analysis Using NIBRS Data
### by Valeria Chavez and Sadie Murray

## Introduction
The CDC defines Intimate Partner Violence as physical violence, sexual violence, stalking, and psychological aggression by a current or former intimate partner (CDC 2021). According to NCADV (2021), on average, nearly 20 people per minute are physically abused by an intimate partner in the United States. In a single year, this equates to more than 10 million men and women. Despite the staggering numbers, there is little to no publicly available resources showing what the spatial distribution of this phenomena looks like. In an attempt to help close that gap, this project maps intimate partner violence in the United States at the county level between 2006 and 2019. We looked at reported incidents of simple assault, aggravated assault, and homicide and nonnegligent manslaughter in 46 states and the District of Columbia. Our findings give us a better understanding of the spatial distribution of intimate partner violence in the United States and contribute to the public awareness around this issue.

## Data and Methodology
### NIBRS
This project relied on the FBI's NIBRS dataset. The National Incident-Based Reporting System (NIBRS) is an incident-based reporting system used by law enforcement agencies in the United States for the collection and reporting of data on criminal offenses. This dataset provides incredibly detailed information about the victims and the offenders (including race, ethnicity, age, sex), weapon, circumstances, and most importantly the ~relationship~ between the victim and the offender. Due to the lack of data exclusively about intimate partner violence at the national level, we relied on a subset of NIBRS data for our analysis. Using Python, we selected the incidents that had one of the following relationship IDs: (3) boyfriend/girlfriend, (21) spouse, (26) ex-spouse. We then narrowed this down further by selecting the three types of offenses: (51) simple assault, (27) aggravated assault, and (32) murder and nonnegligent manslaugther.

A limitation of the NIBRS data is that incidents are reported on a voluntary basis by law enforcement offices across the country which leads to significant gaps in the availability of the data. States such as New York, Florida, and California do not report incidents to NIBRS at all and some states started doing so only in 2019. The absence of data in states with large populations is a significant limitation given that it considerably skews the ranges of the data. It is worth noting that, despite the 2020 NIBRS data becoming available on December 8th, 2021, this project included data as early as 2019.

#### Other Data
We retrieved the County Shapefile from the Census Bureau's GIS data website. We joined the NIBRS data to the shapefiles using ArcGIS Pro. We also used the Dark Grey basemap that is freely available through the ArcGIS JavaScript API.

### Methodology
This project relied on a multitude of technologies including Python, ArcGIS Pro, ArcGIS Online, the ArcGIS JavaScript API, and HTML. Below you can find a general framework of the  main steps we used to conduct our analysis and produce this web application.

![This is an image](https://github.com/sadiecee/finalproj_web/blob/master/Images/flowchart.png)

#### Python
We built a Python script that allowed us to extract all incidents between 2006 and 2019 where the victim and the offender were or had been intimate partners. We subset the data to focus exclusively on simple assault, aggravated assault, and murder and nonnegligent manslaughter. In order to be able to map the incidents at the county level, we used the county and state information provided and assigned each entry their corresponding FIPS code. We then exported the subset into csv files corresponding to each year between 2006 and 2019. A copy of the script is available on the Scripts folder of this Repository.

#### ArcGIS
This project relied heavily on ESRI products, particularly ArcGIS Pro, ArcGIS Online, and the ArcGIS JavaScript API. Once we were done with the data processing in Python, we imported the data into ArcGIS Pro and used the FIPS codes to join it to a shapefile of all US counties. We exported the joined layers as Web Layers onto ArcGIS Online. We then incorporated all layers into our web application using the ArcGIS JavaScript API which also allowed us to incorporate a series of widgets into our map namely LayerList, Legend, ScaleBar, and Compass. We chose to work with the ArcGIS JavaScript API because it provides users with an experience that makes an impact. The availability of widgets and the option to freely host feature layers on the ArcGIS Online server was really valuable and it allowed us to display much more data than we would have otherwise been able to.

#### HTML
We built this web application using the html and css styling skills we learned throughout the semester. We aimed for a minimalist style that clearly communicated our message. We relied on the ArcGIS JavaScript API for all map related functionality as well as some local JavaScript for the website's functionality. The integration between our html files and the ArcGIS JavaScript API were notably successful and allowed us to provide a better user experience.

## New Things We Learned How to Do
While we explored the ArcGIS JavaScript API in class and the widgets during one of our labs, this project gave us the opportunity to work directly with Group Layers and the ArcGIS Online server. When we created the layers in ArcGIS Pro, we knew we would need to group them by type of offense in order to make it clear to the user what they were looking at. We failed repeatedly at adding the layers groups to our script and were only able to get the first one to be visualized. However, after lots of Googling and reading the documentation of the ArcGIS JavaScript API we realized we needed to bring all the layers onto the web app individually and then group them, not vice versa. With the help of the Layer List widget, we were able to set up all the layers in 4 separate groups listed in chronological order giving the user the option of toggling back and forth between the layers.

## Results

![This is an image](https://github.com/sadiecee/finalproj_web/blob/master/Images/ipv_map.PNG)

Comparing the final result to the original proposal, the project was a great success. We built a web application that allowed users to visualize the spatial distribution of intimate partner violence in the United States from 2006 to 2019. We created several different pages using HTML that were interconnected through the effective use of JavaScript. We incorporated a series of widgets to our map which made the user experience more interactive and overall better. We unfortunately were not able to sort out how to get insights on click for each of the counties which was something that we really wanted to do. In general, we ended up leaning more toward the functional and aesthetic aspect of the web application rather than the analysis of the data.

## References
* CDC. (2021). Preventing Intimate Partner Violence. https://www.cdc.gov/violenceprevention/intimatepartnerviolence/fastfact.html
* NCADV. (2021). Statistics. https://ncadv.org/STATISTICS
* FBI. National Incident-Based Reporting System (NIBRS). https://www.fbi.gov/services/cjis/ucr/nibrs

## Appendix: Roles and Responsibilities
Having worked together for about 3-years now, Valeria and Sadie have a great working dynamic and so the responsibilities were pretty evenly distributed. Valeria worked on the acquisition, cleaning, and processing of the data in Python as well as the creation of Web Feature Layers in ArcGIS Pro. She incorporated the layers onto the website and added a series of widgets to the final map using the ArcGIS JavaScript API. Sadie built the full structure of the website using html and JavaScript ensuring the functionality of all the buttons and the interconnectedness of the layers. We both contributed to the aesthetic choices and the written content on the website.
