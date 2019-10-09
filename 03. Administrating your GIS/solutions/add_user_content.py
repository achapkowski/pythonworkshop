fp = "./data/rivers.gdb.zip"
item_properties = {
    'title' : "US Rivers",
    'type' : 'File Geodatabase',
    'tags' : ['Rivers']
}
river_item = gis.content.add(data=fp, item_properties=item_properties, owner=user)
p_river = river_item.publish()
p_river
