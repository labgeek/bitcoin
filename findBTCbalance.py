import requests

# API Token and Bitcoin address
API_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BITCOIN_ADDRESS = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def get_bitcoin_balance(address: str, api_token: str) -> float:
    """
    Fetch the Bitcoin balance of the given address using Blockcypher API.
    """
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance?token={api_token}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for HTTP issues
        data = response.json()
        
        # Balance is returned in satoshis, convert to BTC
        balance_in_btc = data.get("balance", 0) / 1e8
        return balance_in_btc
    except requests.exceptions.RequestException as e:
        print(f"Error fetching balance: {e}")
        return -1

def main():
    print("Blockcypher Bitcoin Balance Checker")
    
    print(f"Checking balance for Bitcoin address: {BITCOIN_ADDRESS}")
    balance = get_bitcoin_balance(BITCOIN_ADDRESS, API_TOKEN)
    
    if balance == -1:
        print("Failed to fetch balance. Please check the address or try again later.")
    else:
        print(f"The balance of the address {BITCOIN_ADDRESS} is {balance:.8f} BTC.")

if __name__ == "__main__":
    main()
