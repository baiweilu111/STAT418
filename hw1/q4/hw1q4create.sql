CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_name TEXT NOT NULL
);


CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_id INTEGER NOT NULL,
    sale_amount REAL NOT NULL,
    sale_date TEXT NOT NULL,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);