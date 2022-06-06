```python
dtrange = sorted(log['dt'].unique())


data = pd.read_csv(data_path, sep='\t', header=None, names=['id', 'keyword'], quoting=3)
# “当文本文件中带有英文双引号时，直接用pd.read_csv进行读取会导致行数减少，此时应该对read_csv设置参数quoting=3或者quoting=csv.QUOTE_NONE”


lv3 = lv3[-lv3['keyword'].isna()].reset_index(drop=True)  # remove nan's

for c1, c2 in data.values 




```

pandas.read_csv()导入大文件时出现pandas.errors.ParserError: Error tokenizing data. C error: Buffer overflow c问题

使用python及其大文件，可以使用 engine='python’如下，解决这个问题。

```python
df = pd.read_csv( file_, index_col=None, header=0, engine='python' )
```