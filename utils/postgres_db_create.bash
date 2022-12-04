#!/usr/bin/env bash
sudo -u postgres psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE crowdcontent_db;
    CREATE USER crowdcontent_user WITH PASSWORD 'password';
    ALTER ROLE crowdcontent_user SET client_encoding TO 'utf8';
    ALTER ROLE crowdcontent_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE crowdcontent_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE crowdcontent_db TO crowdcontent_user;
    ALTER USER crowdcontent_user CREATEDB;
EOSQL
