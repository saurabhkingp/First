from numpy import add
import pandas as pd
from pathlib import Path



def excel_diff(path_OLD, path_NEW): 
    df_OLD = pd.read_excel(path_OLD, sheet_name=2, keep_default_na=False)  
    df_NEW = pd.read_excel(path_NEW, sheet_name=3, keep_default_na=False)
    print('Old '+str(len(df_OLD.columns)))
    print("New "+str(len(df_NEW.columns)))
    
    # if len(df_NEW.columns)> len(df_OLD.columns):
    # x=list(set(df_NEW.columns)-set(df_OLD.columns))
    # x=list((set(df_NEW.columns) | set(df_OLD.columns)) - (set(df_OLD.columns) & set(df_NEW.columns)))
    # for g in x:
    #     df_OLD[g] = ""
    # elif len(df_NEW.columns)< len(df_OLD.columns): 
        # y=list(((set(df_OLD.columns) & set(df_NEW.columns))- set(df_NEW.columns) | set(df_OLD.columns)))
    # y=list(set(df_OLD.columns)-set(df_NEW.columns))
    # for g in y:
    #     df_NEW[g]=''

    added_col=list(set(df_NEW.columns)-set(df_OLD.columns))
    removed_col=list(set(df_OLD.columns)-set(df_NEW.columns))
    key = ["Name", "NeType", "Category"]
    df_OLD = df_OLD.set_index(key)
    df_NEW = df_NEW.set_index(key)
    dfDiff = df_NEW.copy()
    droppedRows = []
    newRows = []
    cols_OLD = df_OLD.columns
    cols_NEW = df_NEW.columns

    sharedCols = list(set(cols_OLD).intersection(cols_NEW))
    col_notin_new=list(set(cols_OLD).difference(cols_NEW))
    col_notin_old=list(set(cols_NEW).difference(cols_OLD))
    print('Col not in old= ',col_notin_old)
    print('Col not in new= ',col_notin_new)
    dfDiff.insert(0, "Comment", '')
    # dfDiff.insert(1, "Added/Removed Columns", '')
    sx=[]
    for row in dfDiff.index:
        if (row in df_OLD.index) and (row in df_NEW.index):
            for col in sharedCols:
                value_OLD = df_OLD.loc[row, col]
                value_NEW = df_NEW.loc[row, col]
                if value_OLD == value_NEW:
                    dfDiff.loc[row, col] = df_NEW.loc[row, col]
                else:
                    sx.append(col)
                    if len(added_col)!=0 and len(removed_col)==0:
                        dfDiff.loc[row,'Comment']='Modified Columns: {}- Added Columns: {} '.format([c for c in sx],added_col)
                    elif len(added_col)!=0 and len(removed_col)!=0:
                        dfDiff.loc[row,'Comment']='Modified Columns: {}- Added Columns: {} -Removed Columns: {}'.format([c for c in sx],added_col,removed_col)
                    elif len(removed_col)!=0 and len(added_col)==0:
                        dfDiff.loc[row,'Comment']='Modified Columns: {}- Removed Columns: {}'.format([c for c in sx],removed_col)
                    elif len(removed_col)==0 and len(added_col)==0:
                        dfDiff.loc[row,'Comment']='Modified Columns: {}'.format([c for c in sx])
            sx.clear()
            if dfDiff.loc[row, "Comment"] == "" : 
                dfDiff.drop(row, inplace=True)
        else:
            dfDiff.loc[row,'Comment']='Added'
            newRows.append(row)
            
    for row in df_OLD.index:
        if row not in df_NEW.index:
            droppedRows.append(row)
            dfDiff = dfDiff.append(df_OLD.loc[row, :])
            dfDiff.loc[row,'Comment']='Removed'

    # nan_value = float("NaN")
    # dataframes=[dfDiff,df_OLD,df_NEW]
    # for v in dataframes:
    #     v.replace(0, nan_value, inplace=True)
    #     v.replace("", nan_value, inplace=True)
    #     v.dropna(how='all', axis=1, inplace=True)
    writer = pd.ExcelWriter(r"output-delta.xlsx", engine="xlsxwriter")
    df_OLD.to_excel(writer, sheet_name="Old Input", index=True)
    df_NEW.to_excel(writer, sheet_name="New Input", index=True)
    dfDiff.to_excel(writer, sheet_name="Delta", index=True)
    writer.save()

def main():
    path_OLD = Path(r"KPI_Delta_Document_20220106191702.xlsx")
    path_NEW = Path(r"KPI_Delta_Document_20220106191702.xlsx")
    excel_diff(path_OLD, path_NEW)
if __name__ == "__main__":
    main()























    # workbook = writer.book
    # worksheet = writer.sheets["Delta"]
    # worksheet.hide_gridlines(2)
    # worksheet.set_default_row(15)
    # grey_fmt = workbook.add_format({"bg_color": "#FF0000"})#,"font_color": "#E0E0E0"})
    # highlight_fmt = workbook.add_format(
    #     {"font_color": "#FF0000", "bg_color": "#B1B3B3"}
    # )
    # new_fmt = workbook.add_format({"bg_color": "#32CD32"})

    # worksheet.conditional_format(
    #     "A1:ZZ1000",
    #     {
    #         "type": "text",
    #         "criteria": "containing",
    #         "value": "→",
    #         "format": highlight_fmt,
    #     },
    # )
    # for rownum in range(dfDiff.shape[0]):
    #     row = dfDiff.index[rownum]
    #     for x in newRows:
    #         if x == row:
    #             worksheet.set_row(rownum + 1, 15, new_fmt)
    #     for y in droppedRows:
    #         if y == row:
    #             worksheet.set_row(rownum + 1, 15, grey_fmt)
            
    
