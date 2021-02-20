# Starbucks Capstone Project:

## Table of contents:

-  How to run?
-  Motivation for this project?
-  Business understanding
-  Data
-  Results
-  Licensing, Authors, Acknowledgements
-  Contact Me via Linkedin
-  Project 4: Starbucks Capstone Project

## 1> How to run?
- Open the Starbucks_Capstone_notebook.ipynb
- You can download the file and run it locally on Jupyter Notebook as its a .ipynb file
- It's completely written in python language
- Libraries used: 
    - matplotlib
    - numpy
    - pandas
    - seaborn
    
## 2> Motivation for this project?
- Starbucks is one of the largest and famous coffee brands in the world and it has at least one store down the street in the US! In US alone, Starbucks managed to     attract 18.9 million people and this number is growing steadily and worldwide it has 31,256 stores!!!So starbucks do have a greater responsibility to provide       great value to their customers with various offers so that they can get these customers quite regularly and also new potential customers by referring and many       ways. As part of Udacity Nano Degree program, let’s try to unwind and explore how the members respond to various offers in Starbucks. I thank Udacity and           Starbucks for providing the simulated data for this capstone challenge and now its time to jump in theproject :)

## 3> Data:

The data is contained in three files:

- portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)
- profile.json - demographic data for each customer
- transcript.json - records for transactions, offers received, offers viewed, and offers completed

Here is the schema and explanation of each variable in the files:

portfolio.json

- id (string) - offer id
- offer_type (string) - the type of offer ie BOGO, discount, informational
- difficulty (int) - the minimum required to spend to complete an offer
- reward (int) - the reward is given for completing an offer
- duration (int) - time for the offer to be open, in days
- channels (list of strings)

profile.json

- age (int) - age of the customer
- became_member_on (int) - the date when customer created an app account
- gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- id (str) - customer id
- income (float) - customer's income

transcript.json

- event (str) - record description (ie transaction, offer received, offer viewed, etc.)
- person (str) - customer id
- time (int) - time in hours since the start of the test. The data begins at time t=0
- value - (dict of strings) - either an offer id or transaction amount depending on the record

## 4> Business understanding: ( These are the questions to which we will be answering )
- Quick Glance about the data. 

- What will be the offer recommendations for an existing customer?

- What will be the new recommendations for a potential new customer?

- What percent of gender population are considering the ‘BOGO’ offer( buy one get one) and standard discount offer?

- What percent of gender population are responding to certain platforms for offers like ‘web’ source/ ’email’ / ’mobile’ / ’social’ ?

## 5> Results:
- Results are given in this <a href="https://kaushiktummala55.medium.com/starbucks-capstone-challenge-using-funksvd-b08f9f8f983b">Medium article!</a>

## 6> Licensing, Authors, Acknowledgements
- Must give credit to Udacity and Starbucks for the data.Otherwise, feel free to use the code here as you would like!

### 7> Contact Me via Linkedin <a href="https://www.linkedin.com/in/kaushik-tummalapalli/">Here!</a>

