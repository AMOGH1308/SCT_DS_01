# Population Visualization from 1960 to 2023 for India

This project aims to visualize the continuous distribution of the population for India from 1960 to 2023 using a bar graph.

## Procedure:

1. **Import Required Libraries:**
   - `pandas`: Used for loading the dataset and creating dataframes.
   - `matplotlib`: Used for plotting different types of charts such as bar charts and histograms.

2. **Load the Dataset:**
   - Assign the file path of the dataset to a variable and load the dataset into a Pandas DataFrame.
   
3. **Clean the Data:**
   - Strip any whitespaces in the column names to ensure consistency within the dataframe.

4. **Filter for a Specific Country:**
   - Select the data for India by filtering the dataframe for the country of interest (`India`).

5. **Transpose the Data:**
   - Use the `transpose()` method to convert columns into rows and rows into columns. This helps in restructuring the data where years become the indices.

6. **Plot the Bar Graph:**
   - Plot a bar graph to visualize the population of India for each year from 1960 to 2023.
   - Use `matplotlib` to set up the plot, and customize the graph with titles, axis labels, and tick formatting for better readability.

### Key Functions:
- `pd.read_csv()`: Loads the dataset into a Pandas DataFrame.
- `.str.strip()`: Removes any leading or trailing whitespaces in column names.
- `.set_index()`: Sets the `Country Name` as the index for filtering.
- `.transpose()`: Converts columns to rows, useful for converting years into indices.
- `plt.bar()`: Plots a bar graph representing population data.
- `plt.xticks(rotation=90)`: Rotates the x-axis labels (years) for readability.

### Outcome:
After following the procedure, you will generate a bar graph that shows the population of India from 1960 to 2023, helping visualize population trends over time.
