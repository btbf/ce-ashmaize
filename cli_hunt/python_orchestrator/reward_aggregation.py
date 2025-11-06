import json
import requests
from collections import defaultdict

CHALLENGE_FILE = "challenges.json"
RATE_API_URL = "https://scavenger.prod.gd.midnighttge.io/work_to_star_rate"

def short_addr(addr: str) -> str:
    """ウォレットアドレスの中間を省略（先頭10 + '...' + 末尾10）"""
    return addr if len(addr) <= 25 else f"{addr[:10]}...{addr[-10:]}"

def format_row(cols, widths):
    """幅を指定して左寄せ整形"""
    return "  ".join(f"{str(c):<{w}}" for c, w in zip(cols, widths))

# === JSON読み込み ===
with open(CHALLENGE_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# === 報酬レート取得 ===
res = requests.get(RATE_API_URL, timeout=10)
res.raise_for_status()
rate_array = res.json()
print(f"✅ Retrieved reward rates for {len(rate_array)} campaign days.")
print("📊 Reward rates per day (1 NIGHT = 1,000,000 STAR):")
for i, rate in enumerate(rate_array, start=1):
    print(f"   • Day {i}: {rate:,} STAR ({rate/1_000_000:.6f} NIGHT)")

# === 集計用構造 ===
results = defaultdict(lambda: defaultdict(lambda: {"status_count": defaultdict(int), "total_star": 0}))
global_counts = defaultdict(int)
global_total_star = 0

# === データ集計 ===
for wallet, wallet_data in data.items():
    challenges = wallet_data.get("challenge_queue", [])
    for record in challenges:
        day = record.get("campaignDay")
        status = record.get("status", "unknown")
        if not isinstance(day, int):
            continue

        results[day][wallet]["status_count"][status] += 1
        if status == "validated":
            rate = rate_array[day - 1] if 0 <= day - 1 < len(rate_array) else 0
            results[day][wallet]["total_star"] += rate

# === 日別出力 ===
for day in range(1, len(rate_array) + 1):
    print(f"\n=== 📅 Day {day} ===")
    if day not in results:
        print("(No data for this day)")
        continue

    statuses = sorted({s for v in results[day].values() for s in v["status_count"].keys()})
    headers = ["WalletAddress"] + statuses + ["total_STAR", "total_NIGHT"]
    col_widths = [25] + [9] * len(statuses) + [12, 13]

    print(format_row(headers, col_widths))
    print("-" * sum(col_widths))

    total_counts = defaultdict(int)
    total_star_all = 0

    for wallet, data in results[day].items():
        row = [short_addr(wallet)]
        for s in statuses:
            c = data["status_count"].get(s, 0)
            row.append(str(c))
            total_counts[s] += c
            global_counts[s] += c
        total_star = data["total_star"]
        total_star_all += total_star
        global_total_star += total_star
        row.extend([str(total_star), f"{total_star / 1_000_000:.6f}"])
        print(format_row(row, col_widths))

    # 日合計
    total_row = ["**DAY TOTAL**"]
    for s in statuses:
        total_row.append(str(total_counts[s]))
    total_row.extend([str(total_star_all), f"{total_star_all / 1_000_000:.6f}"])
    print("-" * sum(col_widths))
    print(format_row(total_row, col_widths))

# === 全体合計 ===
print("\n=== 🌍 OVERALL TOTAL (All Days Combined) ===")
statuses = sorted(global_counts.keys())
print(format_row(["Status", "Count"], [15, 10]))
print("-" * 25)
for s in statuses:
    print(format_row([s, global_counts[s]], [15, 10]))
print(format_row(["validated_total_STAR", global_total_star], [25, 10]))
print(format_row(["validated_total_NIGHT", f"{global_total_star / 1_000_000:.6f}"], [25, 10]))
