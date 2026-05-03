from api.football import FootballApi
from etl import transform_json
from dotenv import load_dotenv
import pandas as pd

def load_data():

    load_dotenv()

    api = FootballApi()

    return {

       "brasileirao":
            transform_json.transform_bsa(
                api.get_competition_bsa()
            ),
        
        "classificacao":
            transform_json.transform_standings(
                api.get_standings()
            ),
        
        "partidas":

            transform_json.transform_mactches(
                api.get_matches()
            ),

        "artilheiros":
            transform_json.transform_scorers(
                api.get_scorers()
            )
    }

if __name__ == "__main__":

    json = load_data()