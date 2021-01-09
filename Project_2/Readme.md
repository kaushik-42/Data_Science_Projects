# Disaster Response Pipeline Project

This project data is provided by Figure 8(Udacity Partner) which has the pre-labelled tweets and text messages from real life disasters. So in this project we analyze the tweets and categorize the tweets into 36 columns like water, request, etc. We have to repair the present data with an ETL pipeline and build an ML pipeline to build a supervised learning model which can accurately categorize the new tweets. The outline of the repo is given below and instructions to run.

### File Structure:

	- app
	| - template
	| |- master.html  # main page of web app
	| |- go.html  # classification result page of web app
	|- run.py  # Flask file that runs app

	- data
	|- disaster_categories.csv  # data to process 
	|- disaster_messages.csv  # data to process
	|- process_data.py
	|- InsertDatabaseName.db   # database to save clean data to

	- models
	|- train_classifier.py
	|- classifier.pkl  # saved model 

	- README.md

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

![disaster_response_project2](Result for our message.png)

### Example 

Type a message such as: My house is full of water! Please help

 
### Contact Me via Linkedin <a href="https://www.linkedin.com/in/kaushik-tummalapalli/">Here!</a>
