def spark_shape(sdf):
    """
    This function sort of imitates pandas' df.shape().
    It takes a spark dataframe as input and prints the number of rows
    and columns of the dataframe in this format: (rows, columns).
    """

    print("(" + str(sdf.count()) + ", " + str(len(sdf.columns)) + ")")
    return