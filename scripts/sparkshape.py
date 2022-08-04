def spark_shape(sdf):
    """
    This function sort of imitates pandas' df.shape().
    It takes a spark dataframe as input and returns the number of rows
    and columns of the dataframe in this tuple format: (rows, columns).
    """
    output = (sdf.count(), len(sdf.columns))

    return output