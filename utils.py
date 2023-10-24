import requests
import json

def google_map_geocoding(query, token):
    try:
        url = 'https://www.google.com/search'
        params = dict(
            gl="dz",
            tbm="map",
            q=query,
            nfpr=1,
            pb=token
        )
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            content = response.text.replace(')]}\'\n', '')
            data = json.loads(content)
            return dict(
                type="success",
                coordinate=[data[0][1][0][14][9][2], data[0][1][0][14][9][3]],
                address=data[0][1][0][14][11]
            )
        else:
            return dict(
                type='error',
                status=response.status_code,
                message=response.text
            )
    except Exception as e:
        print("Exception: ", e)
        return dict(
            type='error',
            satus=500,
            message=str(e)
        )
    return dict(
        type='error',
        status="400",
        message="query not valide",
    )


