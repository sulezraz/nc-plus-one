-- create_database.sql
-- Recreates the nc_plus_one database for initial setup or an intentional full rebuild.

-- Remove the database if it already exists.
DROP DATABASE IF EXISTS nc_plus_one;

-- Create an empty database.
CREATE DATABASE nc_plus_one;

-- Connect this psql session to the new database.
\connect nc_plus_one


-----------

-- RUN FILE:
-- psql -f db/create_database.sql

-- WARNING: Running this file deletes the existing nc_plus_one database.
-- Close application connections to nc_plus_one before running it.

-- ##### WORKFLOW #####

-- Initial setup:
-- Run create_database.sql, then run the Python seed() function.

-- Later development resets:
-- Run seed() to drop tables, recreate them and insert initial data.
-- No database recreation is required.

-- Normal application use:
-- Connect to the existing database without resetting or seeding it.
