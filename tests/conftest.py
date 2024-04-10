import pymssql
import pytest


@pytest.fixture(scope="session")
def mssql_connection():
    server = 'localhost'
    database = 'AdventureWorks2012'
    login = 'TestLogin'
    password = '!password12345'
    port = 1433

    try:
        conn = pymssql.connect(server, login, password, database, port=1433)
    except:
        server = 'host.docker.internal'
        conn = pymssql.connect(server, login, password, database, port=1433)
    # Yield database connection object to query database.
    yield conn

    # Close connection after test executions.
    conn.close()
