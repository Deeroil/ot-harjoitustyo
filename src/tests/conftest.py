from init_db import initialize_database


def pytest_configure():
    initialize_database()

if __name__ == "__main__":
    pytest_configure()