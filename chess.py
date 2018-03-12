import csv
import sqlite3

with open('games.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)


    conn = sqlite3.connect("mydb.sqlite")
    cur = conn.cursor()
    cur.execute("drop table if exists Lichess_10k_Games_Dataset;")
    cur.execute("""
    create table if not exists Lichess_10k_Games_Dataset(
          id varchar(100)
         ,rated varchar(100)
         ,created_at varchar(100)
         ,last_move_at varchar(100)
         ,turns varchar(100)
         ,victory_status varchar(100)
         ,winner varchar(100)
         ,increment_code varchar(100)
         ,white_id(100)
         ,white_rating(100)
         ,black_id varchar(100)
         ,black_rating varchar(100)
         ,moves varchar(100)
         ,opening_eco varchar(100)
         ,opening_name varchar(100)
         ,opening_ply varchar(100)
    );
    """)

    #this allows me to skip the first line in file, which are column headers
    headerline = True

    for record in csv_reader:
        if headerline:
            headerline = False

        else:
            cur.execute("INSERT INTO Lichess_10k_Games_Dataset(id,rated,created_at,last_move_at,turns,victory_status,winner,increment_code,white_id,white_rating,black_id,black_rating,moves,opening_eco,opening_name,opening_ply) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (record))



    cur.execute("select * from Lichess_10k_Games_Dataset;").fetchmany(3)