"""
    This is a function, that takes clients' id as an input and outputs the group number, that this client
belongs to.
"""


def group(customer_id: int):
    group_num = 0
    while customer_id != 0:
        group_num += customer_id % 10  # This operation returns the last number of id
        customer_id = customer_id // 10  # This operation reduces id by the last character
    return group_num


# Function to count number of groups for ids from 0 to n_customers
def func_test_1(n_customers: int):
    groups_dict = {}

    for customer_id in range(n_customers):
        client_group = group(customer_id)
        if client_group in groups_dict.keys():
            groups_dict[client_group] += 1  # If there is an occurrence of a particular group, we simply count it
        else:
            groups_dict[client_group] = 1  # Otherwise we add this new group and count it as first occurrence

    return groups_dict


print(func_test_1(1234567))


def func_test_2(n_first_id: int, n_customers: int):
    groups_dict = {}
    # Since second param we get as an input is n_customers, which stands for number of customers, we assume that it
    # represents number of customers following first id.
    for customer_id in range(n_first_id, n_first_id + n_customers):
        client_group = group(customer_id)
        if client_group in groups_dict.keys():
            groups_dict[client_group] += 1
        else:
            groups_dict[client_group] = 1

    return groups_dict
