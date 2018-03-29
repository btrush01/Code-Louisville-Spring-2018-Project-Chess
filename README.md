#Does Capturing First in Chess Give Players an Advantage?

    ###Requirements:
        You will need Bokeh installed to run this Python file, because it generates a simple pie chart graphic.

    ###Instructions:
        Run the Python file, and a new file calles "pie,html" should be generated. Open it with your preferred browser
        to see the distribution of data in a pie chart.

    ###About, Procedure, and Conclusion:
            This project uses data from a CSV file containing 20,000 games played on the website Lichess to attempt
        to answer the simple question above. I chose to exclude games that ended because players ran out of time,
        and also games that were either draws, or won without a piece being captured, because I only wanted to compare
        games that were definitely won/lost, IE, there was a checkmate, or a player resigned. this turned out to
        eliminate nearly 4,000 games from the original sample.

            Of the remaining 16,000 games, I found that, (rounded to the nearest tenth of a percent,) a player who
        captures a piece first goes on to win the game 53.7% of the time, while a player who doesn't goes on to win the
        remaining 46.3% of the time. The data then seems to support a slight edge to more aggressive play.

            Further investigation into this matter could determine if there is a difference between groups of players in
        different rating ranges. Also, which chess openings are more commonly associated a first capture may indicate
        which are most aggressive, and since aggressive play seems to have an advantage, more aggressive openings may
        logically also have an advantage. Finally, if a first capture is more commonly associated with White than Black
        could offer an additional explanation as to why it is commonly accepted White has a slight edge in Chess. Since
        White moves first, White may also be in a better position to capture first.

        However, such questions are outside the scope of this study at this time. Therefore, I can only conclude that in
        the broad picture of all games sampled, capturing first gives a player a slight advantage.
