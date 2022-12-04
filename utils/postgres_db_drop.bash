#!/usr/bin/env bash
sudo -u postgres psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    DROP DATABASE IF EXISTS crowdcontent_db;
    DROP DATABASE IF EXISTS test_crowdcontent_db;
    DROP USER IF EXISTS crowdcontent_user;
    DROP USER IF EXISTS test_crowdcontent_db;
EOSQL
