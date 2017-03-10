import re
import requests
import argparse

# function containing all the VCF parsing steps
def vcf_parser(file_location):

    # open and parse vcf file
    with open(file_location, 'r') as f:

        # open to write to 'table.txt'
        with open('table.txt', 'w') as w:

            # write header for 'table.txt'
            w.write('Chr\tPosition\tRef\tAlt\tAnnotation\tSeqDepth\tVSReads\tPVSReads\tAFrequency\tAGene\n')

            # parse through vcf file
            for line in f:
            
                # find line containing chrom # '[1-9]'
                # set line with useful info as 'uInfo'
                if re.search('^[1-9]', line):
           
                    # split line along tabs
                    uInfo = line.rsplit('\t')
                
                    # collect chrom, position, ref, alt
                    chrom = uInfo[0]
                    pos = uInfo[1]
                    ref = uInfo[3].rsplit(',')[0]
                    alt = uInfo[4].rsplit(',')[0]
                    
                    # obtain appropriate information w/ try except blocks
                    # set AB to the allele balance 
                    try:
                        AB = float(re.search('AB=0(\.\d+)?|1\.0', uInfo[7]).group(0).rsplit('=')[1])
                    except Exception:
                        AB = 'NA'
                        
                    try:
                        DP = int(re.search('DP=[1-9]+', uInfo[7]).group(0).rsplit('=')[1])
                    except Exception:
                        DP = 'NA'
                    
                    try:
                        TYPE = re.search('TYPE=[a-z]+', uInfo[7]).group(0).rsplit('=')[1].rsplit(',')[0]
                    except Exception:
                        TYPE = 'NA'

                    # calculate number of variant supporting reads
                    try:
                        #VSR = re.search('AO=[1-9]+', uInfo[7]).group(0).rsplit('=')[1]
                        VSR = int(DP - (AB * DP))
                    except Exception:
                        VSR = 'NA'

                    # calculate percent of variant supporting reads
                    try:
                        PVSR = 1 - AB
                    except Exception:
                        PVSR = 'NA'
                    
                    # create REST exac.hms.harvard web query
                    webquery = 'http://exac.hms.harvard.edu/rest/variant/{0}-{1}-{2}-{3}'.format(
                        chrom, pos, ref, alt)
                    
                    # obtain SNP information at location in json format
                    resp = requests.get(webquery)
                    resp = resp.json()
                    
                    # set try except to obtain 'allele_freq'
                    # set to 'NA' if not available
                    try:
                        allele_freq = resp['variant']['allele_freq']
                    except Exception:
                        allele_freq = 'NA'

                    # check for affected gene
                    # set to 'NA' if not available
                    try:
                        affected_gene = resp['variant']['genes'][0]
                    except Exception:
                        affected_gene = 'NA'

                    # insert parsed information into 'table.txt'
                    w.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\n'.format(
                        chrom, pos, ref, alt, TYPE, DP, VSR, PVSR, allele_freq, affected_gene))


# Allow users to specify the location of VCF file
parser = argparse.ArgumentParser()
parser.add_argument('fl', help='VCF file location')
args = parser.parse_args()
vcf_parser(args.fl)
