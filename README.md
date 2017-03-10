# VCF Parser

This script parses a VCF file and outputs a table in tab-separated values (TSV) form.  
The table contains the following columns:  

|Key | Description|
|----|------------|
|Chr | Chromosome variant is locationed on|
|Position | Variants' location on the chromosome|
|Ref | Reference Allele|
|Alt | Alternate Allele|
|Annotation | Type of variant e.g. snp, insertion, del|
|SeqDepth | Total read depth at variant location|
|VSReads | Total number of reads representing the variant i.e. Variant Supporting Reads|
|PVSReads | Percent of reads representing the variant|
|AFrequency | Allele Frequency according to ExAC Browser - Harvard|
|AGene | Affected gene according to ExAC Browser - Harvard|

## Setup

1. There are two ways to ensure the script will function properly:
   - Install [Miniconda](http://conda.pydata.org/miniconda.html)
       - Use setup *Tempus* environment w/ the following code:
       - `conda env create -f environment.yml`
   - Install python3 and install the [requests](http://docs.python-requests.org/en/master/user/install/) package
       - `pip install requests`
   
2. After performing either of the two steps above *cd* into the folder containing the script 
   - Ensure that *vcf_parser.py* is executable
   - Run `python vcf_parser.py <insert vcf file location>`
   
3. The script will output a table (*table.txt*) in TSV form
