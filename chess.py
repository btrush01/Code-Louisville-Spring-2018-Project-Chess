import csv
import sqlite3


count=0

with open('games.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    #the_whole_file = list(csv_reader)

    conn = sqlite3.connect("mydb.sqlite")
    cur = conn.cursor()
    cur.execute("drop table if exists Games_10k;")
    cur.execute("""
    create table if not exists Games_10k(
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

            cur.execute("INSERT INTO Games_10k(id,rated,created_at,last_move_at,turns,victory_status,winner,increment_code,white_id,white_rating,black_id,black_rating,moves,opening_eco,opening_name,opening_ply) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                 (record))
    ##### Data is imported

    my_results = []
    t = 0
    f = 0

    for game in cur.execute("select * from Games_10k where victory_status NOT IN ('outoftime', 'draw')").fetchall():
        # do things with item
        print(game[0])

        #find minimum capture move % 2 for side color, even is black, odd is white, set min_capture = result
        cur.execute("""
        select * from Moves m
        join Games_10k g
            on m.game_id = g.id
        where game_id = ?
            and move like '%x%'
        order by sequence
        limit 1
        """)

        if sequence % 2 == 0:
            min_capture = "black"
        else:
            min_capture = "white"
        #if winner = min_capture t+=1, else f+=1
        if winner == min_capture:
            t+=1
        else:
            f+=1

        result = t/f
        my_results.append(result)


     # for game in games:
        # do science

#     cur.execute("""
#     select * from Moves m
#     join Games_10k g
#         on m.game_id = g.id
#     where game_id = ?
#         and move like '%x%'
#     order by sequence
#     limit 1
#     """, )



    conn.commit()
    cur.close()
    conn.close()

#    cur.execute("SELECT * FROM Lichess_10k_Games_Dataset WHERE victory_status != outoftime;")

#    the_whole_file[row][column]
#    moves_list = moves.split(' ')

#    i=0
#    while i < moves_list.length:
#        i+1
#    else:
#

#    cur.execute("SELECT move_number WHERE move like '%x%'")
#    cur.execute("ORDER BY move_table.move_number LIMIT 1")
