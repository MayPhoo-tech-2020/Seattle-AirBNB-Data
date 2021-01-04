#Drop columns with greater than percent_to_drop value missing values function
def drop_columns_rows(dataframe_name, percent_to_drop):
    #Drop rows with all missing values
    dataframe_name = dataframe_name.dropna(how='all', axis=0)
    column_names = dataframe_name[dataframe_name.columns
                   [dataframe_name.isnull().mean() > percent_to_drop]]
    return column_names
def sum_columns_values(dataframe_name):
    sum_columns_value = dataframe_name.sum(axis=0)
    return sum_columns_value
def sum_row_values(dataframe_name):
    sum_row_values = dataframe_name.sum(axis=1)
    return sum_row_values

