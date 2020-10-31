
## detectCFP (Pipeline for detecting carbon fixation pathways)

[![pypi licence](https://img.shields.io/pypi/l/detectCFP.svg)](https://opensource.org/licenses/gpl-3.0.html)
[![pypi version](https://img.shields.io/pypi/v/detectCFP.svg)](https://pypi.python.org/pypi/detectCFP) 


Dependencies
---

[gapseq](https://github.com/jotech/gapseq)


How to install:
---

+ To install

      pip3 install detectCFP

+ To upgrade
   
      pip3 install --upgrade detectCFP


How to run:
---

1. Cut-off table format (-c) [[example](example_data/cutoff_table.txt)]: file header has to be "MAG	PWY	Enzyme" (tab separated). 
Specify MAG completeness thresholds in the first column, followed by the cutoffs for key enzyme percentage 
and pathway completeness will be used when MAG completeness NO LESS THAN the specified threshold.

1. Genome completeness file format [[example](example_data/mag_cpl.txt)]: no header, no genome file extension, tab separated.
    
1. Example commands for running detectCFP

   + Detect CFP with default fixed cut-offs for key enzyme percentage (50%) and pathway completeness (80%)
    
         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 
         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 -faa faa_files

   + Detect CFP with customized fixed cut-offs for key enzyme percentage (70%) and pathway completeness (80%)
       
         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 -c 70,80

   + Detect CFP with genome specific cut-offs according to genome completeness

         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 -c cutoff_table.txt -q mag_cpl.txt

