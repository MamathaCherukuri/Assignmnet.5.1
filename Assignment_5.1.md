

```python
import pandas as pd
import numpy as np
```

1) How-to-count-distance-to-the-previous-zero
For each value, count the difference of the distance from the previous zero (or the start
of the Series, whichever is closer) and if there are no previous zeros,print the position


```python
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
```


```python
x = (df['X'] != 0).cumsum()
y = x != x.shift()
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()
df['Y']
```




    0    1.0
    1    2.0
    2    0.0
    3    1.0
    4    2.0
    5    3.0
    6    4.0
    7    0.0
    8    1.0
    9    2.0
    Name: Y, dtype: float64



2.Create a DatetimeIndex that contains each business day of 2015 and use it to index a
Series of random numbers.


```python
dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
s = pd.Series(np.random.rand(len(dti)), index=dti)
```


```python
s
```




    2015-01-01    0.131101
    2015-01-02    0.620765
    2015-01-05    0.950731
    2015-01-06    0.261704
    2015-01-07    0.282488
    2015-01-08    0.715331
    2015-01-09    0.540319
    2015-01-12    0.297794
    2015-01-13    0.886370
    2015-01-14    0.743232
    2015-01-15    0.072907
    2015-01-16    0.783054
    2015-01-19    0.007802
    2015-01-20    0.830547
    2015-01-21    0.991665
    2015-01-22    0.184971
    2015-01-23    0.789749
    2015-01-26    0.395065
    2015-01-27    0.064785
    2015-01-28    0.200454
    2015-01-29    0.505516
    2015-01-30    0.522860
    2015-02-02    0.234978
    2015-02-03    0.990977
    2015-02-04    0.036192
    2015-02-05    0.913197
    2015-02-06    0.879530
    2015-02-09    0.471158
    2015-02-10    0.182135
    2015-02-11    0.155882
                    ...   
    2015-11-20    0.634275
    2015-11-23    0.183244
    2015-11-24    0.413014
    2015-11-25    0.214126
    2015-11-26    0.246955
    2015-11-27    0.339203
    2015-11-30    0.482576
    2015-12-01    0.923291
    2015-12-02    0.989186
    2015-12-03    0.203151
    2015-12-04    0.051277
    2015-12-07    0.055584
    2015-12-08    0.417672
    2015-12-09    0.737805
    2015-12-10    0.661371
    2015-12-11    0.589858
    2015-12-14    0.858934
    2015-12-15    0.346345
    2015-12-16    0.908140
    2015-12-17    0.772023
    2015-12-18    0.265794
    2015-12-21    0.694497
    2015-12-22    0.820928
    2015-12-23    0.502188
    2015-12-24    0.281891
    2015-12-25    0.674057
    2015-12-28    0.717776
    2015-12-29    0.948407
    2015-12-30    0.781594
    2015-12-31    0.716013
    Freq: B, Length: 261, dtype: float64



3.Find the sum of the values in s for every Wednesday.


```python
s[dti.weekday == 2].sum() 
```




    29.40532172359606



4) Average For each calendar month


```python
s.resample('M', how='mean')
```

    C:\Users\Nikhil\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: how in .resample() is deprecated
    the new syntax is .resample(...).mean()
      """Entry point for launching an IPython kernel.
    




    2015-01-31    0.489964
    2015-02-28    0.585300
    2015-03-31    0.444768
    2015-04-30    0.487230
    2015-05-31    0.459029
    2015-06-30    0.619254
    2015-07-31    0.484940
    2015-08-31    0.652940
    2015-09-30    0.503869
    2015-10-31    0.546497
    2015-11-30    0.465514
    2015-12-31    0.605121
    Freq: M, dtype: float64



5.For each group of four consecutive calendar months in s, find the date on which the
highest value occurred.


```python
s.groupby(pd.TimeGrouper('4M')).idxmax()
```

    C:\Users\Nikhil\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: pd.TimeGrouper is deprecated and will be removed; Please use pd.Grouper(freq=...)
      """Entry point for launching an IPython kernel.
    




    2015-01-31   2015-01-21
    2015-05-31   2015-02-20
    2015-09-30   2015-08-28
    2016-01-31   2015-10-28
    dtype: datetime64[ns]




```python

```


```python

```


```python

```
