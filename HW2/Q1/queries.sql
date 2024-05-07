SELECT FLOOR(AvgRating) as RatingBin, COUNT(*) as MovieCount
FROM (
    SELECT Movie_FK, AVG(Rating) as AvgRating, COUNT(Rating) as TotalVotes
    FROM Ratings
    GROUP BY Movie_FK
    HAVING COUNT(Rating) >= 1000
) as FilteredMovies
GROUP BY FLOOR(AvgRating);
