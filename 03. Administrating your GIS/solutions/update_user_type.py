print((user.userLicenseTypeId, user.role))
user.update_license_type(user_type="creatorUT")
user.update_role("org_publisher")
print((user.userLicenseTypeId, user.role))
