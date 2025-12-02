import requests, time

def god_mint():
    print("Immutable X — God Mint Detector (10 000+ NFTs minted in one tx)")
    seen = set()
    while True:
        r = requests.get("https://api.x.immutable.com/v1/mints?page_size=50&order_by=created_at&direction=desc")
        for mint in r.json().get("result", []):
            txid = mint["transaction_id"]
            if txid in seen: continue
            seen.add(txid)

            # Batch mint via official minting contract
            if mint.get("status") != "success": continue
            user = mint["user"]
            count = len([m for m in r.json()["result"] if m["user"] == user and m["transaction_id"] == txid])

            if count >= 10_000:
                collection = mint.get("metadata", {}).get("collection_name", "Unknown")
                print(f"GOD MINT DETECTED\n"
                      f"{count:,} NFTs minted in ONE transaction\n"
                      f"Collection: {collection}\n"
                      f"Creator: {user}\n"
                      f"Tx: https://immutable.com/tx/{txid}\n"
                      f"https://market.immutable.com/assets/{mint['token']['data']['id']}\n"
                      f"→ Someone just created an entire game/world in seconds\n"
                      f"→ Usually AAA studio drop, guild tool, or metaverse land\n"
                      f"{'-'*80}")
        time.sleep(3.2)

if __name__ == "__main__":
    god_mint()
