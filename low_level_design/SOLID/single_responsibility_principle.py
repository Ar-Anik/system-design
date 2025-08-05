"""
1. A class should have one, only one reason to change.

> A class can have many methods, as long as all of them serve a single purpose or responsibility.
"""

class UserManager:
    def authenticate_user(self, username, password):
        print("Authentication Logic")

    def update_user_profile(self, user_id, new_profile_data):
        print("Profile Update Logic")

    def send_email_notification(self, user_email, message):
        print("Email Sending Logic")


"""
This class violates the SRP because it has multiple responsibilities: authentication, profile management 
and email notifications.

So, we can write :
"""

class UserAuthenticator:
    def authenticate_user(self, username, password):
        print("Authentication Logic")

class UserProfileManager:
    def update_user_profile(self, user_id, new_profile_data):
        print("Profile Update Logic")

class EmailNotifier:
    def send_email_notification(self, user_email, message):
        print("Email Sending Logic")


"""
> Benefits:
    * Improved maintainability: Changes are easier to make and test.
    * Easier debugging: Less complexity per class.
    * Better readability and organization: Class responsibilities are clear and focused.
    * Reusability: Smaller, focused classes are easier to reuse elsewhere.
"""