# Download VCF
mkdir vcf
cd vcf
wget http://hgdownload.cse.ucsc.edu/gbdb/hg38/1000Genomes/ALL.chr1.shapeit2_integrated_snvindels_v2a_27022019.GRCh38.phased.vcf.gz
wget http://hgdownload.cse.ucsc.edu/gbdb/hg38/1000Genomes/ALL.chr1.shapeit2_integrated_snvindels_v2a_27022019.GRCh38.phased.vcf.gz.tbi
cd ..

# Download hg38
mkdir ref
cd ref
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa 
cd ..

# Download sequencing reads for HG01571
mkdir fastq
cd fastq
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR764/SRR764764/SRR764764_1.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR764/SRR764764/SRR764764_2.fastq.gz
cd ..

# Quality control
mkdir qc
fastqc -t 20 -o qc/ fastq/SRR764764_1.fastq.gz fastq/SRR764764_2.fastq.gz

# Index reference hg38
bwa index ref/GRCh38_full_analysis_set_plus_decoy_hla.fa 

# Mapping
mkdir map
bwa mem -t 20 -o map/HG01571.sam ref/GRCh38_full_analysis_set_plus_decoy_hla.fa fastq/SRR764764_1.fastq.gz fastq/SRR764764_2.fastq.gz

# Post-processing
samtools view -b -h -q 20 -@ 20 -o map/HG01571.bam map/HG01571.sam
samtools sort -@ 20 -o map/HG01571.sorted.bam map/HG01571.bam
samtools index map/HG01571.sorted.bam

# Variant calling
freebayes -f ref/GRCh38_full_analysis_set_plus_decoy_hla.fa map/HG01571.sorted.bam > vcf/HG01571.vcf





