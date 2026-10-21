-- Remove nc_plus_one if it already exists.
DROP DATABASE IF EXISTS nc_plus_one;

-- Create a fresh nc_plus_one database.
CREATE DATABASE nc_plus_one;

-- Connect to the database.
\c nc_plus_one