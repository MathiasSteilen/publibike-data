import pandas as pd
from tqdm.notebook import tqdm
from datetime import datetime
import requests
import os

SAVE_DIR = ("Data")

if __name__ == "__main__":

    # Call the API
    response = requests.get(
        "https://api.publibike.ch/v1/public/partner/stations")
    content = response.json()

    stations = pd.json_normalize(content["stations"], sep="_").assign(
        timestamp=pd.to_datetime(datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    # get datetime col to front
    stations = pd.concat(
        [stations["timestamp"], stations.drop("timestamp", axis=1)], axis=1)

    # get the information from the nested columns about actual bikes at stations
    # and the sponsors associated with them
    bike_df_list = []
    sponsor_df_list = []

    for station_id, vehicle_info, sponsor_info in zip(
        stations["id"], stations["vehicles"], stations["sponsors"]
    ):
        # Expand the bike information into separate df to large back onto the main df later
        bike_df = pd.json_normalize(
            vehicle_info, sep="_").assign(station_id=station_id)
        bike_df_list.append(bike_df)

        # same for the sponsors
        sponsor_df = pd.json_normalize(
            sponsor_info, sep="_").assign(station_id=station_id)
        sponsor_df_list.append(sponsor_df)

    bikes = pd.concat(bike_df_list).rename(
        columns={"id": "bike_id", "name": "bike_name"})

    sponsors = pd.concat(sponsor_df_list).rename(
        columns={"id": "sponsor_id", "name": "sponsor_name"})

    # Create big dataframe to be written to csv from smaller ones
    df = (
        stations.merge(bikes, how="left", left_on="id", right_on="station_id")
        .drop("station_id", axis=1)
        .merge(sponsors, how="left", left_on="id", right_on="station_id")
        .drop(
            [
                "station_id",
                "vehicles",
                "sponsors",
                "network_background_img",
                "network_logo_img",
                "network_sponsors",
                "image",
                "url",
            ],
            axis=1,
        )
        .rename(columns={"id": "station_id", "name": "station_name", "capacity": "station_capacity",
                         "type_id": "bike_type_id", "type_name": "bike_type_name"})
    )

    # If folder doesn't exist, then create it.
    if not os.path.isdir(SAVE_DIR):
        os.makedirs(SAVE_DIR)
        df.to_csv(
            f"Data/publibikes_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv", index=False)
    else:
        # Write to csv with appropriate title
        df.to_csv(
            f"Data/publibikes_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv", index=False)