import requests


subpage_list = ['admin.php', 'wp-admin', 'control-panel', 'admin', 'shop/Admin.php']

url = "https://roldf.org"


for subpage in subpage_list:
	r = requests.head(url + "/" + subpage)

	if r.status_code == 200: #check if the site responds 200 
		print("Found admin page:\n")
		print(url + "/" + subpage)
		exit()
	
print("Something went wrong or not found admin page!")



