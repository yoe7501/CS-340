Grazioso Salvare Animal Rescue Dashboard
Project Description
This project is a web-based dashboard for Grazioso Salvare, designed to analyze and filter animal shelter data to identify suitable candidates for rescue training programs. The dashboard is built using MongoDB, Dash, and Plotly libraries.
Key Features
1.	Interactive Filters:
o	Filter animals by rescue type:
	Water Rescue
	Mountain/Wilderness Rescue
	Disaster/Tracking
o	Reset filter to view all animals.
2.	Dynamic Data Table:
o	Displays shelter data fetched from MongoDB.
o	Updates based on selected filters.
3.	Geolocation Chart:
o	Visualizes animal locations on a map using latitude and longitude data.
4.	Breed Distribution Chart:
o	Displays the frequency of different breeds in filtered results.
Tools and Technologies
•	MongoDB: For storing and querying shelter data.
•	Dash by Plotly: For creating the interactive web dashboard.
•	Pandas: For data manipulation and formatting.
•	Plotly Express: For generating charts and geolocation maps.
•	JupyterDash: To run the Dash app within Jupyter notebooks.
 
Challenges and Solutions
•	Dynamic Filtering: Ensured filters dynamically update all widgets using Dash callbacks.
•	Geolocation Data: Validated MongoDB data to include accurate latitude and longitude fields.
