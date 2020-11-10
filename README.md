
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

1. Genome completeness file format [[example](example_data/mag_cpl.txt)]: **NO** header, **NO** genome file extension, **TAB** separated.
    
1. Example commands for running detectCFP

    **kecc**: key enzyme completeness cut-off
    
    **pcc**: pathway completeness cut-off

   + with fixed kecc and fixed pcc, as specified in path2hmm.txt
         
         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force 

   + with dynamic kecc and fixed pcc, requires genome completeness info

         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force -dynamic_kecc -q MAG_cpl.txt 

   + with fixed kecc and dynamic pcc, requires genome completeness info

         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force -dynamic_pcc -q MAG_cpl.txt 

   + with dynamic kecc and dynamic pcc, requires genome completeness info

         detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force -dynamic_kecc -dynamic_pcc -q MAG_cpl.txt
