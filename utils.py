import requests
import json
from datetime import datetime

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
        request_id = datetime.now().strftime("%Y%m%d%H%M%S")
        if response.status_code == 200:
            content = response.text.replace(')]}\'\n', '')
            data = json.loads(content)

            item = data[0][1]
            result = []
            index = 0
            for i in range(0, len(item)):
                adr = dict()
                try:
                    element = item[i][14]
                    if element[30] == 'Africa/Algiers':
                        adr = {
                            'query': query,
                            'request_id': request_id,
                            'index': index,
                            "coordinate": [element[9][2], element[9][3]],
                            'data_0': element[0],
                            'data_1': element[1],
                            'data_2': element[2],
                            'data_3': element[10],
                            'data_4': element[11],
                            'data_5': element[13],
                            'data_6': element[14],
                            'data_7': element[18],
                        }
                        index += 1
                except Exception as e:
                    pass
                if adr:
                    result.append(adr)

            return dict(
                type="success",
                data=result
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
            status=500,
            message=str(e)
        )
    return dict(
        type='error',
        status=400,
        message="query not valide",
    )


