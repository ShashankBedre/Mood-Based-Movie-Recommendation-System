import pandas as pd

# Load the dataset
file_path = 'netflix_titles.csv'
netflix_df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("Initial data:")
print(netflix_df.head())

# Handling missing values
# Display columns with missing values
print("\nMissing values before cleaning:")
print(netflix_df.isnull().sum())

# Fill missing values for categorical columns with a placeholder
netflix_df['director'].fillna('No Director', inplace=True)
netflix_df['cast'].fillna('No Cast', inplace=True)
netflix_df['country'].fillna('Unknown', inplace=True)
netflix_df['duration'].fillna('Unknown', inplace=True)
netflix_df['rating'].fillna('Unknown', inplace=True)

# Fill missing values for date columns with the mode (most frequent value)
most_frequent_date = netflix_df['date_added'].mode()[0]
netflix_df['date_added'].fillna(most_frequent_date, inplace=True)

# Standardize data formats
# Convert 'date_added' to datetime format
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')

# Handle duplicates
netflix_df.drop_duplicates(inplace=True)

# Feature Engineering
# Extract year from date_added
netflix_df['year_added'] = netflix_df['date_added'].dt.year

# Extract duration in minutes for movies
def get_duration_minutes(duration):
    if 'min' in duration:
        return int(duration.replace(' min', ''))
    else:
        return None

netflix_df['duration_minutes'] = netflix_df['duration'].apply(get_duration_minutes)

# Extract number of seasons for TV shows
def get_seasons(duration):
    if 'Season' in duration:
        return int(duration.split(' ')[0])
    else:
        return None

netflix_df['seasons_count'] = netflix_df['duration'].apply(get_seasons)

# Define updated mood function
def assign_mood(description, genres):
    description = str(description).lower()
    genres = str(genres).lower()

    if any(word in description for word in ['fight', 'war', 'battle', 'angry', 'revenge', 'violence', 'conflict']):
        return 'Angry'
    elif any(word in description for word in ['gross', 'disgusting', 'disturbing', 'horror', 'creepy']):
        return 'Disgust'
    elif any(word in description for word in ['fear', 'scary', 'terror', 'haunted', 'ghost', 'paranormal', 'nightmare']):
        return 'Fear'
    elif any(word in description for word in ['happy', 'funny', 'comedy', 'joy', 'celebrate', 'adventure']) or 'comedy' in genres:
        return 'Happy'
    elif any(word in description for word in ['sad', 'tragedy', 'heartbreaking', 'emotional', 'loss', 'grief']):
        return 'Sad'
    elif any(word in description for word in ['surprise', 'twist', 'unexpected', 'shock', 'mystery']) or 'mystery' in genres:
        return 'Surprise'
    else:
        return 'Neutral'

# Apply mood assignment
netflix_df['mood'] = netflix_df.apply(lambda row: assign_mood(row['description'], row['listed_in']), axis=1)

# Display data after feature engineering and mood assignment
print("\nData after feature engineering and mood assignment:")
print(netflix_df.head())

# Display missing values after feature engineering
print("\nMissing values after feature engineering:")
print(netflix_df.isnull().sum())

# Save the cleaned dataset
cleaned_file_path = 'cleaned_netflix_titles_with_mood.csv'
netflix_df.to_csv(cleaned_file_path, index=False)
print(f"\nDataset saved with mood and feature engineering: {cleaned_file_path}")
