import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter a city (either chicago, new york city, or washington): ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print("Sorry, that's not a valid city!")
        city = input('Enter a city (either chicago, new york city, or washingon): ')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter a month (all, january, february, ... , june): ').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("Sorry, that's not a valid month!")
        month = input('Enter a month (all, january, february, ... , june): ')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a day of the week (all, monday, tuesday, ... sunday): ').lower()
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:        
        print("Sorry, that's not a valid day!")
        day = input('Enter a day of the week (all, monday, tuesday, ... sunday): ')
        
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[popular_month-1]
    print('The most popular month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day is: ', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo = (df['Start Station'] + ' + ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip is: ', popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_total = df['Trip Duration'].sum()
    print('The total travel time is: ', travel_total)

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print('The mean travel time is: ', travel_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users including count of gender and year of birth"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of user types are:\n', user_types, '\n')
    
    try:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('The count per genger is:\n', gender, '\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        min_birth = df['Birth Year'].min()
        print('The earliest birth year is: ', min_birth)

        max_birth = df['Birth Year'].max()
        print('The most recent birth year is: ', max_birth)

        mode_birth = df['Birth Year'].mode()[0]
        print('The most common birth year is: ', mode_birth)
    except:
        print('Sorry, there is no gender or birth year data avaialble for Washington')

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
        
        #Display 5 rows of the data if required by the user, continues until the user says no
        raw_data = input('\nWould you like to view 5 rows of the data? Enter yes or no.\n')
        counter = 0
        while raw_data.lower() == 'yes':
            print(df.iloc[counter:counter+5])
            raw_data = input('\nWould you like to view 5 more rows of the data? Enter yes or no.\n')
            counter += 5
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
