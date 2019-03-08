
import pandas as pd


dataSet = pd.read_html("https://www.wrh.noaa.gov/mesowest/getobext.php?wfo=sto&sid=KEDU&num=72&raw=0")
len(dataSet)
dataSet[0]
dataSet[1]



## Min-Yao

dataSet = pd.read_html("https://ndb.nal.usda.gov/ndb/search/list")
len(dataSet)

USDA = dataSet[0]
USDA.head()
Manufacturer_stamps = USDA['Food Group or Manufacturer']
Manufacturer_stamps.value_counts()


## John Davis
wikiPython = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)")
type(wikiPython)
pythonTypes = wikiPython[1]
pythonTypes.head()
pythonTypes.columns = pythonTypes.iloc[0]
pythonTypes = pythonTypes.drop(0)
pythonTypes.head(2)
pythonTypes[pythonTypes.mutable == "immutable"]
pythonTypes[pythonTypes.mutable != "mutable"]

[type(each) for each  in pythonTypes["mutable"] ]

pythonTypes_sansNA = pythonTypes[[type(each) == str for each in pythonTypes["mutable"]]]
pythonTypes_sansNA[pythonTypes_sansNA.mutable == "immutable"]
