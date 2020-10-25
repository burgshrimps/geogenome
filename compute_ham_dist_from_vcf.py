from pysam import VariantFile
import sys
import numpy as np
import pandas as pd

# Input
vcf_file = sys.argv[1]
sample_sheet = sys.argv[2]

# Load VCF
vcf = VariantFile(vcf_file)

# Stratified sampling
n = 20 # Number of samples from each group
samples = pd.read_csv(sample_sheet, sep='\t')
samples = samples[samples['Sample name'].isin(list(vcf.header.samples))]
samples_subset = samples.groupby('Superpopulation code').apply(lambda x: x.sample(n=n))
num_samples = len(samples_subset)
samples_subset.to_csv('samples_subset.tsv', sep='\t', index=False)
vcf.subset_samples(list(samples_subset['Sample name']))

# Prepare matrices
num_mismatches = np.zeros((num_samples, num_samples))
num_snps = 0

# Parse VCF
for rec in vcf.fetch():
    print(rec.pos)
    all_homref = True
    tmp_mismatches = np.zeros((num_samples, num_samples))
    for i in range(num_samples):
        if rec.samples[i]['GT'] != (0,0):
            all_homref = False
        for j in range(i, num_samples):
            if (rec.samples[i]['GT'] != rec.samples[j]['GT']) & (rec.samples[i]['GT'] != rec.samples[j]['GT'][::-1]):
                tmp_mismatches[i,j] += 1
    if not all_homref:
        num_mismatches += tmp_mismatches
        num_snps += 1

ham_dist = num_mismatches / num_snps
ham_dist = np.triu(ham_dist) + np.tril(ham_dist.T) # Make matrix balanced
np.savetxt('ham_dist.txt', ham_dist, delimiter='\t', fmt='%1.3f')