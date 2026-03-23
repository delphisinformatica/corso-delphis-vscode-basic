CREATE TABLE hello_world (
    id SERIAL PRIMARY KEY,
    message VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO hello_world (message) 
VALUES ('Hello, World!');

INSERT INTO hello_world (message) 
VALUES ('Welcome to PostgreSQL and DBeaver!');

INSERT INTO hello_world (message) 
VALUES ('Databases are fun!');

SELECT * FROM hello_world;