-- Create the database if it doesn't exist

CREATE DATABASE IF NOT EXISTS library_catalog;

-- Use the database

USE library_catalog;

-- Create the books table

CREATE TABLE
    IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        publication_year INT,
        category VARCHAR(255),
        description TEXT,
        rating FLOAT
    );

-- Create the members table

CREATE TABLE
    IF NOT EXISTS members (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        join_date DATE
    );

CREATE TABLE
    IF NOT EXISTS ratings (
        id int AUTO_INCREMENT PRIMARY KEY,
        member_id INT NOT NULL,
        rating INT NOT NULL,
        book_id INT NOT NULL
    );