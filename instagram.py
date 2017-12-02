#Data analaysis using Instagram
from IPython.display import Image
from IPython.display import display

from InstagramAPI import InstagramAPI
username=""
InstagramAPI = InstagramAPI(username,"password")
InstagramAPI.login()

InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
print(result)
#All the results are stored in Json format

#print (result['user']['biography'])

InstagramAPI.timelineFeed()
result1 = InstagramAPI.LastJson
#print(result1[text])


#List of all the posts
import time
myposts=[]
has_more_posts = True
max_id=""

while has_more_posts:
    InstagramAPI.getSelfUserFeed(maxid=max_id)
    if InstagramAPI.LastJson['more_available'] is not True:
        has_more_posts = False #stop condition
        print ("stopped")
    
    max_id = InstagramAPI.LastJson.get('next_max_id','')
    myposts.extend(InstagramAPI.LastJson['items']) #merge lists
    time.sleep(2) # Slows the script down to avoid flooding the servers 
    



