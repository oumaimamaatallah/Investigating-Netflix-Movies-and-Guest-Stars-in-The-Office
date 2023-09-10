
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103,101,99,100,100,95,95,96,93,90]
movie_dict = {'years': years, 'durations': durations}
print(movie_dict)
import pandas as pd
durations_df=pd.DataFrame(movie_dict) 
print(durations_df)
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(years,durations)
plt.title('Netflix Movie Durations 2011-2020')
plt.show()
#Loading the rest of the data from a CSV
netflix_df =pd.read_csv("datasets/netflix_data.csv")
print(netflix_df[0:5])
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df['type']=='Movie']
netflix_movies_col_subset = netflix_df_movies_only.loc[:,["title","country","genre","release_year","duration"]]
print(netflix_movies_col_subset[0:5])
# increase the figure size
fig = plt.figure(figsize=(12,8))
# Create a scatter plot of duration versus year
plt.scatter(years,durations)
# Create a title
plt.title("Movie Duration by Year of Release")
plt.show()
# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"]<60]
colors =[]

# Iterate over rows of netflix_movies_col_subset
for  lab,row in  netflix_movies_col_subset.iterrows():
    if row['genre']=="Children" :
        colors.append("red")
    elif row['genre']== "Documentaries":
        colors.append("blue")
    elif row['genre']=="Stand_Up" :
        colors.append("green")
    else:
        colors.append("black")
#plotting with color
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(release_year,duration)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration(min)")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = "yes"









