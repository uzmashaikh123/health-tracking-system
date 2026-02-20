import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# File path
DATA_FILE = 'data/health_data.csv'

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# Initialize data file
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['Date', 'Exercise (min)', 'Water (L)', 'Sleep (hrs)', 'Calories'])
    df.to_csv(DATA_FILE, index=False)


def add_entry():
    """Add a new health entry."""
    date = datetime.now().strftime("%Y-%m-%d")
    print(f"\n📅 Date: {date}")

    exercise = float(input("🏃 Exercise (minutes): "))
    water = float(input("💧 Water (liters): "))
    sleep = float(input("😴 Sleep (hours): "))
    calories = float(input("🍎 Calories consumed: "))

    df = pd.read_csv(DATA_FILE)
    new_data = pd.DataFrame([[date, exercise, water, sleep, calories]],
                            columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print("\n✅ Entry added successfully!\n")


def view_summary():
    """View health statistics."""
    df = pd.read_csv(DATA_FILE)

    if df.empty:
        print("\n⚠️ No data found!\n")
        return

    print("\n📊 Weekly Health Summary:")
    print(df.tail(7))

    print("\n📈 Average Stats (Last 7 Days):")
    print(df.tail(7).mean(numeric_only=True))


def plot_progress():
    """Visualize health progress."""
    df = pd.read_csv(DATA_FILE)

    if df.empty:
        print("\n⚠️ No data for plotting!\n")
        return

    df['Date'] = pd.to_datetime(df['Date'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Exercise (min)'], label='Exercise (min)', marker='o')
    plt.plot(df['Date'], df['Water (L)'], label='Water (L)', marker='o')
    plt.plot(df['Date'], df['Sleep (hrs)'], label='Sleep (hrs)', marker='o')
    plt.plot(df['Date'], df['Calories'], label='Calories', marker='o')
    plt.title("Health Tracker Progress")
    plt.xlabel("Date")
    plt.ylabel("Measurements")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    """Main menu for the health tracker."""
    while True:
        print("\n=== 🩺 Health Tracker Menu ===")
        print("1. Add New Entry")
        print("2. View Weekly Summary")
        print("3. Show Health Progress Chart")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            plot_progress()
        elif choice == '4':
            print("\n👋 Exiting Health Tracker. Stay healthy!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
