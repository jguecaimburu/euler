"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
The first ten pentagonal numbers are:
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value
of D?
"""

import numpy as np


class MinPentagonalDif():
    # Limit set in pentagonal numbers order, not value.
    # Limit = 100 means first 100 pentagonals
    # Limit = 1000000 with batch size 2500 means 400 iterations!
    def __init__(self, limit, batch_size=2500, shared_batch=500):
        self.limit = limit
        self.batch_size = batch_size
        self.shared_batch = shared_batch
        self.batch_answers = []
        self.finish = False

    def get_smallest_pentagonal_difference_in_limit(self):
        self.set_first_n_pentagonal_numbers()
        self.start_processing_batchs()
        self.get_best_answer()

    def set_first_n_pentagonal_numbers(self):
        range = np.arange(1, self.limit + self.batch_size + 1)
        self.pentagonals = list(map(self.pentagonal_number, range))
        print("First pentagonal:", self.pentagonals[0])
        print("Last pentagonal:", self.pentagonals[self.limit-1])

    def pentagonal_number(self, index):
        return int(index * (3 * index - 1) / 2)

    def start_processing_batchs(self):
        self.set_first_batch_indexes()
        while not self.finish:
            print("Preparing batch...")
            batch = self.prepare_batch()
            self.process_batch(batch)
            self.update_batch_index()

    def set_first_batch_indexes(self):
        self.batch_start_index = 0
        self.set_end_batch_index()

    def set_end_batch_index(self):
        print("Starting index set to", self.batch_start_index)
        self.batch_end_index = self.batch_start_index + self.batch_size
        if self.batch_end_index > self.limit:
            self.batch_end_index = self.limit
        print("End index set to", self.batch_end_index)

    def prepare_batch(self):
        batch = self.pentagonals[self.batch_start_index: self.batch_end_index]
        print("First item in batch:", batch[0])
        print("Last item in batch:", batch[-1])
        return batch

    def process_batch(self, batch):
        array, trans_array = self.set_arrays_for_cross_operations(batch)
        sum_array = self.cross_sum(array, trans_array)
        subs_array = self.cross_subs(array, trans_array)
        batch_answer, mask = self.clean_arrays_and_extract_answer(sum_array,
                                                                  subs_array)
        self.check_and_save_batch_answer(batch_answer, batch, subs_array, mask)

    def set_arrays_for_cross_operations(self, batch):
        array = np.array(batch).reshape((len(batch), 1))
        trans_array = array.copy().T
        return array, trans_array

    def cross_sum(self, array, trans_array):
        return array + trans_array

    def cross_subs(self, array, trans_array):
        return array - trans_array

    def clean_arrays_and_extract_answer(self, sum_array, subs_array):
        clean_sum = self.replace_non_pentagonals(sum_array)
        clean_subs = self.replace_non_pentagonals(subs_array)
        mask = (clean_sum > 0) & (clean_subs > 0)
        masked_subs = clean_subs[mask]
        try:
            batch_answer = min(np.unique(masked_subs))
            print("Batch answer:", batch_answer)
        except ValueError:
            batch_answer = None
            print("No answer in this batch. Batch set to", batch_answer)
        return batch_answer, mask

    def replace_non_pentagonals(self, array):
        replace_value = -1
        return np.where(np.in1d(array, self.pentagonals)
                        .reshape(array.shape), array, replace_value)

    def check_and_save_batch_answer(self, batch_answer, batch,
                                    subs_array, mask):
        if batch_answer:
            not_mask = ~mask
            subs_array[not_mask] = -1
            print("Checking batch answer...")
            answer_indexes = np.where(subs_array == batch_answer)
            print("Found in", answer_indexes)
            index_zero = (answer_indexes[0][0], answer_indexes[1][0])
            first_pentagonal = batch[index_zero[0]]
            second_pentagonal = batch[index_zero[1]]
            sum_pentagonals = (first_pentagonal + second_pentagonal)
            subs_pentagonals = (first_pentagonal - second_pentagonal)

            print("Parents pentagonals:")
            print(first_pentagonal)
            print(second_pentagonal)
            print("Sum:", sum_pentagonals)
            print("Diff:", subs_pentagonals)
            assert sum_pentagonals in self.pentagonals
            try:
                assert subs_pentagonals in self.pentagonals
            except AssertionError:
                assert (-subs_pentagonals) in self.pentagonals
            self.batch_answers.append(batch_answer)

    def update_batch_index(self):
        if self.batch_end_index != self.limit:
            self.batch_start_index += self.shared_batch
            self.set_end_batch_index()
        else:
            self.finish = True

    def get_best_answer(self):
        try:
            min_answer = min(self.batch_answers)
            print("Min answer:", min_answer)
            return min_answer
        except ValueError:
            print("No answer found in limit.")
            return None


# limit = 1000
# Min answer: 5482660
# CPU times: user 57.3 s, sys: 6.86 s, total: 1min 4s
# Wall time: 47.4 s
