DB_FILE="pill_reminder_db.db"

SCHEMA_FILE="sql_scripts/schema_setup.sql"
SEED_FILE="sql_scripts/seed_data.sql"

if sqlite3 "$DB_FILE" <<EOF
PRAGMA foreign_keys = ON;
.read $SCHEMA_FILE
.read $SEED_FILE
EOF
then
    echo "Database created successfully."
else:
    echo "Database was not created successfully."
fi