#----User interface----#

#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Define Functions----#
def show_original_data():
    murders_by_country_df = pd.read_csv('murders_by_country.csv')
    print(murders_by_country_df)

def show_updated_data():
    updated_murders_by_country_df = pd.read_csv('murders_by_country_updated.csv')
    print(updated_murders_by_country_df)

def show_top_5_countries():
    murders_by_country_top_5_df = pd.read_csv('murders_by_country_top_5.csv')
    print(murders_by_country_top_5_df)

def show_bottom_5_countries():
    murders_by_country_bottom_5_df = pd.read_csv('murders_by_country_bottom_5.csv')
    print(murders_by_country_bottom_5_df)

def show_updated_data_visualised():
    murders_by_country_df = pd.read_csv('murders_by_country_updated.csv')

    murders_by_country_df.plot(
                           kind='bar',
                           x='country',
                           y='Total',
                           color='blue',
                           alpha=0.3,
                           title='The number of total murders in 187 countries between 1990 and 2016'
                          )
    plt.show()

def show_top_5_countries_visualised():
    murders_by_country_top_5_df = pd.read_csv('murders_by_country_top_5.csv')

    murders_by_country_top_5_df.plot(
                                 kind='bar',
                                 x='country',
                                 y='Total',
                                 color='blue',
                                 alpha=0.3,
                                 title='The top 5 countries with the most murders between 1990 and 2016'
                                )
    plt.show()

def show_bottom_5_countries_visualised():
    murders_by_country_bottom_5_df = pd.read_csv('murders_by_country_bottom_5.csv')

    murders_by_country_bottom_5_df.plot(
                                 kind='bar',
                                 x='country',
                                 y='Total',
                                 color='blue',
                                 alpha=0.3,
                                 title='The top 5 countries with the least murders between 1990 and 2016'
                                )
    plt.show()

#----User options----#
def userOptions():
    global quit
    
    print('Welcome! To get started press either 1, 2, 3, 4, 5, 6, 7 or 8.')
    print('Pressing 1 will read and display the unaltered "murders by country" dataset in a dataframe.')
    print('Pressing 2 will clean and analyse the dataset before displaying it in a dataframe.')
    print('Pressing 3 will show the top 5 countries with MOST murders in a dataframe.')
    print('Pressing 4 will show the top 5 countries with LEAST murders in a dataframe.')
    print('Pressing 5 will visualise the full dataset using a Matplotlib chart.')
    print('Pressing 6 will visualise the top 5 countries with the MOST murders using a Matplotlib chart.')
    print('Pressing 7 will visualise the top 5 countries with the LEAST murders using a Matplotlib chart.')
    print('Pressing 8 will stop the program.')

    user_choice = int(input('Enter a number between 1 and 8: '))
    if user_choice == 1:
        show_original_data()
    elif user_choice == 2:
        show_updated_data()
    elif user_choice == 3:
        show_top_5_countries()
    elif user_choice == 4:
        show_bottom_5_countries()
    elif user_choice == 5:
        show_updated_data_visualised()
    elif user_choice == 6:
        show_top_5_countries_visualised()
    elif user_choice == 7:
        show_bottom_5_countries_visualised()
    elif user_choice == 8:
        quit = True
    else:
        print('Error!!! Try entering a number between 1 and 7')

while not quit:
    userOptions()