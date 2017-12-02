#Data analaysis using Instagram
from IPython.display import Image
from IPython.display import display

from InstagramAPI import InstagramAPI
username="krisha_mehta"
InstagramAPI = InstagramAPI(username,"prideandprejudice")
InstagramAPI.login()

InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
#print(result)
#All the results are stored in Json format

#print (result['user']['biography'])

InstagramAPI.timelineFeed()
#result1 = InstagramAPI.LastJson
#print(result1[text])

#Get_posts_from_list()
#Get_url()
#image_urls = InstagramAPI.LastJson
#image_urls



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
    
profile_pic = myposts[0]['caption']['user']['profile_pic_url']
img = Image(profile_pic)
display(profile_pic)


