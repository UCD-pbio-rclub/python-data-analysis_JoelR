import pandas as pd
import seaborn as sns


airports = pd.read_csv('https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv')
weather = pd.read_csv('https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv')
airports.head(10)

weather.head(10)



weather.boxplot(column=["temp"],by=["origin","month"])
weather.boxplot(column=["temp"],by=["origin"])


df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
                          columns=['A', 'B', 'C', 'D'],
                          index=np.arange(0, 100, 10))


df.plot(color = s.sort_index().values)
weather[['origin',"temp"]].set_index(['origin']).plot()


subW = weather[(weather.month == 1) & (weather.day == 1)]
subW[["origin","temp"]].boxplot(by="origin")



weather.head(1)


dat = weather[(weather.month==1) & (weather.day==1)]
sns.lineplot(data=dat, x="hour",y="temp",hue="origin",style="origin",palette="tab10", linewidth=2.5)


dat = weather[(weather.month==12)]
sns.lineplot(data=dat, x="hour",y="temp",hue="origin",style="origin",palette="tab10", linewidth=2.5)


dat = weather[(weather.month==7)]
sns.lineplot(data=dat, x="day",y="temp",hue="origin",style="origin", linewidth=2.5)
