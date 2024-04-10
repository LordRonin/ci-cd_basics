from conftest import mssql_connection


def test_data_in_table_exists(mssql_connection):
    with mssql_connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM Person.Address')
        rows_count = cursor.fetchone()[0]

    assert rows_count > 0, 'Table is empty.'


def test_valid_state_province_id(mssql_connection):
    with mssql_connection.cursor() as cursor:
        cursor.execute(
            'SELECT AddressID \
            FROM Person.Address \
            WHERE StateProvinceID NOT IN ( \
                SELECT StateProvinceID \
                FROM Person.StateProvince);'
        )
        rows = cursor.fetchall()

    assert not rows, 'Foreign key constraint violation'
