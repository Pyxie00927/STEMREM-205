import numpy as np

# Core scverse libraries
import scanpy as sc
import anndata as ad
import scipy.io
import gzip
# Data retrieval
import pooch
import pandas as pd
import os

sc.settings.set_figure_params(dpi=50, facecolor="white")

matrix_file_name = "GSM7230113_Crosslinked_Collagen_D3_matrix.mtx.gz"
barcodes_file_name = "GSM7230113_Crosslinked_Collagen_D3_barcodes.tsv.gz"
features_file_name = "GSM7230113_Crosslinked_Collagen_D3_features.tsv.gz"

with gzip.open(matrix_file_name, "rb") as f:
    sparse_matrix = scipy.io.mmread(f)
    
dense_matrix = sparse_matrix.toarray()
print(dense_matrix.shape)
print(dense_matrix[3,5])

print("Hi my name is Peter")

# Load barcodes (cell identifiers)
barcodes = pd.read_csv(barcodes_file_name, sep="\t", header=None)
barcodes.columns = ["Barcode"]  # Name the column for clarity

# Load features (genes)
# features = pd.read_csv("GSM7230111_D0_Control_features.tsv.gz", sep="\t")
#features.columns = ["Gene_ID", "Gene_Name", "Feature_Type"]  # Standard 10x format

# Display the first few rows
print(barcodes.head())
# print(features.head())

# df = pd.read_csv('GSM7230111_D0_Control_features.tsv.gz', sep='\t')
# Open the compressed file
# with gzip.open('GSM7230111_D0_Control_features.tsv.gz', 'rt') as f:
    # Read the file into a Pandas DataFrame
#    df = pd.read_csv(f, sep='\t')

new_file_path = features_file_name
features = pd.read_csv(features_file_name, sep='\t', header=None)
# features.columns = ["Gene_ID", "Gene_Name", "Feature_Type"]
print(features.head())

