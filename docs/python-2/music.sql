CREATE TABLE genre (
    genre_name              VARCHAR(100)    PRIMARY KEY,
    genre_number_of_listeners       INT     NOT NULL
);

CREATE TABLE album (
    album_name          VARCHAR(100)    PRIMARY KEY,
    album_year          INT             NOT NULL
);

CREATE TABLE song (
    song_name           VARCHAR(100)    PRIMARY KEY,
    song_year           INT             NOT NULL,
    song_album          VARCHAR(100),
    song_genre          VARCHAR(100)    NOT NULL,
    FOREIGN KEY (song_album) REFERENCES album(album_name)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (song_genre) REFERENCES genre(genre_name)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE record_label (
    record_label_name               VARCHAR(100)    PRIMARY KEY,
    record_label_revenue            INT             NOT NULL,
    record_label_origin_country     VARCHAR(100)    NOT NULL
);

CREATE TABLE artist (
    artist_name             VARCHAR(100)    PRIMARY KEY,
    artist_country          VARCHAR(100)    NOT NULL,
    artist_record_label     VARCHAR(100),
    FOREIGN KEY (artist_record_label) REFERENCES record_label(record_label_name)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE sings (
    sings_artist    VARCHAR(100)    NOT NULL,
    sings_song      VARCHAR(100)    NOT NULL,
    PRIMARY KEY (sings_artist, sings_song),
    FOREIGN KEY (sings_artist) REFERENCES artist(artist_name)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sings_song) REFERENCES song(song_name)
        ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO genre VALUES
('hip-hop', 156),
('rock', 132),
('pop', 81),
('country', 49),
('latin', 38),
('electronic', 22),
('jazz', 6),
('classical', 6);

INSERT INTO album VALUES
('DAMN.', 2017),
('Melodrama', 2017),
('Everybody', 2017),
('1989', 2014),
('Life Changes', 2017),
('Abbey Road', 1969),
('The Aviary', 2017);

INSERT INTO song VALUES
('DNA.', 2017, 'DAMN.', 'hip-hop'),
('ELEMENT.', 2017, 'DAMN.', 'hip-hop'),
('FEEL.', 2017, 'DAMN.', 'hip-hop'),
('LOYALTY.', 2017, 'DAMN.', 'hip-hop'),
('HUMBLE.', 2017, 'DAMN.', 'hip-hop'),
('LOVE.', 2017, 'DAMN.', 'hip-hop'),
('Green Light', 2017, 'Melodrama', 'pop'),
('Sober', 2017, 'Melodrama', 'pop'),
('Homemade Dynamite', 2017, 'Melodrama', 'pop'),
('Liability', 2017, 'Melodrama', 'pop'),
('Hallelujah', 2017, 'Everybody', 'hip-hop'),
('Everybody', 2017, 'Everybody', 'hip-hop'),
('Mos Definitely', 2017, 'Everybody', 'hip-hop'),
('1-800-272-8255', 2017, 'Everybody', 'hip-hop'),
('Anziety', 2017, 'Everybody', 'hip-hop'),
('Welcome to New York', 2014, '1989', 'pop'),
('Blank Space', 2014, '1989', 'pop'),
('Shake It Off', 2014, '1989', 'pop'),
('Bad Blood', 2014, '1989', 'pop'),
('Wildest Dreams', 2014, '1989', 'pop'),
('How You Get The Girl', 2014, '1989', 'pop'),
('Craving You', 2017, 'Life Changes', 'country'),
('Unforgettable', 2017, 'Life Changes', 'country'),
('Sixteen', 2017, 'Life Changes', 'country'),
('Marry Me', 2017, 'Life Changes', 'country'),
('Come Together', 1969, 'Abbey Road', 'rock'),
('Something', 1969, 'Abbey Road', 'rock'),
('I Want You', 1969, 'Abbey Road', 'rock'),
('Here Comes The Sun', 1969, 'Abbey Road', 'rock'),
('Hey Alligator', 2017, 'The Aviary', 'electronic'),
('Girls On Boys', 2017, 'The Aviary', 'electronic'),
('Tell Me You Love Me', 2017, 'The Aviary', 'electronic'),
('Hunter', 2017, 'The Aviary', 'electronic'),
('Love On Me', 2017, 'The Aviary', 'electronic'),
('No Money', 2017, 'The Aviary', 'electronic'),
('Closer', 2016, NULL, 'pop'),
('Roses', 2015, NULL, 'pop'),
('Don''t Let Me Down', 2016, NULL, 'pop'),
('Something Just Like This', 2017, NULL, 'pop');


INSERT INTO record_label VALUES
('Top Dawg Entertainment', 125, 'United States'),
('Universal Music Group', 150, 'United States'),
('Def Jam Recordings', 180, 'United States'),
('Big Machine Records', 130, 'United States'),
('Big Beat Records', 78, 'United States'),
('Sony Music Entertainment', 85, 'United States'),
('RCA Records', 50, 'United States'),
('Parlophone', 70, 'Germany');

INSERT INTO artist VALUES
('Kendrick Lamar', 'United States', 'Top Dawg Entertainment'),
('Lorde', 'New Zealand', 'Universal Music Group'),
('Logic', 'United States', 'Def Jam Recordings'),
('Taylor Swift', 'United States', 'Big Machine Records'),
('Thomas Rhett', 'United States', 'Big Machine Records'),
('The Beatles', 'United States', NULL),
('Galantis', 'Sweden', 'Big Beat Records'),
('The Chainsmokers', 'United States', 'Sony Music Entertainment'),
('Rihanna', 'Barbados', 'Def Jam Recordings'),
('Alessia Cara', 'Canada', 'Def Jam Recordings'),
('Khalid', 'United States', 'RCA Records'),
('Coldplay', 'United Kingdom', 'Parlophone');

INSERT INTO sings VALUES
('Kendrick Lamar', 'DNA.'),
('Kendrick Lamar', 'ELEMENT.'),
('Kendrick Lamar', 'FEEL.'),
('Kendrick Lamar', 'LOYALTY.'),
('Rihanna', 'LOYALTY.'),
('Kendrick Lamar', 'HUMBLE.'),
('Kendrick Lamar', 'LOVE.'),
('Lorde', 'Green Light'),
('Lorde', 'Sober'),
('Lorde', 'Homemade Dynamite'),
('Lorde', 'Liability'),
('Lorde', 'Hallelujah'),
('Logic', 'Everybody'),
('Lorde', 'Mos Definitely'),
('Logic', '1-800-272-8255'),
('Alessia Cara', '1-800-272-8255'),
('Khalid', '1-800-272-8255'),
('Logic', 'Anziety'),
('Taylor Swift', 'Welcome to New York'),
('Taylor Swift', 'Blank Space'),
('Taylor Swift', 'Shake It Off'),
('Taylor Swift', 'Bad Blood'),
('Kendrick Lamar', 'Bad Blood'),
('Taylor Swift', 'Wildest Dreams'),
('Taylor Swift', 'How You Get The Girl'),
('Thomas Rhett', 'Craving You'),
('Thomas Rhett', 'Unforgettable'),
('Thomas Rhett', 'Sixteen'),
('Thomas Rhett', 'Marry Me'),
('The Beatles', 'Come Together'),
('The Beatles', 'Something'),
('The Beatles', 'I Want You'),
('The Beatles', 'Here Comes The Sun'),
('Galantis', 'Hey Alligator'),
('Galantis', 'Girls On Boys'),
('Galantis', 'Tell Me You Love Me'),
('Galantis', 'Hunter'),
('Galantis', 'Love On Me'),
('Galantis', 'No Money'),
('The Chainsmokers', 'Closer'),
('The Chainsmokers', 'Roses'),
('The Chainsmokers', 'Don''t Let Me Down'),
('The Chainsmokers', 'Something Just Like This'),
('Coldplay', 'Something Just Like This');
