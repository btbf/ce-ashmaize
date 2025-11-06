# ⚙️ Midnight Scavenger CLI Miner – Reward Aggregation Tool

## 🔧 Improvements & Contribution Notes  
**English / 日本語併記版**

---

### 🇬🇧 English

This repository contains **community improvements and helper scripts** related to the  
[Midnight Scavenger CLI Miner](https://github.com/mpizenberg/ce-ashmaize).  
All credits for the original implementation go to the author of the upstream repository:  
👉 **[`mpizenberg/ce-ashmaize`](https://github.com/mpizenberg/ce-ashmaize)**  

> ⚠️ **Note:** Always use the original repository for actual mining.  
> This fork only provides optional analysis and reporting tools, not a replacement for the miner itself.

---

### 🧩 How to Use

You can download and run **only the analysis script** without cloning the whole repo.

> 💾 Please save the downloaded file inside your local miner directory:  
> `ce-ashmaize/cli_hunt/python_orchestrator/`

```bash
# Download the script directly
curl -O https://raw.githubusercontent.com/btbf/ce-ashmaize/refs/heads/reward-aggregation/cli_hunt/python_orchestrator/reward_aggregation.py

# Move it into your Midnight miner folder
mv challenges_aggregation.py ce-ashmaize/cli_hunt/python_orchestrator/

# Place your challenges.json in the same directory and run
cd ce-ashmaize/cli_hunt/python_orchestrator/
python3 challenges_aggregation.py
````

If you see an error such as:

```bash
ModuleNotFoundError: No module named 'requests'
```

please install the required package manually:

```bash
sudo apt install -y python3-pip   # if pip is not installed
pip3 install requests
```

---

### 💡 What the Script Does

* Automatically fetches the latest reward rate data from the API
* Aggregates and summarizes validated challenges by wallet and campaign day
* Displays total STAR and NIGHT rewards in a formatted CLI table

For **actual mining**, please use the official repository:
👉 [https://github.com/mpizenberg/ce-ashmaize](https://github.com/mpizenberg/ce-ashmaize)

---

### 🪄 Example Output

```text
✅ Retrieved reward rates for 6 campaign days.
📊 Reward rates per day (1 NIGHT = 1,000,000 STAR):
   • Day 1: 3,724,076 STAR (3.724076 NIGHT)
   • Day 2: 2,133,655 STAR (2.133655 NIGHT)
   • Day 3: 2,396,362 STAR (2.396362 NIGHT)
   • Day 4: 3,521,664 STAR (3.521664 NIGHT)
   • Day 5: 2,233,377 STAR (2.233377 NIGHT)
   • Day 6: 1,851,267 STAR (1.851267 NIGHT)

=== 📅 Day 5 ===
WalletAddress              expired   invalid   started   validated   total_STAR   total_NIGHT
--------------------------------------------------------------------------------------------
addr1q8rkn...zytsstwecc    1         0         1         13          24066471     24.066471
addr1q9h08...s2dq9uw7g2    0         0         0         19          35174073     35.174073
```

---

### 🙌 Contribution Policy

This repository follows the upstream author’s open approach:
**Independent, community-driven improvements are welcome.**

If you find **a bug**, have **a feature request**, or want to **suggest improvements**,
please open an **[Issue](../../issues)** on GitHub.

You can also:

* Fork this repository and modify the Python script, or
* Share your enhancements via Discussions or Pull Requests

> Your feedback helps improve the analysis tool for everyone.

---

### 🇯🇵 日本語訳

このリポジトリは、
[Midnight Scavenger CLI Miner（mpizenberg/ce-ashmaize）](https://github.com/mpizenberg/ce-ashmaize)
に関連する **集計・分析用スクリプト** を提供するコミュニティフォークです。

オリジナル実装の著作権およびクレジットは
👉 **[`mpizenberg/ce-ashmaize`](https://github.com/mpizenberg/ce-ashmaize)** に帰属します。

> ⚠️ **注意:** 実際のマイニングや報酬獲得には必ず公式リポジトリを使用してください。
> このフォークは、**解析・レポート用途の補助スクリプト**として提供されています。

---

### 🧩 使用方法

`git clone` は不要です。
以下のコマンドで `challenges_aggregation.py` を直接ダウンロードして実行できます。

> 💾 スクリプトは次の場所に保存してください：
> `ce-ashmaize/cli_hunt/python_orchestrator/`

```bash
# スクリプトを直接ダウンロード
curl -O https://raw.githubusercontent.com/btbf/ce-ashmaize/refs/heads/reward-aggregation/cli_hunt/python_orchestrator/reward_aggregation.py

# Midnight miner のフォルダに移動
mv challenges_aggregation.py ce-ashmaize/cli_hunt/python_orchestrator/

# 同じディレクトリに challenges.json を置いて実行
cd ce-ashmaize/cli_hunt/python_orchestrator/
python3 challenges_aggregation.py
```

もし次のようなエラーが出た場合：

```bash
ModuleNotFoundError: No module named 'requests'
```

以下のコマンドで `requests` をインストールしてください：

```bash
sudo apt install -y python3-pip   # pipが未インストールの場合
pip3 install requests
```

---

### 💡 スクリプトの機能

* 報酬レートAPIから最新データを自動取得
* ウォレット単位・日ごとの `validated` チャレンジを集計
* STARおよびNIGHT報酬を整列テーブルで出力

実際のマイニングは必ず公式リポジトリを使用してください：
👉 [https://github.com/mpizenberg/ce-ashmaize](https://github.com/mpizenberg/ce-ashmaize)

---

### 🪄 出力例

```text
✅ Retrieved reward rates for 6 campaign days.
📊 Reward rates per day (1 NIGHT = 1,000,000 STAR):
   • Day 1: 3,724,076 STAR (3.724076 NIGHT)
   • Day 2: 2,133,655 STAR (2.133655 NIGHT)
   • Day 3: 2,396,362 STAR (2.396362 NIGHT)
   • Day 4: 3,521,664 STAR (3.521664 NIGHT)
   • Day 5: 2,233,377 STAR (2.233377 NIGHT)
   • Day 6: 1,851,267 STAR (1.851267 NIGHT)
```

---

### 🙌 貢献について

このフォークでは、オリジナル作者の「自分のフォークで改良する」という方針を尊重しつつ、
オープンで独立したコミュニティ貢献を歓迎しています。

もし **バグを見つけた場合**、**機能追加の要望**、または **改善提案** がある場合は、
ぜひ GitHub の **[Issue](../../issues)** を作成してください。

また、次のような貢献も歓迎します：

* このリポジトリをフォークしてスクリプトを改良
* Issue や Discussion で改善案や成果を共有

> あなたのフィードバックが、より良いツールづくりにつながります。
