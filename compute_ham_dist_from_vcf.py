from pysam import VariantFile
import sys

vcf_file = sys.argv[1]
vcf = VariantFile(vcf_file)

print(list(vcf.header.samples))