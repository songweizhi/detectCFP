
def sort_pwy_by_completeness(op_table_1, op_table_3):

    op_table_3_handle = open(op_table_3, 'w')
    pwy_list = []
    pwy_cpl_pos_dict = {}
    pwy_found_pos_dict = {}
    line_index = 0
    for each_detection in open(op_table_1):
        each_detection_split = each_detection.strip().split('\t')

        # read in header
        if line_index == 0:
            n = 1
            while n < len(each_detection_split):
                pwy_id = each_detection_split[n].split('__')[0]
                pwy_list.append(pwy_id)
                pwy_cpl_pos_dict[pwy_id] = n + 1
                pwy_found_pos_dict[pwy_id] = n + 2
                n += 3

        # parse detection
        else:
            # read in line
            current_gnm_pwy_cpl_set = set()
            current_gnm_cpl_to_pwy_dict = {}
            for each_pwy in pwy_list:
                current_pwy_found = each_detection_split[pwy_found_pos_dict[each_pwy]]
                if current_pwy_found == '1':
                    current_pwy_cpl = float(each_detection_split[pwy_cpl_pos_dict[each_pwy]])
                    current_gnm_pwy_cpl_set.add(current_pwy_cpl)
                    if current_pwy_cpl not in current_gnm_cpl_to_pwy_dict:
                        current_gnm_cpl_to_pwy_dict[current_pwy_cpl] = [each_pwy]
                    else:
                        current_gnm_cpl_to_pwy_dict[current_pwy_cpl].append(each_pwy)

            # sort completeness list
            current_gnm_pwy_cpl_list_sorted = sorted([cpl for cpl in current_gnm_pwy_cpl_set])[::-1]

            # write out
            if len(current_gnm_pwy_cpl_list_sorted) > 0:
                list_to_write = [each_detection_split[0]]
                for each_cpl in current_gnm_pwy_cpl_list_sorted:
                    for each_found_pwy in current_gnm_cpl_to_pwy_dict[each_cpl]:
                        list_to_write.append(each_found_pwy)
                        list_to_write.append(str(each_cpl))
                str_to_write = '\t'.join(list_to_write) + '\n'
                op_table_3_handle.write(str_to_write)

        line_index += 1
    op_table_3_handle.close()

# file in/out
op_table_1 = '/Users/songweizhi/Desktop/Sponges_detected_CFPs.1.txt'
op_table_3 = '/Users/songweizhi/Desktop/Sponges_detected_CFPs.3.txt'

sort_pwy_by_completeness(op_table_1, op_table_3)

