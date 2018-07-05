# Type your code here
def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    result_dict = {}
    mid_dict = {}
    pass_list = []
    for val in scores_list:
        if val >=60:
            pass_list.append('pass')
        else:
            pass_list.append('fail')
    for val in range(len(ages_list)):
        mid_dict = {names_list[val]: [ages_list[val],scores_list[val],pass_list[val]]}
        result_dict.update(mid_dict)
    return result_dict





lista =(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60])
print(construct_dictionary_from_lists(lista[0], lista[1], lista[2]))