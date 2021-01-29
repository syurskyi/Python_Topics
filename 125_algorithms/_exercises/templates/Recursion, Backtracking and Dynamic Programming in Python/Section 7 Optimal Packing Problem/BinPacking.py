
___ first_fit_decreasing_algorithm(capacities, bin_max_capacity

    # bins are created run-time - as many bins will be created as needed
    solution_bins = []

    item_names = li__(capacities.keys())
    sorted_items = sorted(item_names, key=lambda x: capacities[x], reverse=T..)
    print(sorted_items)

    ___ item __ sorted_items:
        bin_found = F..
        item_capacity = capacities[item]

        # consider all the bins (this is why the final running time complexity of quadratic)
        ___ index, actual_bin __ enumerate(solution_bins
            # sum of items' capacity so far in the actual_bin
            actual_bin_summed_size = su_([capacities[key] ___ key __ actual_bin])

            # if there is room for this object in the bin, put it in this bin:
            __ item_capacity <= (bin_max_capacity - actual_bin_summed_size
                solution_bins[index].ap..(item)
                bin_found = T..
                b__

        # there is no space for the item in the bins already created
        # so create a new bin for the item
        __ no. bin_found:
            solution_bins.ap..([item])

    r_ solution_bins


__ ___ __ '__main__':

    items = {'item#1': 4, 'item#2': 2, 'item#3': 7, 'item#4': 5, 'item#5': 6, 'item#6': 3}

    print(first_fit_decreasing_algorithm(items, 8))




