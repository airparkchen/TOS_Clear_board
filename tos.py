

def decompose_stone_counts(stone_counts):
    """
    Decompose the stone counts into groups of 3, 4, or 5.

    :param stone_counts: Dictionary with stone types as keys and their counts as values.
    :return: A dictionary with stone types as keys and a list of groups as values.
    """
    decomposed_counts = {}
    for stone, count in stone_counts.items():
        groups = []
        while count > 0:
            if count % 5 == 0:
                groups.append(5)
                count -= 5
            elif count % 4 == 0 or (count - 4) % 3 == 0:
                groups.append(4)
                count -= 4
            elif count >= 3:
                groups.append(3)
                count -= 3
        decomposed_counts[stone] = groups
    return decomposed_counts

def count_decomposed_groups(decomposed_counts):

    group_counts = {3: 0, 4: 0, 5: 0}
    for groups in decomposed_counts.values():
        for group in groups:
            group_counts[group] += 1
    return group_counts

def match_pattern_by_group_counts(group_counts):

    patterns = {
        1: {3: 10, 4: 0, 5: 0}, # Pattern 1: 33333 33333
        2: {3: 0, 4: 0, 5: 6},  # Pattern 2: 555555
        3: {3: 5, 4: 0, 5: 3},  # Pattern 3: 555 33333
        4: {3: 1, 4: 3, 5: 3},  # Pattern 4: 555 4443
        5: {3: 0, 4: 5, 5: 2},  # Pattern 5: 55 44444
        6: {3: 2, 4: 6, 5: 0},  # Pattern 6: 4443 4443
        7: {3: 6, 4: 3, 5: 0},  # Pattern 7: 4443 33333
        8: {3: 4, 4: 2, 5: 2},  # Pattern 8: 5544 3333
        9: {3: 3, 4: 4, 5: 1},  # Pattern 9: 5444 4333
        10: {3: 3, 4: 4, 5: 1}, # Pattern 10: 54444 333
        11: {3: 7, 4: 1, 5: 1}, # Pattern 11: 5433 33333
        12: {3: 2, 4: 1, 5: 4}  # Pattern 12: 5555 433
    }

    # Compare group_counts with each pattern
    for pattern_num, pattern in patterns.items():
        if group_counts == pattern:
            return pattern_num

    return None
def record_group_types(decomposed_counts):
    """
    記錄每個分組大小（3、4、5）

    :param decomposed_counts: 字典，key為符石類型，value為分組列表。
    :return: 字典，鍵為分組大小（3、4、5），值為符石類型列表。
    """
    group_types = {3: [], 4: [], 5: []}
    for stone, groups in decomposed_counts.items():
        for group in groups:
            group_types[group].append(stone)
    return group_types

# def group_layout():
#     layout = {
#         1: {3: 10, 4: 0, 5: 0}, # Pattern 1: 33333 33333
#         2: {3: 0, 4: 0, 5: 6},  # Pattern 2: 555555
#         3: {3: 5, 4: 0, 5: 3},  # Pattern 3: 555 33333
#         4: {3: 1, 4: 3, 5: 3},  # Pattern 4: 555 4443
#         5: {3: 0, 4: 5, 5: 2},  # Pattern 5: 55 44444
#         6: {3: 2, 4: 6, 5: 0},  # Pattern 6: 4443 4443
#         7: {3: 6, 4: 3, 5: 0},  # Pattern 7: 4443 33333
#         8: {3: 4, 4: 2, 5: 2},  # Pattern 8: 5544 3333
#         9: {3: 3, 4: 4, 5: 1},  # Pattern 9: 5444 4333
#         10: {3: 3, 4: 4, 5: 1}, # Pattern 10: 54444 333
#         11: {3: 7, 4: 1, 5: 1}, # Pattern 11: 5433 33333
#         12: {3: 2, 4: 1, 5: 4}  # Pattern 12: 5555 433

#     }
# {[5[0],5[0],5[0],5[0],5[0],4[0]],
#  [4[1],4[2],4[3],3[0],3[1],4[0]],
#  [4[1],4[2],4[3],3[0],3[1],4[0]],
#  [4[1],4[2],4[3],3[0],3[1],4[0]],
#  [4[1],4[2],4[3],3[2],3[2],3[2]]}

def generate_text_pattern(matching_pattern, group_types):
    if matching_pattern == 9:
        # 建立模式 9 的排列
        pattern = [
            [group_types[5][0]] * 5 + [group_types[4][0]],
            [group_types[4][1], group_types[4][2], group_types[4][3], group_types[3][0], group_types[3][1], group_types[4][0]],
            [group_types[4][1], group_types[4][2], group_types[4][3], group_types[3][0], group_types[3][1], group_types[4][0]],
            [group_types[4][1], group_types[4][2], group_types[4][3], group_types[3][0], group_types[3][1], group_types[4][0]],
            [group_types[4][1], group_types[4][2], group_types[4][3], group_types[3][2], group_types[3][2], group_types[3][2]]
        ]
        return pattern
    else:
        return []

# Example Usage
stone_counts_example = {'水': 3, '火': 5, '木': 6, '光': 4, '暗': 4, '心': 8} #input
decomposed_counts = decompose_stone_counts(stone_counts_example)
group_counts = count_decomposed_groups(decomposed_counts)
group_types = record_group_types(decomposed_counts)
matching_pattern = match_pattern_by_group_counts(group_counts)
pattern_output = generate_text_pattern(matching_pattern, group_types)

print("屬性組:", decomposed_counts)
print("數量組:", group_counts)
print("模式:", matching_pattern)
print("數量對應屬性:", group_types)
print(f"輸入的符石:{stone_counts_example}")
for row in pattern_output:
    print(' '.join(row))