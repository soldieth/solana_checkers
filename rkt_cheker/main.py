import requests


def check_wallet(wallet):
    url = "https://racket.wtf/api/trpc/claim.checkClaim?batch=1"
    data = {"0": {
        "json": {
            "address": wallet
        }}
    }
    r = requests.post(url, json=data).json()
    if r[0]['result']['data']['json']['claim']:
        text = f"{wallet} - {r[0]['result']['data']['json']['claim']['totalRkt']}\n"
        return text
    else:
        return False


if __name__ == '__main__':
    with open("wallets.txt", "r") as file:
        wallets = file.read().split('\n')
    with open("eligible_wallet.txt", "a") as file:
        for wallet in wallets:
            text = check_wallet(wallet)
            if text:
                print(text)
                file.write(text)
    print("Check completed. All eligible wallets in eligible_wallet.txt")
