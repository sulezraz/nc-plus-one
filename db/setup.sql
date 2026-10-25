-- Remove nc_plus_one if it already exists.
DROP DATABASE IF EXISTS nc_plus_one;

-- Create a fresh nc_plus_one database.
CREATE DATABASE nc_plus_one;

-- Connect to the database.
\c nc_plus_one


-- Workflow
-- Initial setup: One time only to set up the database
-- Run setup.sql → Run seed()

-- Later resets:
-- Run seed()

-- Normal application use:
-- Connect to the existing database
