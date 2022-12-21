import sys
import pandas as pd
from time import sleep

if __name__ == '__main__':
    csv_file = sys.argv[1]
    size = int(sys.argv[2])
    prefix = sys.argv[3]
    suffix = sys.argv[4] if len(sys.argv) > 4 else ''

    sleep(1)

    df = pd.read_csv(csv_file).rename({'permutation': 'Permutation'}, axis=1)

    for i in range(2, size + 1):
      pivot_df = pd.pivot_table(
        data=df[df['i'] == i],
        index=['Permutation'],
        columns=['j'], 
        values='comparisons',
        aggfunc='count',
        margins=True,
        margins_name='Occurrences'
      )
      pivot_df = pivot_df.fillna(0)
      pivot_df = pivot_df.astype(int)
      rename_dict = dict()
      for j in range(1, i + 1):
        pivot_df[j] = pivot_df[j].replace({0: ''})
        rename_dict[j] = f'j={j}'
      pivot_df = pivot_df.drop(['Occurrences'], axis=1)
      pivot_df = pivot_df.rename(rename_dict, axis=1)
      pivot_df.to_csv(f'{prefix}{i}{suffix}.csv', index=True, header=True)
