import sys
import pandas as pd
from sqlalchemy import *

def load_data(messages_filepath, categories_filepath):
    '''All the loading steps including merging is in the next 3 lines'''
    """
        args:
            messages_filepath is the the messages dataframe present in the csv format
            categories_filepath is the the messages dataframe present in the csv format
        returns:
            we get the merged dataframe
        
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on='id', how='outer')
    return df


def clean_data(df):
    '''All the cleaning steps that we performed like one coding data, splitting into categories.'''
    """
        args:
            The dataframe we got from the load_data method.
        returns:
            we get the cleaned dataframe after doing the pre-processing steps
        
    """

    categories = df['categories'].str.split(";", expand=True)
    row = categories.iloc[0]
    category_colnames = list(map(lambda x: x.split("-")[0], categories.iloc[0].values.tolist()))
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
        
        # convert column from string to numeric
        categories[column] = categories[column].apply(pd.to_numeric)
    """
        I have gone through the official pandas docs and found one great method i.e duplicated()
        dataframe.duplicated(subset=[col],keep=first)
        'subset' is not necessary and 'keep' tells you about how to count that col as duplicated or not.
        I'll be using this method to find out how many duplicates are present so that we can drop them for further processing!
    """
    df=df.drop('categories',axis=1)
    df = pd.concat([df, categories], axis=1)
    df = df.drop_duplicates(keep='first')
    return df


def save_data(df, database_filename):
    '''Saves the cleaned dataframe to a table messages in the database given'''
    """
        args:
            df is the the cleaned data frame from the clean_data method
            database_filename is the database filename where the data is stored currently
        returns:
            we convert the dataframe to sql
        
    """

    engine = create_engine('sqlite:///'+ database_filename)
    df.to_sql('messages', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
