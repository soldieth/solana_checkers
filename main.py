import requests
import os


def check_wallets(wallets, chain):
    print(f"{chain.capitalize()} WALLETS:")
    oneEligible = False
    for wallet in wallets:
        url = f"https://airdrop.pyth.network/api/grant/v1/amount_and_proof?ecosystem={chain}&identity={wallet}"
        r = requests.get(url)
        if f"No result found for {chain} identity" not in str(r.json()):
            print(f"{wallet} - {int(r.json()['amount']) / 1000000}")
            oneEligible = True
    if not oneEligible:
        print(f"No {chain} wallets eligible")


if __name__ == '__main__':
    chains = ['solana', 'evm', 'injective', 'sui', 'aptos', 'sei', 'osmosis', 'neutron']
    chains_to_check = []
    for chain in chains:
        file_name = f"{chain}_wallets.txt"
        if os.path.getsize(file_name) != 0:
            chains_to_check.append(chain)
    for chain in chains_to_check:
        with open(f"{chain}_wallets.txt", "r") as file:
            wallets = file.read().split("\n")
        if wallets:
            check_wallets(wallets, chain)
    input()
