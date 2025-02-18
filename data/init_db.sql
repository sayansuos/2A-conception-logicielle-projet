-----------------------------------------------------
-- User
-----------------------------------------------------
CREATE TABLE IF NOT EXISTS users_data (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    pseudo      TEXT,
    mdp         VARCHAR
);

----------------------------------------------------
-- Champions
-----------------------------------------------------
CREATE TABLE IF NOT EXISTS champs_data (
    id     INTEGER PRIMARY KEY,
    name   TEXT
);

-----------------------------------------------------
-- Items
-----------------------------------------------------
CREATE TABLE IF NOT EXISTS items_data (
    id     INTEGER PRIMARY KEY,
    name   TEXT
);

-----------------------------------------------------
-- Builds
-----------------------------------------------------
CREATE TABLE IF NOT EXISTS builds_data (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    champ_id    INTEGER,
    item1_id    INTEGER,
    item2_id    INTEGER,
    item3_id    INTEGER,
    item4_id    INTEGER,
    item5_id    INTEGER,
    FOREIGN KEY (champ_id) REFERENCES champs_data(id) ON DELETE CASCADE,
    FOREIGN KEY (item1_id) REFERENCES items_data(id) ON DELETE CASCADE,
    FOREIGN KEY (item2_id) REFERENCES items_data(id) ON DELETE CASCADE,
    FOREIGN KEY (item3_id) REFERENCES items_data(id) ON DELETE CASCADE,
    FOREIGN KEY (item4_id) REFERENCES items_data(id) ON DELETE CASCADE,
    FOREIGN KEY (item5_id) REFERENCES items_data(id) ON DELETE CASCADE
);

-----------------------------------------------------
-- User's builds
-----------------------------------------------------
CREATE TABLE IF NOT EXISTS users_builds_data (
    user_id     INTEGER,
    build_id    INTEGER,
    PRIMARY KEY (user_id, build_id),
    FOREIGN KEY (user_id) REFERENCES users_data(id) ON DELETE CASCADE,
    FOREIGN KEY (build_id) REFERENCES builds_data(id) ON DELETE CASCADE
);
