
## detectCFP (Detect carbon fixation pathways)

[![pypi licence](https://img.shields.io/pypi/l/detectCFP.svg)](https://opensource.org/licenses/gpl-3.0.html)
[![pypi version](https://img.shields.io/pypi/v/detectCFP.svg)](https://pypi.python.org/pypi/detectCFP) 


Dependencies
---

[gapseq](https://github.com/jotech/gapseq)


How to install:
---

detectCFP can be installed via `pip3`:

    # First-time installation
    pip3 install detectCFP
        
    # upgrade
    pip3 install --upgrade detectCFP


How to run:
---

    detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 
    detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 -faa faa_files
    detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 -c 70,80
    detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 6 -c cutoff_table.txt -q mag_completeness.txt
