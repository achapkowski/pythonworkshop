import datetime 
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
today = int(datetime.datetime.timestamp(today)) * 1000
yesterday = int(datetime.datetime.timestamp(yesterday)) * 1000
items = GIS().content.search("created: [{yesterday} TO {today}]".format(yesterday=yesterday, today=today), 
                             max_items=100000)
print("Number of Items: {n}".format(n=len(items)))