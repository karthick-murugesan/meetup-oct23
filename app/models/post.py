from pydantic import BaseModel

class UserPost(BaseModel):
    first_name:str
    last_name:str
    college:str
    email:str
    contact:str
    radio_set1:str
    radio_set2:str
    radio_set3:str
    radio_set4:str
    radio_set5:str
    about_the_event:str
    future_meetup_topics:str
    feedback:str
    
class post_item(BaseModel):
    link : str