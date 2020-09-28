import time
import pandas as pd
import numpy as np
from statistics import mode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
    while city not in CITY_DATA:
        print("\n\n enter one of thr 3 cities")
        city = input("Would you like to see data for Chicago, New York, or Washington?").lower()
    # get user input for month (all, january, february, ... , june)
    month=input("Which month - January, February, March, April, May, or June?").lower()
    while month not in months:
        print("\n\n enter the month correctly please")
        month=input("Which month - January, February, March, April, May, or June?").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
    while day not in days:
        print("\n\n enter the day correctly please")
        day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()


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
    #print(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #print(df['day_of_week'])
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

    # display the most common month
    popular_month=df['month'].mode()[0]
    print("most popular month:",popular_month)

    # display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print("most popular day of the week:",popular_day)

    # display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used start station:",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("most commonly used end station:",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    comb=df.mode()
    print("most commonly used combination of stations:",comb['Start Station'][0]," & ",comb['End Station'][0])
    #                       or
    #counts = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    #print(counts)
    #print("most commonly used combination if stations:",counts.index[0])
    #df['End Station'].mode()[0]&df['Start Station'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=sum(df['Trip Duration'])
    print("Total travel time: ",total_travel)

    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print("mean travel time: ",mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    try:
            gender = df['Gender'].value_counts()
            print(gender)
    except:
        print('there isn\'t a gender column.\n')

    # Display earliest, most recent, and most common year of birth
    try:
        print("earliest year of birth:",min(df['Birth Year']))
        print("most recent year of birth:",max(df['Birth Year']))
        print("most common year of birth:",df['Birth Year'].mode()[0])
    except:
        print('there isn\'t a birth year column.\n')

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
        i=0
        j=5
        while input("would you like to see the data ? enter yes/no.\n")=="yes":
            print(df.iloc[i:j])
            i+=5
            j+=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
