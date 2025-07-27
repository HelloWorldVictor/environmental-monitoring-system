from cli import print_header
from db_handler import initialize_db


def main():
    """Main function to run the Environmental Monitory system CLI."""
    initialize_db()

    print_header()
    pass


if __name__ == "__main__":
    main()
