import sys
import pandas as pd
from time import sleep

if __name__ == '__main__':
    csv_file = sys.argv[1]
    size = int(sys.argv[2])
    outfile = sys.argv[3]

    sleep(1)

    df = pd.read_csv(csv_file).rename({'permutation': 'Permutation'}, axis=1)

    pivot_df = pd.pivot_table(
      data=df,
      index=['Permutation'],
      columns=['i'], 
      values='comparisons',
      aggfunc='sum',
      margins=True,
      margins_name='Sum'
    )
    pivot_df = pivot_df.fillna(0)
    pivot_df = pivot_df.astype(int)
    rename_dict = dict()
    for i in range(2, size + 1):
      rename_dict[i] = f'i={i}'
    pivot_df = pivot_df.rename(rename_dict, axis=1)
    last_row = pivot_df.iloc[-1]
    pivot_df.to_csv(f'{outfile}.csv', index=True, header=True)
    with open(f'{outfile}.csv', 'a') as f:
      f.write('Average,')
      for i in range(2, size + 1):
        f.write('{:.4f},'.format(float(last_row[f'i={i}'])/(pivot_df.shape[0] - 1)))
      f.write('{:.4f}'.format(float(last_row['Sum'])/(pivot_df.shape[0] - 1)))
