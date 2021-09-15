#!/bin/sh
flask db stamp head -d migrations_local
flask db migrate -m "first migration" -d migrations_local