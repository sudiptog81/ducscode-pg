from os import path, makedirs
from shutil import copy

from tqdm import tqdm
import pandas as pd

DEST_FOLDER = 'filtered_data'
DATASET_FOLDER = path.join(path.dirname(path.abspath(__file__)), 'covid-chestxray-dataset')

metadata_df = pd.read_csv('covid-chestxray-dataset/metadata.csv')

print('Creating folders and copying files according to views...')
for index, row in tqdm(metadata_df.iterrows(), total=metadata_df.shape[0]):
  if row['view'] in ['PA', 'AP']:
    view_dest_folder = path.join(DEST_FOLDER, row['view'])
    if not path.exists(view_dest_folder):
      makedirs(view_dest_folder)
    copy(path.join(DATASET_FOLDER, row['folder'], row['filename']), view_dest_folder)

