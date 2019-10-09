user = gis_agol.users.create(firstname="Demo", lastname="Account2",
                             user_type="creatorUT",
                             username="entitleduser",
                             password="flimFLAM2!",
                             email="fakeperson@esri.com")
r = pro_license.report
print(r[r['Entitlement'] == 'desktopStdN'])
pro_license.assign(username=user.username, entitlements="desktopStdN")
r = pro_license.report
r[r['Entitlement'] == 'desktopStdN']