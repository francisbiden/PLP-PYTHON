import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load the dataset
    file_path = 'pokemon_data.csv'
    df = pd.read_csv(file_path)

    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Explore the structure of the dataset
    print("\nDataset Information:")
    print(df.info())

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Clean the dataset (filling missing values for simplicity)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    print("\nMissing values filled (if any).")

except FileNotFoundError:
    print("Error: The specified file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Grouping by a categorical column and computing mean
    if 'Type 1' in df.columns:
        group_mean = df.groupby('Type 1')['Attack'].mean()
        print("\nMean Attack by Type 1:")
        print(group_mean)

        # Interesting findings (example)
        print("\nInteresting Findings:")
        print(f"The Pokémon type with the highest mean Attack is '{group_mean.idxmax()}' with {group_mean.max():.2f} Attack.")

except KeyError as e:
    print(f"KeyError: {e}. Ensure the dataset contains the necessary columns.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 3: Data Visualization
try:
    # Line Chart (example using Attack over a hypothetical index)
    plt.figure(figsize=(10, 6))
    plt.plot(df['Attack'], label='Attack', color='blue')
    plt.title('Trend of Attack Values')
    plt.xlabel('Index')
    plt.ylabel('Attack')
    plt.legend()
    plt.show()

    # Bar Chart
    if 'Type 1' in df.columns:
        plt.figure(figsize=(10, 6))
        group_mean.plot(kind='bar', color='orange')
        plt.title('Average Attack by Pokémon Type')
        plt.xlabel('Type 1')
        plt.ylabel('Average Attack')
        plt.xticks(rotation=45)
        plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['Defense'], bins=15, color='green', edgecolor='black')
    plt.title('Distribution of Defense Values')
    plt.xlabel('Defense')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter Plot
    if 'HP' in df.columns and 'Attack' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df['HP'], y=df['Attack'], hue=df['Type 1'], palette='viridis')
        plt.title('HP vs Attack by Type 1')
        plt.xlabel('HP')
        plt.ylabel('Attack')
        plt.legend(title='Type 1', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

except Exception as e:
    print(f"An error occurred during visualization: {e}")
