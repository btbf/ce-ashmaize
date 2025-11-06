#!/usr/bin/env python3
import json
import os
import requests
from collections import defaultdict

# === Settings ===
API_URL = "https://scavenger.prod.gd.midnighttge.io/work_to_star_rate"
CHALLENGE_FILE = "challenges.json"

# === Helpers ===
def short_addr(addr: str) -> str:
    return addr[:10] + "..." + addr[-10:] if len(addr) > 20 else addr

def format_num(n):
    return f"{n:,}"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

# === Main ===
def main():
    if not os.path.exists(CHALLENGE_FILE):
        print(f"❌ File not found: {CHALLENGE_FILE}")
        return

    # Fetch reward rate array
    try:
        rate_array = requests.get(API_URL, timeout=10).json()
        days_available = len(rate_array)
        print(f"✅ Retrieved reward rates for {days_available} campaign days.")
        print("📊 Reward rates per day (1 NIGHT = 1,000,000 STAR):")
        for i, r in enumerate(rate_array, 1):
            print(f"   • Day {i}: {format_num(r)} STAR ({r/1_000_000:.6f} NIGHT)")
        print()
    except Exception as e:
        print(f"⚠️ Failed to fetch rate data: {e}")
        return

    data = load_json(CHALLENGE_FILE)

    # Aggregation containers
    daily = defaultdict(lambda: defaultdict(lambda: {
        "expired": 0, "invalid": 0, "started": 0, "validated": 0, "other": 0,
        "total_STAR": 0, "total_NIGHT": 0.0
    }))
    wallet_totals = defaultdict(lambda: {
        "expired": 0, "invalid": 0, "started": 0, "validated": 0, "other": 0,
        "total_STAR": 0, "total_NIGHT": 0.0
    })
    overall = {"expired": 0, "invalid": 0, "started": 0, "validated": 0, "other": 0,
               "total_STAR": 0, "total_NIGHT": 0.0}

    # --- Aggregate data ---
    for wallet, content in data.items():
        addr_short = short_addr(wallet)
        for ch in content.get("challenge_queue", []):
            status = ch.get("status", "other")
            day = ch.get("campaignDay", 0)

            # skip invalid or future day (beyond available rate days)
            if day <= 0 or day > days_available:
                continue

            if status not in ["expired", "invalid", "started", "validated"]:
                status = "other"

            daily[day][addr_short][status] += 1
            wallet_totals[addr_short][status] += 1

            # reward calc only for validated
            if status == "validated":
                rate = rate_array[day - 1]
                daily[day][addr_short]["total_STAR"] += rate
                daily[day][addr_short]["total_NIGHT"] += rate / 1_000_000
                wallet_totals[addr_short]["total_STAR"] += rate
                wallet_totals[addr_short]["total_NIGHT"] += rate / 1_000_000

    # === Print per-day results ===
    for day in sorted(daily.keys()):
        print(f"=== 📅 Day {day} ===")
        header = f"{'WalletAddress':<26} {'expired':>8} {'invalid':>8} {'started':>8} {'validated':>10} {'other':>8} {'total_STAR':>13} {'total_NIGHT':>13}"
        print(header)
        print("-" * len(header))
        day_sum = {"expired": 0, "invalid": 0, "started": 0, "validated": 0, "other": 0, "total_STAR": 0, "total_NIGHT": 0.0}
        for addr, s in daily[day].items():
            print(f"{addr:<26} {s['expired']:>8} {s['invalid']:>8} {s['started']:>8} {s['validated']:>10} {s['other']:>8} {s['total_STAR']:>13,} {s['total_NIGHT']:>13.6f}")
            for k in day_sum:
                day_sum[k] += s[k]
        print(f"{'**DAY TOTAL**':<26} {day_sum['expired']:>8} {day_sum['invalid']:>8} {day_sum['started']:>8} {day_sum['validated']:>10} {day_sum['other']:>8} {day_sum['total_STAR']:>13,} {day_sum['total_NIGHT']:>13.6f}\n")
        for k in overall:
            overall[k] += day_sum[k]

    # === Wallet totals ===
    print("=== 💼 WALLET TOTALS (All Days Combined) ===")
    header = f"{'WalletAddress':<26} {'expired':>8} {'invalid':>8} {'started':>8} {'validated':>10} {'other':>8} {'total_STAR':>13} {'total_NIGHT':>13}"
    print(header)
    print("-" * len(header))
    for addr, s in wallet_totals.items():
        print(f"{addr:<26} {s['expired']:>8} {s['invalid']:>8} {s['started']:>8} {s['validated']:>10} {s['other']:>8} {s['total_STAR']:>13,} {s['total_NIGHT']:>13.6f}")

    # === Overall total ===
    print("\n=== 🌍 OVERALL TOTAL ===")
    header = f"{'expired':>8} {'invalid':>8} {'started':>8} {'validated':>10} {'other':>8} {'total_STAR':>13} {'total_NIGHT':>13}"
    print(header)
    print("-" * len(header))
    print(f"{overall['expired']:>8} {overall['invalid']:>8} {overall['started']:>8} {overall['validated']:>10} {overall['other']:>8} {overall['total_STAR']:>13,} {overall['total_NIGHT']:>13.6f}")

# === Entry ===
if __name__ == "__main__":
    main()
