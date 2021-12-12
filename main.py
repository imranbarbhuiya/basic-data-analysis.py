import pandas

data = pandas.read_csv("census_data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data.csv", index=False)
