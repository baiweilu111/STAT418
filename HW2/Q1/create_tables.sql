CREATE TABLE Movies (
    MovieTitle VARCHAR(255),
    ReleaseYear INT,
    PlotDescription TEXT,
    Genre VARCHAR(100),
    AverageRating DECIMAL(3,1),
    NumberOfVotes INT
);



CREATE TABLE Ratings (
    User_FK INT,
    Movie_FK INT,
    Rating DECIMAL(3,1),
    FOREIGN KEY (User_FK) REFERENCES Users(UserID),
    FOREIGN KEY (Movie_FK) REFERENCES Movies(MovieID)
);

CREATE TABLE Users (
    Username VARCHAR(255) PRIMARY KEY,
    First_Name VARCHAR(255),
    Last_Name VARCHAR(255)
);
