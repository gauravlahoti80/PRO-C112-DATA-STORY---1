# importing the modules
import random
import plotly.figure_factory as ff
import numpy as np
import statistics
import plotly.graph_objects as go
import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()


with open("data.csv", newline="") as f:
    csv_object = csv.reader(f)
    filelist = list(csv_object)
    filelist.pop(0)
    # print(filelist)

    #printing filelist
    print(filelist)

remainder = 0
money_saved_who_got_remainded = []
money_saved_who_did_not_got_remainded = []

for i in range(0, len(filelist)):
    if int(filelist[i][3]) == 1:
        remainder = remainder + 1
        money_saved_who_got_remainded.append(float(filelist[i][0]))
    else:
        money_saved_who_did_not_got_remainded.append(float(filelist[i][0]))

print(remainder)

remainder_not_sent = len(filelist) - remainder
print(remainder_not_sent)

graph = go.Figure(go.Bar(
    x=["remainder", "remainder_not_sent"],
    y=[remainder, remainder_not_sent],
))
graph.show()


quant_saved = df["quant_saved"].tolist()
age = df["age"].tolist()
mean_of_quant_saved = statistics.mean(quant_saved)
print(mean_of_quant_saved)

median_of_quant_saved = statistics.median(quant_saved)
print(median_of_quant_saved)

mode_of_quant_saved = statistics.mode(quant_saved)
print(mode_of_quant_saved)

# print(money_saved_who_got_remainded)
# print(money_saved_who_did_not_got_remainded)

# finding mean median mode for the peole who were sent remainder

mean_of_remainder = statistics.mean(money_saved_who_got_remainded)
print(mean_of_remainder)

mean_of_did_not_got_remainder = statistics.mean(
    money_saved_who_did_not_got_remainded)
print(mean_of_did_not_got_remainder)

median_of_remainder = statistics.median(money_saved_who_got_remainded)
print(median_of_remainder)

median_of_did_not_got_remainder = statistics.median(
    money_saved_who_did_not_got_remainded)
print(median_of_did_not_got_remainder)

mode_of_remainder = statistics.mode(money_saved_who_got_remainded)
print(mode_of_remainder)

mode_of_did_not_got_remainder = statistics.mode(
    money_saved_who_did_not_got_remainded)
print(mode_of_did_not_got_remainder)

dict = {
    'x': age,
    'y': quant_saved
}
correlation = np.corrcoef(dict['x'], dict['y'])
print(correlation)


fig = ff.create_distplot([quant_saved], ["Quantity Saved"], show_hist=False)
fig.show()

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)

iqr = q3-q1
lower_whisker = q1-1.5*iqr
upper_whisker = q3+1.5*iqr
print(lower_whisker, upper_whisker)

new_df = df[df["quant_saved"] < upper_whisker]


new_df = new_df["quant_saved"].tolist()
mean_of_new_df = statistics.mean(new_df)
print(mean_of_new_df)

median_of_new_df = statistics.median(new_df)
print(median_of_new_df)

mode_of_new_df = statistics.mode(new_df)
print(mode_of_new_df)


fig = ff.create_distplot([new_df], ["Quantity Saved"], show_hist=False)
fig.show()


final_list = []


def getRandomValues():
    sample_data = []
    for i in range(0, 100):
        random_value = random.randint(0, len(new_df)-1)
        value = new_df[random_value]
        sample_data.append(value)
    mean = statistics.mean(sample_data)
    final_list.append(mean)


for i in range(0, 1000):
    getRandomValues()

fig = ff.create_distplot([final_list], ["Sampling Data"], show_hist=False)
fig.show()

print(statistics.mean(new_df), statistics.mean(final_list))
print(statistics.stdev(new_df), statistics.stdev(final_list))
