from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/wallet-movement/<address>', methods=['GET'])
def get_wallet_movement(address):
    cookies = {
        '_ga': 'GA1.1.2113811878.1732235985',
        '_clck': '1djpu3l%7C2%7Cfr8%7C0%7C1787',
        '_clsk': 'ev8mp6%7C1732676642494%7C3%7C1%7Cb.clarity.ms%2Fcollect',
        '_ga_JDVWTH2QBN': 'GS1.1.1732676607.3.1.1732676662.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://layerhub.xyz/search?p=berachain',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
        'content-type': 'application/json',
        'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    # URL now includes the address dynamically from the route
    url = f'https://layerhub.xyz/be-api/protocol_wallets/movement/{address}'
    
    response = requests.get(url, cookies=cookies, headers=headers)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
