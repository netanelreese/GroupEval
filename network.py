#import requests
from pip._vendor import requests
from canvasapi import *
import config

class Network:
    API_LINK = config.API_URL
    API_KEY = config.API_KEY
    COURSE_ID = config.COURSE_ID
    GROUP_CATEGORY_ID = config.GROUP_CATEGORY_ID
    CANVAS = Canvas(API_LINK, API_KEY)
    COURSE = CANVAS.get_course(COURSE_ID)
    HEADER = {'Authorization' : 'Bearer ' + config.API_KEY }
    def get_groups(self):
        groups = Network.COURSE.get_groups()
        return groups
    def get_students_from_group_id(self, group_id):
        groups = Network.COURSE.get_groups()
        for group in groups:
            if (group == group_id):
                return group.get_users()
            else:
                print("Fuck you asshole you gave us the wrong id")
    def make_group(self, group_name, category_id):
        category = Network.COURSE.get_group_categories()[0]
        category.create_group(group={'name': 'Maddie Quiroga'})
        groups = category.get_groups()
        for group in groups:
            if (group.name == "Maddie Quiroga"):
                return group.name
            else:
                return "failed to create group"
    def add_members_to_group(self, member_string, group_id):
        endpoint = 'groups/%s' % group_id
        body = { 'members' : member_string }
        response = self.put_network_call(endpoint, body)
        return response
    def delete_student_made_group(self, group_id):
        endpoint = 'groups/%s' % group_id
        response = self.delete_network_call(endpoint)
        return response
    def delete_network_call(self, endpoint):
        response = requests.delete(self.API_LINK + endpoint, headers = self.HEADER)
        return response.json()
    def post_network_call(self, endpoint, body):
        response = requests.post(self.API_LINK + endpoint, headers = self.HEADER, data=body)
        return response.json()
    def get_network_call(self, endpoint):
        response = requests.get(self.API_LINK + endpoint, headers = self.HEADER)
        return response.json()
    def put_network_call(self, endpoint, body):
        response = requests.put(self.API_LINK + endpoint, headers = self.HEADER, data=body)
        return response.json()
