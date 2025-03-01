import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # Update with your project name
django.setup()

from django.db import connection
from api.models import Post, Category  # Import models after django.setup()

# Function to delete all records and reset auto-increment
def reset_table(model):
    table_name = model._meta.db_table

    # Delete all records
    model.objects.all().delete()
    print(f"🗑️ Deleted all records from {table_name}.")

    # Reset auto-increment
    with connection.cursor() as cursor:
        if connection.vendor == 'postgresql':
            sequence_name = f"{table_name}_id_seq"
            cursor.execute(f"ALTER SEQUENCE {sequence_name} RESTART WITH 1;")
            print(f"✅ PostgreSQL: Auto-increment reset for {table_name}.")
        elif connection.vendor == 'mysql':
            cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")
            print(f"✅ MySQL/MariaDB: Auto-increment reset for {table_name}.")
        elif connection.vendor == 'sqlite':
            cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}';")
            print(f"✅ SQLite: Auto-increment reset for {table_name}.")
        else:
            print("❌ Unsupported database type.")

# Reset tables
for model in [Post, Category]:
    reset_table(model)