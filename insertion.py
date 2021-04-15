import pymysql
import pandas as pd

connection = pymysql.connect(host="localhost",user= "ashna03",password= "password", database="movie_project");
cursor = connection.cursor();

df = pd.read_csv('imdb_movie_list.csv')
print( df.head())
for row in df.index:
    tid = df['tconst'][row]
    title_type = df['titleType'][row]
    year_release = int(df['year'][row])
    #year_release=str(2000)
    primary_title = df['primaryTitle'][row]
    
    run_time= int(df['runtimeMinutes'][row])
    genres= df['genres'][row]
    average_rating=float( df['averageRating'][row])
    num_votes = int(df['numVotes'][row])
    #cursor.execute(''' Insert into movie_ratings values (%s, %s, %s, %s,%s, %s, %s, %s)''', (tid, title_type, year_release, primary_title, run_time, genres, average_rating, num_votes))
    sql = ''' Insert into movie_ratings values (%s, %s, %s, %s,%s, %s, %s, %s)''' 
    val = (tid, title_type,year_release,primary_title,run_time,genres,average_rating,num_votes)
    cursor.execute(sql,val)
    connection.commit()
