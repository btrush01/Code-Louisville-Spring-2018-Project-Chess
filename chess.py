import csv
import sqlite3
from bokeh.plotting import *
from bokeh.charts import Donut
import pandas as pd


with open('games.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    #MyList = csv.reader(csvfile.text.strip().split('\n'))
    #the_whole_file = list(csv_reader)

    conn = sqlite3.connect("mydb.sqlite")
    cur = conn.cursor()
    cur.execute("drop table if exists Games;")
    cur.execute("""
    create table if not exists Games(
        id varchar(100)
       ,rated Boolean
       ,created_at varchar(100)
       ,last_move_at varchar(100)
       ,turns integer
       ,victory_status varchar(100)
       ,winner varchar(100)
       ,increment_code varchar(100)
       ,white_id varchar(100)
       ,white_rating integer
       ,black_id varchar(100)
       ,black_rating integer
       ,moves varchar(100)
       ,opening_eco varchar(100)
       ,opening_name varchar(100)
       ,opening_ply integer
    );
    """)
    cur.execute("drop table if exists Moves;")
    cur.execute("""
    create table if not exists Moves(
        id integer
       ,game_id varchar(100)
       ,sequence integer
       ,move varchar(10)
    );
    """)


    #this allows me to skip the first line in file, which are column headers
    headerline = True
    count=0

    for record in csv_reader:
        if headerline:
            headerline = False

        else:
            game_id = record[0]
            moves = record[12]

            # define a counter variable and set it to 0
            i=0
            for move in moves.split(" "): #loop over the output of moves.split
                i+=1
                count+=1
                cur.execute("INSERT INTO Moves(id, game_id, sequence, move) VALUES(?,?,?,?)", (count, game_id, i, move))
                # increment counter

            cur.execute("INSERT INTO Games(id,rated,created_at,last_move_at,turns,victory_status,winner,increment_code,white_id,white_rating,black_id,black_rating,moves,opening_eco,opening_name,opening_ply) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (record))

    ##### Data is imported

    my_results = []
    t = 0
    f = 0


    games = cur.execute("""
                        select game_id, min(sequence), winner from Moves m
                        join Games g on m.game_id = g.id where victory_status not in ('outoftime', 'draw') and m.move like '%x%'
                        group by m.game_id
                        """).fetchall()
    for first_capture in games:
        #find minimum capture move % 2 for side color, even is black, odd is white, set min_capture = result

        if first_capture is not None:

            sequence = first_capture[1]
            winner = first_capture[2]

            if sequence % 2 == 0:
                min_capture = "black"
            else:
                min_capture = "white"
            #if winner = min_capture t+=1, else f+=1
            if winner == min_capture:
                t+=1
            else:
                f+=1

    result = [t,f]
    my_results.append(result)


    conn.commit()
    cur.close()
    conn.close()


    series = pd.Series([result[0], result[1]], index=('Captured 1st and Won', 'Didn\'t Capture 1st and Won'))
    p = Donut(series, title="First Capture vs Victor", hover_text='Total Games')
    # display/save everything
    output_file("pie.html")
    show(p)
