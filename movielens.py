#Importing Necessary Libraries
import pandas as pd
import datacompy

#Reading in Datasets
#Links/Identifiers dataset
links = pd.read_csv("MovieLens\ml-latest-small\ml-latest-small\links.csv")
links.info
links.head()

#Movies dataset
movies = pd.read_csv("MovieLens\ml-latest-small\ml-latest-small\movies.csv")
movies.info
movies.head()

#Ratings dataset
ratings = pd.read_csv("G:\My Drive\Python\MovieLens\ml-latest-small\ml-latest-small\mratings.csv")
ratings.info
ratings.head()

#Tags dataset
tags = pd.read_csv("MovieLens\ml-latest-small\ml-latest-small\mtags.csv")
tags.info
tags.head()

#Getting information about dataset
movies.describe() #9742 values

#Selecting from dataset
tags.head()
tags["tag"].head()
tags_impcolumns = ['movieId', 'tag']
tags[tags_impcolumns].iloc[10] #10th index in tags dataset has movieId 431 and tag Al Pacino

movies.head(10) #First 10 indexes
movies_impcolumns = ['movieId', 'title']
movies[movies_impcolumns].iloc[10] #10th index in movies dataset

compare = datacompy.Compare(tags,movies,join_columns="movieId", df1_name = tags, df2_name= movies)
print(compare.report(50)) #Comparison report between tags and movies dataset, joined on movieId column
print(compare.count_matching_rows()) #1572 matching movieIds

#Filtering data
ratings.head(50)
#Selecting movies with ratings greater than 3.0
good_movies = ratings[ratings.rating > 3.0]
good_movies #61716
ratings #100836
good_percent = (good_movies.count()/ratings.count()) * 100
good_percent #61.204332% of movies have a rating above 3.0

#Splitting and Grouping Different Datasets
ratings.head()
ratings_per_user = ratings["movieId"].groupby(ratings["userId"])#Ratings grouped by User ID
ratings_per_user.count() 
#610 Ratings per user

#Average rating per movie
rating_per_movie = ratings["rating"].groupby(ratings["movieId"]) #Ratings grouped by Movie ID
rating_per_movie.head()
average_rating_per_movie = rating_per_movie.mean()
average_rating_per_movie
average_rating_per_movie.mean() #Average of the average rating = 3.2624482748109656
#Best Rated Movies via ID
highest_rating = average_rating_per_movie.max()
highest_rating
best_movies = average_rating_per_movie[average_rating_per_movie == highest_rating] #Best movies are the movies that have an average rating equal to the highest rating
best_movies #296 movies 
#Best Rated Movies via Title
movies.head()
best_movies_titled = movies[movies.movieid.isin(best_movies)].title
best_movies_titled #Best Movie based on Average Rating: Father of the Bride Part II (1995)
