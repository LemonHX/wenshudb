CREATE TABLE IF NOT EXISTS PINYIN (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    SHENGMU TEXT,
    YUNMU TEXT NOT NULL,
    DIAO INT NOT NULL
);

CREATE TABLE IF NOT EXISTS JYUTPING (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    SHENGMU TEXT,
    YUNMU TEXT NOT NULL,
    YUNWEI TEXT,
    DIAO INT NOT NULL
);

CREATE TABLE IF NOT EXISTS CHAIZI(
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    CHAI TEXT NOT NULL,
    XU INT NOT NULL
);

CREATE TABLE IF NOT EXISTS BIHUA (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT UNIQUE NOT NULL,
    BIHUA INT NOT NULL
);

CREATE TABLE IF NOT EXISTS ZIPIN (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    PINLV TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS BIANTI (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    LEIXING TEXT NOT NULL,
    BIANTI TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS DEFINITION (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    DEFINITION TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS KANGXI (
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    JUAN TEXT NOT NULL,
    BU TEXT NOT NULL,
    YE TEXT NOT NULL,
    YI TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS CIYU (
    ID INTEGER PRIMARY KEY NOT NULL,
    CI TEXT NOT NULL,
    PINYIN TEXT,
    YI TEXT,
    YUAN TEXT,
    LI TEXT
);

CREATE TABLE IF NOT EXISTS XIEHOUYU (
    ID INTEGER PRIMARY KEY NOT NULL,
    XIEHOUYU TEXT NOT NULL,
    JIESHI TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS SHUZI(
    ID INTEGER PRIMARY KEY NOT NULL,
    ZI TEXT NOT NULL,
    LEIXING TEXT NOT NULL,
    SHU INT
);
