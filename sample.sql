DROP TABLE IF EXISTS friend;

CREATE TABLE friend (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    email TEXT NOT NULL,
    extra_data TEXT NULL
);

INSERT INTO friend (last_name, first_name, date_of_birth, email, extra_data) VALUES
    ('Doe', 'John', '1982/10/08', 'john.doe@foobar.com', NULL),
    ('Ann', 'Mary', '1975/09/11', 'mary.ann@foobar.com', '{"phone": "123456789"}'
);
