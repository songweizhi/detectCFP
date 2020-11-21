
## detectCFP (Pipeline for detecting carbon fixation pathways)
[![pypi licence](https://img.shields.io/pypi/l/detectCFP.svg)](https://opensource.org/licenses/gpl-3.0.html)
[![pypi version](https://img.shields.io/pypi/v/detectCFP.svg)](https://pypi.python.org/pypi/detectCFP) 


Dependencies
---

[Prodigal](https://github.com/hyattpd/Prodigal)

[HMMER](http://hmmer.org) 

[GapSeq](https://github.com/jotech/gapseq)


How to install:
---

    # to install 
    pip3 install detectCFP
    
    # to upgrade 
    pip3 install --upgrade detectCFP

Input file format:
---

1. path2hmm file: **TAB** separated columns.
   + File header has to be "Pwy	KeyEnzyme	PwyCpl	KeyEnzymeCpl".
   + **Col 1**: pathway id, no "|" at the two ends
   + **Col 2**: hmm id of key enzymes, if there are multiple key enzymes, separate by comma.
   + **Col 3**: minimum pathway completeness for the pathway to be considered as existing in **COMPLETE** genome.
   + **Col 4**: minimum key enzyme completeness for the pathway to be considered as existing in **COMPLETE** genome.

         Pwy	KeyEnzyme	PwyCpl	KeyEnzymeCpl
         rTCA1	citas,citbs	85	100
         rTCA2	CCSs,CCSL,CCL	90	100
         4HB3HP	HBD_alignments	80	100
         3HP	TIGR04253	90	100	
         DC4HB	HBD_alignments	90	100	
         CALVIN-PWY	PRK	69	100	
         CALVIN-PWY	PRK2	85	100	
         CODHb-PWY	MeTr_alignments	90	100	
         CODHa-PWY	MeTr_alignments	90	100	

1. Genome completeness file: **NO** header, **NO** genome file extension, **TAB** separated.
            
       mag_1	97.57
       mag_2	74.21
       mag_3	100
       
1. Genome taxonomy file: choose from **Bacteria**/**Archaea**, **NO** header, **NO** genome file extension, **TAB** separated.

       mag_1	Archaea
       mag_2	Archaea
       mag_3	Bacteria

How to run:
---

+ **KECC**: key enzyme completeness cut-off

+ **PCC**: pathway completeness cut-off

1. With fixed KECC and fixed PCC, as specified in path2hmm.txt
     
       detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force -taxon MAG_taxon.txt 

1. With dynamic KECC and fixed PCC, requires genome completeness info

       detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force -taxon MAG_taxon.txt -dynamic_kecc -cpl MAG_cpl.txt 

1. With dynamic KECC and dynamic PCC, requires genome completeness info

       detectCFP -p DeepSea -g MAG_files -x fna -hmm keyEnzymes.hmm -k path2hmm.txt -t 12 -force -taxon MAG_taxon.txt -dynamic_kecc -dynamic_pcc -cpl MAG_cpl.txt

Output files:
---

1. Output 1:
    + Each pathway in this file has three columns: PWY_HMM, PWY_completeness and PWY_found
    + **PWY_HMM**: "_n_" refers to "and " and "_v_" refers to "or "
    + **PWY_cpl**: Gapseq provided pathway completeness
    + **PWY_found**: "1" for detected and "0" for not

1. Output 2: presence/absence of interested pathways among MAGs

