import traceback


def generate_knapsack(items_dict, constraint_value):
    items = sorted(items_dict.items(), key=lambda x:x[1], reverse=True)

    return _compute_greedy_knapsack(items, constraint_value, [])


def _compute_greedy_knapsack(items, constraint_value, knapsack_collection):
    bag_of_items = []
    knaspack_weight = 0

    idx = 0
    while idx < len(items):
        if knaspack_weight > constraint_value:
            break

        item = items[idx]
        name, weight = item
        verification_weight = knaspack_weight + weight

        if verification_weight <= constraint_value:
            bag_of_items.append(name)
            items.pop(idx)
            knaspack_weight = verification_weight
        else:
            idx += 1

    knapsack_collection.append(bag_of_items)

    if len(items) > 0:
        return _compute_greedy_knapsack(items, constraint_value, knapsack_collection)

    return knapsack_collection


def test_one():
    items_dict = {'Harry': 50,
                  'Mr. Belding': 15,
                  'Mickey': 75,
                  'Percy': 20,
                  'Peaches': 60,
                  'Larry': 45,
                  'Lenny': 10,
                  'Carrie': 5,
                  'Molly': 85,
                  'Maxx': 65}
    weight_constraint = 100

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [['Molly', 'Mr. Belding'],
                         ['Mickey', 'Percy', 'Carrie'],
                         ['Maxx', 'Lenny'], ['Peaches'],
                         ['Harry', 'Larry']]

    assert knapsack == expected_knapsack


def test_two():
    items_dict = {'Donuts': 50,
                  'Burgers': 65,
                  'Peaches': 12,
                  'Whip Cream': 35,
                  'Radishes': 50,
                  'Danishes': 85,
                  'Butter': 72,
                  'Limes': 24,
                  'Chocolates': 10,
                  'Apples': 38}
    weight_constraint = 100

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [['Danishes', 'Peaches'],
                         ['Butter', 'Limes'],
                         ['Burgers', 'Whip Cream'],
                         ['Donuts', 'Radishes'],
                         ['Apples', 'Chocolates']]

    assert knapsack == expected_knapsack


def test_three():
    items_dict = {'Burgers': 39,
                  'Whip Cream': 59,
                  'Radishes': 42,
                  'Licorices': 41,
                  'Chocolates': 59,
                  'Butter': 11,
                  'Star Crunch': 54,
                  'Apples': 28}
    weight_constraint = 120

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [['Whip Cream', 'Chocolates'],
                         ['Star Crunch', 'Radishes', 'Butter'],
                         ['Licorices', 'Burgers', 'Apples']]

    assert knapsack == expected_knapsack


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
