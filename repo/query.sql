SELECT * FROM users;
SELECT * FROM posts;
SELECT * FROM votes;


/* Insert data into users table
*/
INSERT INTO users
    (email, "password")
VALUES
    ('user1@localhost.com', 'password123'),
    ('user2@localhost.com', 'password123'),
    ('user3@localhost.com', 'password123')


/* Insert data into posts table
*/
INSERT INTO posts
    (title, "content", owner_id)
VALUES
    ('First Post', 'First Content', 1),
    ('Second Post', 'Second Content', 2),
    ('Third Post', 'Third Content', 3);

INSERT INTO votes
    (post_id, user_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 3)