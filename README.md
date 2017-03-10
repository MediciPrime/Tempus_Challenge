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

