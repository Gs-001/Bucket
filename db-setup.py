import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_user",
                        password="db_pass",
                        port="db_port")

cursor = conn.cursor()

"""
Have buckets without goal amount for example: Sat Sang
"""

"""
INSERT INTO Bucket (title, amount, goal_amount, time_interval) 
VALUES 
    ('Masters - USA', 20000, 200000,'0 0 1 * *'),
    ('Travel', 2000, 20000,'0 0 1 * *')
    ('Lifestyle', 2000, 20000,'0 0 1 * *')
    ('Emergency Fund', 1000, 100000,'0 0 1 * *')
"""


"""
CREATE TABLE Bucket (
    title VARCHAR(255) PRIMARY KEY,
    amount INTEGER NOT NULL,
    goal_amount INTEGER,
    time_interval VARCHAR(50),
    created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
)
"""

"""
CREATE TABLE BucketTxns (
    description TEXT,
    bucket VARCHAR(255),
    fulfilled BOOLEAN DEFAULT TRUE,
    created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(bucket) REFERENCES Bucket(title)
)
"""

"""
INSERT INTO Category (title) 
VALUES 
    ('Lifestyle'),
    ('Groceries'),
    ('Essential'),
    ('Recurring')
"""

"""
CREATE TABLE Category (
    title VARCHAR(100) PRIMARY KEY, 
    created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    )
"""

"""
CREATE TABLE Transactions (
    id SERIAL PRIMARY KEY, 
    title VARCHAR, 
    payment_mode VARCHAR(100), 
    amount INTEGER NOT NULL, 
    nature varchar(50) NOT NULL, 
    date DATE NOT NULL, 
    category varchar(100), 
    created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY(category) REFERENCES Category(title)
    )
"""

"""
CREATE TABLE Transaction_Category (
    txn_id INTEGER REFERENCES Transaction(id),
    category_id INTEGER REFERENCES Category(id),
    PRIMARY KEY(category_id, txn_id)
)
"""

