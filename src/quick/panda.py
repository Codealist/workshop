def show_table(dataframe, head=False):
    if head:
        dataframe.head()
    else:
        dataframe.info()
