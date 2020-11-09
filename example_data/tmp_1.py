import os


def get_pwy_ec_cutoff_by_mag_cpl(mag_cpl, mag_cpl_to_cutoff_dict, mag_cpl_threshold_list):

    mag_cpl_threshold_list_high_to_low = sorted(mag_cpl_threshold_list)[::-1]

    cutoffs_determined = False
    pathway_cutoff = 0
    key_enzyme_cutoff = 0
    for cpl_threshold in mag_cpl_threshold_list_high_to_low:

        if cutoffs_determined is False:
            if mag_cpl >= cpl_threshold:
                key_enzyme_cutoff = mag_cpl_to_cutoff_dict[cpl_threshold][0]
                pathway_cutoff = mag_cpl_to_cutoff_dict[cpl_threshold][1]
                cutoffs_determined = True

    return key_enzyme_cutoff, pathway_cutoff


# pwy_cpl_cutoff              = args['pcc']
# key_enzyme_cpl_cutoff       = args['kecc']
key_enzyme_and_pwy_cutoff   = ''
mag_cpl_file                = ''


##################################### check key enzyme and pwy cutoff settings #####################################

dynamic_cutoff = False
if (os.path.isfile(key_enzyme_and_pwy_cutoff) is True) and (os.path.isfile(mag_cpl_file) is True):
    dynamic_cutoff = True

elif (os.path.isfile(key_enzyme_and_pwy_cutoff) is True) and (mag_cpl_file is None):
    print('MAG completeness file not provided, program exited!')
    exit()

elif (',' in key_enzyme_and_pwy_cutoff) and (mag_cpl_file is not None):
    print('Cut-offs for key enzyme percentage and pathway completeness were fixed, MAG qualities will be ignored')

key_enzyme_percentage_cutoff = 0
pwy_completeness_cutoff = 0
mag_to_key_enzyme_cutoff_dict = {}
mag_to_pathway_cutoff_dict = {}
mag_completeness_dict = {}
min_mag_cpl_threshold = 0
if dynamic_cutoff is False:
    key_enzyme_percentage_cutoff = float(key_enzyme_and_pwy_cutoff.split(',')[0])
    pwy_completeness_cutoff = float(key_enzyme_and_pwy_cutoff.split(',')[1])
else:
    # read in cutoff table
    mag_cpl_to_cutoff_dict = {}
    mag_cpl_threshold_list = []
    for line in open(key_enzyme_and_pwy_cutoff):
        if not line.startswith('MAG	PWY	Enzyme'):
            line_split = line.strip().split()
            mag_c = int(line_split[0])
            mag_e = int(line_split[1])
            mag_p = int(line_split[2])
            mag_cpl_to_cutoff_dict[mag_c] = [mag_e, mag_p]
            mag_cpl_threshold_list.append(mag_c)

    min_mag_cpl_threshold = min(mag_cpl_threshold_list)

    # get mag_to_pathway_cutoff_dict and mag_to_key_enzyme_cutoff_dict
    for mag in open(mag_cpl_file):
        mag_split = mag.strip().split('\t')
        mag_id = mag_split[0]
        mag_cpl = float(mag_split[1])
        mag_completeness_dict[mag_id] = mag_cpl
        current_mag_pathway_cutoff, current_mag_key_enzyme_cutoff = get_pwy_ec_cutoff_by_mag_cpl(mag_cpl,
                                                                                                 mag_cpl_to_cutoff_dict,
                                                                                                 mag_cpl_threshold_list)
        mag_to_pathway_cutoff_dict[mag_id] = current_mag_pathway_cutoff
        mag_to_key_enzyme_cutoff_dict[mag_id] = current_mag_key_enzyme_cutoff

print(mag_to_key_enzyme_cutoff_dict)
print(mag_to_pathway_cutoff_dict)
