import requests


subpage_list = ['admin.php', 'wp-admin', 'control-panel', 'admin', 'shop/Admin.php']


def main():
  print("Welcome to MrCrowley a tool desing to crawl into webpages and try to find admin pages\n")
  url =  input("Type the url ex[https://test.com]:")
  crawl(url)

def crawl(url):
  
  try:
    
    for subpage in subpage_list:
  	  r = requests.head(url + "/" + subpage)

  	  if r.status_code == 200: #check if the site responds 200 
  		  print("Found admin page:\n")
  		  print(url + "/" + subpage)
	  	  exit()
	
  except SSLCertVerificationError:
    print("You got a problem with the SSL certificate on provided page!")
    exit()



if __name__ == "__main__":
  main()


