import os


# cutoff files for pwy and key_enzyme are required
pwy_to_key_enzyme_file      = '/Users/songweizhi/Desktop/cutoff_setting/pathwaysXhmmfiles.txt'
key_enzyme_cpl_cutoff       = '/Users/songweizhi/Desktop/cutoff_setting/ke_cutoff.txt'  # kecc
pwy_cpl_cutoff              = '/Users/songweizhi/Desktop/cutoff_setting/pwy_cutoff.txt'  # pcc
mag_cpl_file                = '/Users/songweizhi/Desktop/cutoff_setting/mag_cpl.txt'
dynamic_pcc = True
dynamic_kecc = True
str_connector = '__|__'


########################################## read in pathway to key enzyme file ##########################################

# read in pathway to key enzyme file
pwy_to_key_enzyme_dict = {}
default_PwyCpl_cutoff_dict = {}
default_KeyEnzymeCpl_cutoff_dict = {}
for each_pathway in open(pwy_to_key_enzyme_file):
    if not each_pathway.startswith('Pwy	KeyEnzyme'):
        each_pathway_split = each_pathway.strip().split('\t')
        pwy_id = each_pathway_split[0]
        key_enzyme_str = each_pathway_split[1]
        key_enzyme_list = key_enzyme_str.split(',')
        PwyCpl = float(each_pathway_split[2])
        KeyEnzymeCpl = float(each_pathway_split[3])

        if pwy_id not in pwy_to_key_enzyme_dict:
            pwy_to_key_enzyme_dict[pwy_id] = [key_enzyme_list]
        else:
            pwy_to_key_enzyme_dict[pwy_id].append(key_enzyme_list)

        key_str = '%s%s%s' % (pwy_id, str_connector, key_enzyme_str)
        default_PwyCpl_cutoff_dict[key_str] = PwyCpl
        default_KeyEnzymeCpl_cutoff_dict[key_str] = KeyEnzymeCpl




genome_list = []
for each_genome in open(mag_cpl_file):
    each_genome_split = each_genome.strip().split('\t')
    genome_list.append(each_genome_split[0])

# read genome completeness into dict
genome_cpl_dict = {}
for each_genome in open(mag_cpl_file):
    each_genome_split = each_genome.strip().split('\t')
    genome_id  =  each_genome_split[0]
    genome_cpl =  float(each_genome_split[1])
    genome_cpl_dict[genome_id] = genome_cpl

# get genome specific key enzyme completeness cutoff
if dynamic_kecc is True:
    dynamic_KeyEnzymeCpl_cutoff_dict = {}
    for genome in genome_list:
        current_genome_KeyEnzymeCpl_cutoff_dict = {}
        for key_str in default_KeyEnzymeCpl_cutoff_dict:
            adjusted_cutoff = (default_KeyEnzymeCpl_cutoff_dict[key_str]) * (genome_cpl_dict[genome]) / 100
            current_genome_KeyEnzymeCpl_cutoff_dict[key_str] = adjusted_cutoff
        dynamic_KeyEnzymeCpl_cutoff_dict[genome] = current_genome_KeyEnzymeCpl_cutoff_dict

# get genome specific pathway completeness cutoff
if dynamic_pcc is True:
    dynamic_PwyCpl_cutoff_dict = {}
    for genome in genome_list:
        current_genome_PwyCpl_cutoff_dict = {}
        for key_str in default_PwyCpl_cutoff_dict:
            adjusted_PwyCpl_cutoff = (default_PwyCpl_cutoff_dict[key_str]) * (genome_cpl_dict[genome]) / 100
            current_genome_PwyCpl_cutoff_dict[key_str] = adjusted_PwyCpl_cutoff
        dynamic_PwyCpl_cutoff_dict[genome] = current_genome_PwyCpl_cutoff_dict









