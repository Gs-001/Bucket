def create_transaction():
    print("Create Transaction")
    "CREATE TABLE Transactions (id SERIAL PRIMARY KEY, title VARCHAR, payment_mode VARCHAR(100), amount INTEGER NOT NULL, nature varchar(50) NOT NULL, date DATE NOT NULL, category varchar(100), created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(category) REFERENCES Category(title))"