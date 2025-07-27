from cli import (
    handle_fetch_data,
    handle_query_historical,
    handle_set_thresholds,
    handle_show_latest,
    handle_view_tips,
    print_header,
    print_menu,
)
from db_handler import initialize_db


def main():
    """Main function to run the Environmental Monitory system CLI."""
    initialize_db()

    print_header()
    while True:
        print_menu()
        choice = input("Choose (1–6): ")

        if choice == "1":
            handle_fetch_data()
        elif choice == "2":
            handle_show_latest()
        elif choice == "3":
            handle_query_historical()
        elif choice == "4":
            handle_set_thresholds()
        elif choice == "5":
            handle_view_tips()
        elif choice == "6":
            print("\nExiting. Stay safe!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
