import pymysql

connection =pymysql.connect("localhost", "ashna03", "password", "movie_project");
cursor = connection.cursor();

delete_existing_table = "drop table if exists movie_ratings";
create_table_query = """ Create table movie_ratings(tid varchar(20) PRIMARY KEY, title_type varchar(100), year_release int(4), primary_title varchar(100), runtime int, genres varchar(100), average_rating decimal(2,1), num_votes int) """;


try:
    cursor.execute(delete_existing_table);
    print("Exisiting table has been deleted");
    cursor.execute(create_table_query);
    print("movie_rating table has been created");
except Exception as e:
    print("Exception : ", e);

connection.close();
