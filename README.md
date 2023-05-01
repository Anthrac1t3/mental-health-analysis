Project- Mental Health Analysis: 

To analyze the mental health of the user by their social media posts in twitter, Instagram, reddit, Facebook and other platforms. In this work, the number of peoples content in social media in which opinions are highly unstructured and are either positive or negative or sometimes neutral is being used for the analysis.  Simulation results show the results in sentiment analysis of the social media data for the intuitive mental wellness of a person. This project highlights the methodology for mental health analysis for the intuitive well-being of the person. It uses sentiment analysis and its approach to analyze the mental well-being of users and display results using data visualization. 


Project is deployed in webUI - https://lsdm-project.coles-lab.com/index.html
In above site Home page have search functionality, Results page displays the trends and statistics from the results of sentiment analysis to understand the project we have project description in the webpage. 

To execute and test

#1. Run the webscrapping script (TwitterScraperThreads.py / TwitterScraper.py ) to extract the data from the internet. This will download the data in fomr of .csv files.
#2. Execute the quoteCleaner.py by input the filepath where the files are downloaded from above step and output files will be generated with all quotes cleaned as part of dat cleaning.
#3. Login to https://lsdm-project.coles-lab.com/pgadmin4/ with the credentials given and create a database in the project server and create tables, indexes and primary key. Now import the files data to the tables. 
#4. To view the WebUI visit: https://lsdm-project.coles-lab.com/index.html where you can enter your search keyword as text or emoji. The source files for this is in LSDM_weinterface folder.
#5. For sentiment Analysis and data visualizations execute the sentimentAnalysis.py file by input the cleaned data files and output images are being downloaded in form of bargraphs and word cloud. These results are used to display the trends and statistics in the webinterface showing the mental health of people.
