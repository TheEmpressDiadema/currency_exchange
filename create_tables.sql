-- SQLite
-- creates currency table
CREATE TABLE currency
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    code TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    sign TEXT NOT NULL
);
-- creates exchange_rate table
CREATE TABLE exchange_rate
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    base_currency_id INTEGER NOT NULL,
    target_currency_id INTEGER NOT NULL,
    rate REAL NOT NULL,
    FOREIGN KEY (base_currency_id) REFERENCES currency (id),
    FOREIGN KEY (target_currency_id) REFERENCES currency (id)
);