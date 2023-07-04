import read_file
from Ga import *
from Solution import *

data = {}
# Small
# data["Small/input_6_4_2.txt"] = [6, 4, 2]
# data["Small/input_8_4_3.txt"] = [8, 4, 3]
# data["Small/input_10_4_3.txt"] = [10, 4, 3]
# data["Small/input_10_6_3.txt"] = [10, 6, 3]
# data["Small/input_12_6_4.txt"] = [12, 6, 4]
# # Medium
# data["Medium/input_12_8_4.txt"] = [12, 8, 4]
# data["Medium/input_14_8_4.txt"] = [14, 8, 4]
# data["Medium/input_14_10_5.txt"] = [14, 10, 5]
# data["Medium/input_16_10_6.txt"] = [16, 10, 6]
# data["Medium/input_16_12_6.txt"] = [16, 12, 6]
# # Large
# data["Large/input_18_12_6.txt"] = [18, 12, 6]
# data["Large/input_18_14_8.txt"] = [18, 14, 8]
# data["Large/input_20_14_8.txt"] = [20, 14, 8]
# data["Large/input_24_14_10.txt"] = [24, 14, 10]
# data["Large/input_24_16_10.txt"] = [24, 16, 10]
# # Extra-large 
# data["Extra-large/input_26_16_12.txt"] = [26, 16, 12]
# data["Extra-large/input_30_18_12.txt"] = [30, 18, 12]
# data["Extra-large/input_40_18_12.txt"] = [40, 18, 12]
# data["Extra-large/input_40_20_14.txt"] = [40, 20, 14]
# data["Extra-large/input_50_24_16.txt"] = [50, 24, 16]

# Data thầy:
# data["Data/input6.txt"] = [6, 4, 2]
# data["Data/input5.txt"] = [10, 4, 2]
# data["Data/input7.txt"] = [50, 15, 5]
# data["Data/input8.txt"] = [100, 30, 10]
# data["Data/input1.txt"] = [200, 50, 20]
data["Data/input2.txt"] = [300, 50, 30]
data["Data/input3.txt"] = [500, 100, 50]
data["Data/input4.txt"] = [600, 150, 60]
data["Data/input9.txt"] = [800, 200, 80]
data["Data/input10.txt"] = [1000, 200, 100]


for file_name in data.keys():

    input = read_file.read(file_name)

    sol = Solution(input)

    N = 20
    Gen = 10

    ga = Ga(N, Gen, sol)
    ga.run()
