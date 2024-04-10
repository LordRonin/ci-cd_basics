from conftest import mssql_connection


def test_revision_min_max(mssql_connection):
    with mssql_connection.cursor(as_dict=True) as cursor:
        cursor.execute(
            '''
            SELECT MIN(Revision) min_revision,
                MAX(Revision) max_revision
            FROM Production.Document
            '''
        )
        row = cursor.fetchone()

    assert int(row['min_revision']) >= 0, 'Invalid revision'
    assert int(row['max_revision']) >= 0, 'Invalid revision'


def test_top_hierarchy_folder(mssql_connection):
    with mssql_connection.cursor(as_dict=True) as cursor:
        cursor.execute(
            '''
SELECT DocumentLevel,
    Title,
    FolderFlag
FROM Production.Document
WHERE Title = 'Documents'
            '''
        )
        row = cursor.fetchone()

    assert int(row['DocumentLevel']) == 0, 'Not top hierarchy'
    assert int(row['FolderFlag'] == 1), 'Not a folder'
