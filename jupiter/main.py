import csv
import requests


def check_jup(wallet):
    headers = {
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Referer': 'https://airdrop.jup.ag/',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    try:
        r = requests.get(f'https://jup-airdrop.zhen8558.workers.dev/allocation/{wallet.lower()}', headers=headers).json()
        print(f"{wallet} - {r['tokens_final']}")
        return [wallet, r['tokens_final']]
    except requests.exceptions.JSONDecodeError:
        print(f"No tokens for {wallet}")


if __name__ == '__main__':
    with open("wallets.txt", "r") as file:
        wallets = file.read().split('\n')
    all_pairs = list()
    for wallet in wallets:
        pair = check_jup(wallet)
        all_pairs.append(pair)
    with open('checked_wallets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['wallet', 'tokens'])
        writer.writerows(all_pairs)