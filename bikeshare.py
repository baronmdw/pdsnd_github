import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_input(inputstring, filtertype):
    """

    Converts allowed user input to correct string for further operations.

    Input: 
        (str) inpustring: user input in lower cases
        (str) filtertype: choice, if input has been made for cities, month or day
    
    Returns
        (str) corresponding working string for further operations
    """

    # dictionary for cities:
    citydict = {'chicago': ['chicago', 'c', 'chic'],
    'new york city':['new york city', 'nyc','new york'],
    'washington':['washington','w','wash']}

    #dictionary for months:
    monthdict = {'january':['january','jan','1'],
    'february':['february','feb','2'],
    'march':['march','mar','3'],
    'april':['april','apr','4'],
    'may':['may','5'],
    'june':['june','jun','6'],
    'all':['all']}

    #dictionary for days:
    daydict = {'sunday':['sunday','sun','su','1'],
    'monday':['monday','mon','mo','2'],
    'tuesday':['tuesday','tue','tu','3'],
    'wednesday':['wednesday','wed','we','4'],
    'thursday':['thursday','thu','th','5'],
    'friday':['friday','fri','fr','6'],
    'saturday':['saturday','sat','sa','7'],
    'all':['all']}

    # Return correct city string
    if filtertype == 'city':
        for city in citydict:
            if inputstring in citydict.get(city):
                return city
    
    #return correct month string
    if filtertype == 'month':
        for month in monthdict:
            if inputstring in monthdict.get(month):
                return month
    
    #return correct day string
    if filtertype == 'day':
        for day in daydict:
            if inputstring in daydict.get(day):
                return day
    




def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # Definition of allowed user inputs for city, month, day of week:
    legal_cities = ['chicago','c', 'chic','new york city','nyc','new york','washington','w','wash']
    legal_months = ['january','february','march','april','may','june','1','2','3','4','5','6','all']
    legal_days = ['sunday','su','sun','monday','mo','mon','tuesday','tu','tue','wednesday','we','wed','thursday','th','thu','friday','fr','fri','saturday','sa','sat','all']

    print('Hi! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_input = input('Choose City between Chicago (C), New York City (NYC) and Washington (W): ')
        except:
            print('Oops, that didn\'t go particularly well. Let\'s try again...')
            continue
        if city_input.lower() in legal_cities:
            city = get_input(city_input.lower(),'city')
            break
        else:
            print('Seems like there has been a Typo. Let\'s give it another try...')
            continue

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_input = input('Choose Month from January (1) to June (6) or all: ')
        except:
            print('Oops, that didn\'t go particularly well. Let\'s try again...')
            continue
        if month_input.lower() in legal_months:
            month = get_input(month_input.lower(),'month')
            break
        else:
            print('Seems like you searched for a month outside the db, please try again...')
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day_input = input('Choose Day of Week (Su,Mo,Tu,We,Th,Fr,Sa) or all: ')
        except:
            print('Oops, that didn\'t go particularly well. Let\'s try again...')
            continue
        if day_input.lower() in legal_days:
            day = get_input(day_input.lower(),'day')
            break
        else: 
            print('Seems like the day was not typed in the coorect format. Have another try...')
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_number = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month_number]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mc_month_number = int(df['month'].mode())
    print('The most common month for that rental perios is: {}'.format(mc_month_number))

    # display the most common day of week
    mc_day = df['day_of_week'].mode()[0]
    print('The most common Day of the week for that rental perios is: {}'.format(mc_day))

    # display the most common start hour
    mc_hour = int(df['Start Time'].dt.hour.mode())
    print('The most common Day of the week for that rental perios is: {}'.format(mc_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mc_startstation = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(mc_startstation))

    # display most commonly used end station
    mc_endstation = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(mc_endstation))

    # display most frequent combination of start station and end station trip
    # get count of most frequent combination
    mc_combination_max = df.groupby(['Start Station'])['End Station'].value_counts().max()

    #set up second dataset with combination and counts and extract start- end and station with count equal to maximum
    helpling = df.groupby(['Start Station','End Station']).size().reset_index().rename(columns={0:'count'})
    mc_comb_start = helpling[helpling['count']==mc_combination_max]['Start Station'].unique()[0]
    mc_comb_end = helpling[helpling['count']==mc_combination_max]['End Station'].unique()[0]
    print('The most commonly used way is from {} to {}.'.format(mc_comb_start,mc_comb_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {} sec.'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: {} sec.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n {}'.format(user_types))

    # Display counts of gender
    genders = df['Gender'].value_counts()
    print('Users split by gender:\n {}'.format(genders))

    # Display earliest, most recent, and most common year of birth
    earliest_yob = int(df['Birth Year'].min())
    recent_yob = int(df['Birth Year'].max())
    mc_yob = int(df['Birth Year'].mode())

    print('The oldest user was born in {}\n The youngest user was born in {}\n Most of the users were born in {}'.format(earliest_yob, recent_yob, mc_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

def show_data(df):
    i = 0
    while input('Do you want to see the next 5 rows of data? (y\\n):') == 'y':
        print(df[i:i+5])
        i+=5


if __name__ == "__main__":
	main()
