import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

df=pd.read_csv("Project109/data.csv")
readScore=df["reading score"].to_list()
writeScore=df["writing score"].to_list()

mean=sum(readScore)/len(readScore)
print(mean)

mean1=sum(writeScore)/len(writeScore)
print(mean)

median=statistics.median(readScore)
print(median)

median1=statistics.median(writeScore)
print(median1)

mode=statistics.mode(readScore)
print(mode)

mode1=statistics.mode(writeScore)
print(mode1)

stdDeviation=statistics.stdev(readScore)
print(stdDeviation)

stdDeviation=statistics.stdev(writeScore)
print(stdDeviation)

first_stdDeviation_start, first_stdDeviation_end = mean-stdDeviation, mean+stdDeviation
second_stdDeviation_start, second_stdDeviation_end = mean-(2*stdDeviation), mean+(2*stdDeviation)
third_stdDeviation_start, third_stdDeviation_end = mean-(3*stdDeviation), mean+(3*stdDeviation)

list_of_read_within_1_stdDeviation = [result for result in readScore if result > first_stdDeviation_start and result < first_stdDeviation_end]
list_of_read_within_2_stdDeviation = [result for result in readScore if result > second_stdDeviation_start and result < second_stdDeviation_end]
list_of_read_within_3_stdDeviation = [result for result in readScore if result > third_stdDeviation_start and result < third_stdDeviation_end]

list_of_write_within_1_stdDeviation = [result for result in writeScore if result > first_stdDeviation_start and result < first_stdDeviation_end]
list_of_write_within_2_stdDeviation = [result for result in writeScore if result > second_stdDeviation_start and result < second_stdDeviation_end]
list_of_write_within_3_stdDeviation = [result for result in writeScore if result > third_stdDeviation_start and result < third_stdDeviation_end]

print("Mean of read is {}".format(mean))
print("Median of read is {}".format(median))
print("Mode of read is {}".format(mode))
print("Standard deviation of read is {}".format(stdDeviation))
print("{}% of read lies within 1 standard deviation".format(len(list_of_read_within_1_stdDeviation)*100.0/len(readScore)))
print("{}% of read lies within 2 standard deviations".format(len(list_of_read_within_2_stdDeviation)*100.0/len(readScore)))
print("{}% of read lies within 3 standard deviations".format(len(list_of_read_within_3_stdDeviation)*100.0/len(readScore)))

print("Mean of write is {}".format(mean1))
print("Median of write is {}".format(median1))
print("Mode of write is {}".format(mode1))
print("Standard deviation of write is {}".format(stdDeviation))
print("{}% of write lies within 1 standard deviation".format(len(list_of_write_within_1_stdDeviation)*100.0/len(writeScore)))
print("{}% of write lies within 2 standard deviations".format(len(list_of_write_within_2_stdDeviation)*100.0/len(writeScore)))
print("{}% of write lies within 3 standard deviations".format(len(list_of_write_within_3_stdDeviation)*100.0/len(writeScore)))