import requests
import os

class FootballApi:

    def __init__(self):
        self.base_url = os.getenv("FOOTBALL_API_URL")
        self.headers = {"X-Auth-Token": os.getenv("FOOTBALL_API_TOKEN")}

    def api_request(self, endpoint):
        
        url = self.base_url+endpoint
        response = requests.get(url=url,headers=self.headers)

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 429:
                raise Exception(
                    f"""Limite da API atingido. {response.json()["message"]}""")
        
        else:
            print("Erro: ", response.status_code, response.text)
            return None
        
    def get_competition_bsa(self):

        return self.api_request("competitions/BSA")

    def get_standings(self):

        return self.api_request("competitions/BSA/standings")
    
    def get_matches(self):

        return self.api_request("competitions/BSA/matches")
    
    def get_scorers(self):

        return self.api_request("competitions/BSA/scorers?limit=15")

    