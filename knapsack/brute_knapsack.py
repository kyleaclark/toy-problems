import traceback

__author__ = 'kclark'


def generate_knapsack(items_dict, constraint_value):
    items_list = sorted(items_dict.items(), key=lambda x:x[1], reverse=True)
    items_partitions = _generate_partitions_helper(items_list)

    optimal_knapsack = None
    for items_set in items_partitions:
        current_knapsack = _compute_brute_knapsack(items_set, constraint_value)

        if current_knapsack is not None:
            if optimal_knapsack is None:
                optimal_knapsack = current_knapsack
            elif len(current_knapsack) < len(optimal_knapsack):
                optimal_knapsack = current_knapsack

    return optimal_knapsack


def _compute_brute_knapsack(items_list, constraint_value):
    current_collection = []

    for items_set in items_list:
        total_weight = 0
        current_set_list = []

        for cow in items_set:
            name, weight = cow
            verify_weight = total_weight + weight

            if verify_weight <= constraint_value:
                current_set_list.append(name)
                total_weight = verify_weight
            else:
                return None

        current_collection.append(current_set_list)

    return current_collection


def _generate_partitions_helper(set_):
    for partition in _compute_partitions_helper(set_):
        yield [list(elt) for elt in partition]


def _compute_partitions_helper(items_set):
    if not items_set:
        yield []
        return

    for index in range(2 ** len(items_set) // 2):
        parts = [set(), set()]

        for item in items_set:
            parts[index&1].add(item)
            index >>= 1

        for bit in _compute_partitions_helper(parts[1]):
            yield [parts[0]] + bit


def test_one():
    items_dict = {'Lemons': 40,
                  'Pennies': 20,
                  'Milky Ways': 40,
                  'Mounds': 50,
                  'Apples': 25,
                  'Crackers': 25}
    weight_constraint = 100

    knapsack = [sorted(group, key=str.lower) for group in generate_knapsack(items_dict, weight_constraint)]

    expected_knapsack = [['Milky Ways', 'Pennies', 'Lemons'], ['Apples', 'Mounds', 'Crackers']]
    expected_knapsack = [sorted(group, key=str.lower) for group in expected_knapsack]

    assert len(knapsack) == len(expected_knapsack) and sorted(knapsack) == sorted(expected_knapsack)


def test_two():
    items_dict = {'Snickers': 50,
                  'Barbies': 65,
                  'Butterfingers': 72}
    weight_constraint = 75

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [['Snickers'], ['Butterfingers'], ['Barbies']]
    expected_knapsack = [sorted(group, key=str.lower) for group in expected_knapsack]

    assert len(knapsack) == len(expected_knapsack) and sorted(knapsack) == sorted(expected_knapsack)


def test_three():
    items_dict = {'Starbursts': 54,
                  'Barbies': 39,
                  'Limes': 41,
                  'Butterfingers': 11}
    weight_constraint = 145

    knapsack = [sorted(group, key=str.lower) for group in generate_knapsack(items_dict, weight_constraint)]

    expected_knapsack = [['Limes', 'Starbursts', 'Barbies', 'Butterfingers']]
    expected_knapsack = [sorted(group, key=str.lower) for group in expected_knapsack]

    assert len(knapsack) == len(expected_knapsack) and sorted(knapsack) == sorted(expected_knapsack)


if __name__ == "__main__":
    try:
        print('begin tests')
        test_one()
        test_two()
        test_three()
        print('tests passed')
    except AssertionError:
        print('test assertions failed')
        print(traceback.format_exc())
    except Exception:
        print('unknown failure')
        print(traceback.format_exc())
