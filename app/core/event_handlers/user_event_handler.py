from api.model import User

class UserEventHandler:

    def subscribe(self):
        pass

    def handle_user_created(self, user:User):
        pass
    
    def handle_user_deleted(self, user_id:int):
        pass

user_event_handler= UserEventHandler()
        