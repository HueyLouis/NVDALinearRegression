# NVDALinearRegression

As a data analyst, I created many visualization using linear regression models. This was a very basic version that was the basis for a lot of my other work.

This Python code performs linear regression on a dataset using the scikit-learn library. The dataset is loaded from a CSV file using pandas, and the linear regression model is created using the LinearRegression class from scikit-learn.

## Dependencies
- pandas
- numpy
- matplotlib
- scikit-learn

## Usage
1. Install the required dependencies using pip:

```bash
pip install pandas numpy matplotlib scikit-learn
```
2. Download the data in csv format and save it in the **Data** folder.
3. Run the Python script:

## Explanation
The code first loads the dataset from the CSV file using pandas. The dates in the dataset are converted to datetime format using the **pd.to_datetime()** function. The data is then prepared for linear regression by selecting the **position** column as the independent variable **X** and the **adjClose** column as the dependent variable **y**. The **LinearRegression()** class from scikit-learn is used to create a linear regression model, which is then fit to the data using the **fit()** method.

The code then generates predictions for the next 100 steps using the **predict()** method of the linear regression model. The predictions are plotted along with the actual data using matplotlib.
