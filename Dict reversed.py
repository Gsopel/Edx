def _reverse_dictionary(input_dict):
    output_dict={}
    for k in input_dict:
        for value in input_dict[k]:
            key_lowered=k.lower()
            value_lowered=value.lower()
            if output_dict.get(value_lowered):
                if k not in output_dict[value_lowered]:
                    output_dict[value_lowered].append(key_lowered)
                    output_dict[value_lowered].sort()
            else:
                output_dict[value_lowered]=[key_lowered]
    return output_dict




dictionary = {'Accurate': ['exact', 'precise'], 'exact': ['precise'], 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}
print(_reverse_dictionary(dictionary))