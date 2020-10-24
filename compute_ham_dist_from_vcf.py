from pysam import VariantFile
import sys
import numpy as np

# Load VCF
vcf_file = sys.argv[1]
vcf = VariantFile(vcf_file)
samples = list(vcf.header.samples)

# Prepare matrices
num_mismatches = np.zeros((len(samples), len(samples)))
num_snps = 0

# Parse VCF
for rec in vcf.fetch():
    print(rec.pos)
    num_snps += 1
    for i in range(len(samples)):
        for j in range(i, len(samples)):
            if (rec.samples[i]['GT'] != rec.samples[j]['GT']) & (rec.samples[i]['GT'] != rec.samples[j]['GT'][::-1]):
                num_mismatches[i,j] += 1
                num_mismatches[j,i] += 1

ham_dist = num_mismatches / num_snps
np.savetxt('ham_dist.txt', ham_dist, delimiter='\t', fmt='%1.3f')
