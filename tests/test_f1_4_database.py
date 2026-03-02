import sqlite3
import pytest

def test_sqlite_level_reduction():
    # In-memory SQLite database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE levelling_data (
            id INTEGER PRIMARY KEY,
            point_id TEXT,
            backsight REAL,
            foresight REAL,
            known_elevation REAL
        )
    ''')
    
    # Insert data
    cursor.execute('''
        INSERT INTO levelling_data (point_id, backsight, foresight, known_elevation)
        VALUES ('A', 1.5, 1.2, 10.0)
    ''')
    
    # Calculate new elevation
    cursor.execute('''
        SELECT point_id, (known_elevation + backsight - foresight) AS new_elevation
        FROM levelling_data
    ''')
    
    result = cursor.fetchone()
    assert result[0] == 'A'
    assert abs(result[1] - 10.3) < 1e-4

    conn.close()

try:
    import duckdb
    HAS_DUCKDB = True
except ImportError:
    HAS_DUCKDB = False

@pytest.mark.skipif(not HAS_DUCKDB, reason="DuckDB is not installed")
def test_duckdb_level_reduction():
    # In-memory DuckDB database
    conn = duckdb.connect(':memory:')
    
    # Create table and insert data
    conn.execute('''
        CREATE TABLE levelling_data (
            point_id VARCHAR,
            backsight DOUBLE,
            foresight DOUBLE,
            known_elevation DOUBLE
        )
    ''')
    conn.execute('''
        INSERT INTO levelling_data VALUES ('B', 2.0, 1.0, 15.0)
    ''')
    
    # Calculate new elevation
    result = conn.execute('''
        SELECT point_id, (known_elevation + backsight - foresight) AS new_elevation
        FROM levelling_data
    ''').fetchone()
    
    assert result[0] == 'B'
    assert abs(result[1] - 16.0) < 1e-4

