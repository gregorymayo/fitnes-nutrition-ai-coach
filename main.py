from routines import build_weekday_routine, build_weekend_routine, build_holiday_routine

def main():
    while True:
        print("\nWelcome to the Fitness And Nutrition AI Coach!\n")
        print("Choose an option:")
        print("1. Build routines for the weekday")
        print("2. Build routines for the weekend")
        print("3. Build routines for the holiday")
        print("0. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            routine = build_weekday_routine()
        elif choice == '2':
            routine = build_weekend_routine()
        elif choice == '3':
            routine = build_holiday_routine()
        elif choice == '0':
            break
        else:
            print("Invalid choice")
            continue

        print("\nHere's your personalized routine:")
        print(routine)

if __name__ == "__main__":
    main()
