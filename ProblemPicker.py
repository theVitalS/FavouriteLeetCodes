import random

# List of problems by category (I prioritize medium difficulty, so only these problems currently present)
sliding_window_problems = {3, 159, 187, 209, 340, 395, 413, 424, 438, 487, 567, 658, 713, 718, 837, 21, 904, 930, 978,
                           1004, 1031, 1052, 1100, 1151, 1156, 1208, 1234, 1248, 1297, 1343, 1358, 1423, 1438, 1456,
                           1477, 1493, 1658, 1695, 1838, 1839, 1852, 1871, 1888, 1918, 2024, 2090, 2107, 2134, 2260,
                           2401, 2411, 2461, 2516, 2537, 2555, 2653, 2730, 2743, 2747, 2762, 2779, 2799, 2831, 2841,
                           2875, 2904, 2958, 2962, 2981, 2982, 3023, 3097, 3135, 3191, 3208, 3234, 3254, 3255, 3297,
                           3305, 3306, 3323, 3325, 3346}

two_pointers_problems = {5, 11, 15, 16, 18, 19, 31, 61, 75, 80, 82, 86, 142, 143, 148, 151, 161, 165, 167, 186, 189,
                         244, 251, 253, 259, 277, 287, 360, 443, 457, 475, 481, 522, 524, 532, 556, 567, 581, 611, 633,
                         647, 658, 723, 763, 777, 786, 795, 809, 825, 826, 838, 845, 870, 881, 923, 948, 969, 986, 1023,
                         1040, 1048, 1055, 1214, 1229, 1237, 1265, 1471, 1498, 1508, 1570, 1574, 1577, 1616, 1634, 1650,
                         1679, 1712, 1721, 1750, 1754, 1764, 1813, 1850, 1855, 1861, 1868, 1877, 1885, 1898, 1963, 2046,
                         2095, 2105, 2109, 2130, 2149, 2161, 2300, 2330, 2332}

prefix_sum = {304, 523, 528, 713, 813, 848, 930, 974, 1004, 1094, 1208, 1248}

#Problems from NeetCode 150 list
neet_code_150 = {2, 3, 5, 7, 11, 15, 17, 19, 22, 33, 36, 39, 40, 42, 43, 45, 46, 48, 49, 50, 53, 54, 55, 56, 57, 62, 72,
                 73, 74, 78, 79, 90, 91, 97, 98, 102, 105, 128, 130, 131, 133, 134, 138, 139, 143, 146, 150, 152,
                 153, 155, 167, 198, 199, 200, 207, 208, 210, 211, 213, 215, 230, 235, 238, 253, 261, 271, 286, 287,
                 300, 309, 322, 323, 347, 355, 371, 416, 417, 424, 435, 494, 518, 567, 621, 647, 678, 684, 695, 739,
                 743, 763, 787, 846, 853, 875, 973, 981, 994, 1143, 1448, 1584, 1899, 2013}

neet_code_priority = {424, 3, 567,                                          #Sliding Window
                      5, 647, 167, 11, 15, 143, 19, 567, 763, 253, 287}     #Two Pointers

#LeetCode Top Interview 150 questions
leetcode_top_interview_150 = {1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 30, 33,
                              34, 35, 36, 39, 42, 45, 46, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 61, 63, 64, 66, 67,
                              68, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 86, 88, 92, 97, 98, 100, 101, 102, 103,
                              104, 105, 106, 108, 112, 114, 117, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 133,
                              134, 135, 136, 137, 138, 139, 141, 146, 148, 149, 150, 151, 153, 155, 162, 167, 169, 172,
                              173, 188, 189, 190, 191, 198, 199, 200, 201, 202, 205, 207, 208, 209, 210, 211, 212, 215,
                              219, 221, 222, 224, 226, 228, 230, 236, 238, 242, 274, 289, 290, 295, 300, 322, 373, 380,
                              383, 392, 399, 427, 433, 452, 502, 530, 637, 909, 918}

# Google interview problems, feel welcomed to additional questions
google_interview = {1007, 1161, 1573}

#I would be grateful if you could add list with questions from other companies


# Lists of problems that are solved, poorly understood, need revisiting
solved =set()
poorly_understood = set() # Solved, but to be reviewed later
to_revisit = set() #solved okay, and yet feel like revisiting it later


# List of problems to exclude. Default is to exclude solved but not in priority list
exclude = solved - (neet_code_150 | google_interview | leetcode_top_interview_150 | poorly_understood | to_revisit)

all_problems = sliding_window_problems | two_pointers_problems | prefix_sum | neet_code_150 | google_interview | leetcode_top_interview_150


def get_random_problems(problems: set | tuple = tuple(all_problems), exclude: set| tuple = tuple(exclude), n: int = 10):
    choice_set = list(set(problems) - set(exclude))
    random_problems = {random.choice(choice_set) for _ in range(n)}
    return random_problems



print(get_random_problems())