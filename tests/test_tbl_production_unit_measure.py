from conftest import mssql_connection


def test_name_uniqueness(mssql_connection):
    with mssql_connection.cursor() as cursor:
        cursor.execute('SELECT Name '
                       'FROM Production.UnitMeasure '
                       'GROUP BY Name '
                       'Having Count(Name) > 1')
        rows = cursor.fetchall()

    assert not rows, 'Duplicated UnitMeasure Names'


def test_codes_names_count(mssql_connection):
    with mssql_connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(DISTINCT UnitMeasureCode), '
                       'COUNT(DISTINCT Name) '
                       'FROM Production.UnitMeasure')
        codes_count, names_count = cursor.fetchone()

    assert codes_count == names_count, 'Count of Codes does not match count of Names'
