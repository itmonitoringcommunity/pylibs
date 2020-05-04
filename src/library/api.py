# -*- coding: utf-8 -*-
import json
import requests


class CustomApi():
    def __init__(self, APIURL):
        self.url = APIURL
        self.username = ''
        self.password = ''
        self.token = ''
        self.is_login = 0
        self.msg = ''
        self.id = ''
        self.bulletin = None
        self.scheduledBulletins = None
        self.startedBulletins = None

    def login(self, USERNAME, PASSWORD):
        self.username = USERNAME
        self.password = PASSWORD
        self.__api_login()

    def logout(self):
        self.is_login = 0
        self.token = ''
        self.msg = 'Good Bye..!!!'

    def get_bulletin(self):
        self.__api_get_bulletin()
        self.id = self.bulletin["id"]

    def get_scheduled_bulletins(self):
        self.__api_get_scheduled_bulletins()

    def get_started_bulletins(self):
        self.__api_get_started_bulletins()

    def send_bulletin(self):
        self.__api_send_bulletin()

    def set_bulletin(self):
        self.__api_set_bulletin()

    def __api_login(self):
        result = ""

        try:
            session = requests.Session()
            headers = {
                "content-type": "application/json"
            }
            values = {
                "username": self.username,
                "password": self.password
            }
            response = session.post(
                url=self.url + 'rest-auth/login/',
                data=values
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "Welcome !!!"
                self.token = result["key"]
            except KeyError as e:
                self.is_login = 0
                self.msg = "Username or password is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)

    def __api_get_bulletin(self):
        result = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            response = session.get(
                url=self.url + 'bulletins/' + self.id,
                headers=head
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "You get bulletin information"
                self.bulletin = result

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)

    def __api_send_bulletin(self):
        result = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            response = session.get(
                url=self.url + 'bulletins/' + self.id + '/send/',
                headers=head
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "You sent bulletin mail"

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)

    def __api_get_scheduled_bulletins(self):
        results = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            values = {
                'page': '1',
                'search': 'Scheduled'
            }
            response = session.get(
                url=self.url + 'bulletins/',
                data=values,
                headers=head
            )
            session.close()
            try:
                results = json.loads(response.content)
                self.is_login = 1
                self.msg = "You get bulletin information"
                self.scheduledBulletins = results["results"]

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)

    def __api_get_started_bulletins(self):
        results = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            values = {
                'page': '1',
                'search': 'Started'
            }
            response = session.get(
                url=self.url + 'bulletins/',
                data=values,
                headers=head
            )
            session.close()
            try:
                results = json.loads(response.content)
                self.is_login = 1
                self.msg = "You get bulletin information"
                self.startedBulletins = results["results"]

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)

    def __api_set_bulletin(self):
        result = ""

        try:
            session = requests.Session()
            head = {
                "content-type": "application/json",
                "Authorization": "Token " + self.token
            }
            values = {
                'smtp': self.bulletin["smtp"],
                'port': self.bulletin["port"],
                'username': self.bulletin["username"],
                'password': self.bulletin["password"],
                'tolist': self.bulletin["tolist"],
                'cclist': self.bulletin["cclist"],
                'bcclist': self.bulletin["bcclist"],

                'btype': self.bulletin["btype"],
                'priority': self.bulletin["priority"],
                'state': self.bulletin["state"],
                'color': self.bulletin["color"],

                'created_by': self.bulletin["created_by"],
                'code': self.bulletin["code"],
                'title': self.bulletin["title"],
                'detail': self.bulletin["detail"],
                'effect': self.bulletin["effect"],
                'contact': self.bulletin["contact"],

                'begin_time': self.bulletin["begin_time"],
                'end_time': self.bulletin["end_time"],
                'duration': self.bulletin["duration"],

                'ticket_case_url': self.bulletin["ticket_case_url"],
                'ticket_case_id': self.bulletin["ticket_case_id"],

                'resolved_time': self.bulletin["resolved_time"],
                'is_resolved': self.bulletin["is_resolved"],
                'resolved_by': self.bulletin["resolved_by"],
                'temporary_solution': self.bulletin["temporary_solution"],
                'permanent_solution': self.bulletin["permanent_solution"],
                'root_cause': self.bulletin["root_cause"],

                'insert_time': self.bulletin["insert_time"],
                'modify_time': self.bulletin["modify_time"],
                'is_automated': self.bulletin["is_automated"],
                'is_deleted': self.bulletin["is_deleted"]
            }
            response = session.put(
                url=self.url + 'bulletins/' + self.id + '/update/',
                json=values,
                headers=head
            )
            session.close()
            try:
                result = json.loads(response.content)
                self.is_login = 1
                self.msg = "You set bulletin information"

            except KeyError as e:
                self.msg = "Some parameters is invalid."

        except requests.exceptions.HTTPError as errh:
            self.msg = "Http Error: " + str(errh)
        except requests.exceptions.ConnectionError as errc:
            self.msg = "Error Connecting: " + str(errc)
        except requests.exceptions.Timeout as errt:
            self.msg = "Timeout Error: " + str(errt)
        except requests.exceptions.RequestException as err:
            self.msg = "OOps: Something Else " + str(err)
