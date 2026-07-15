import requests
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://dench.mklab.osakac.ac.jp/script-pg/"
cache_file = "last_script_pg.txt"

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    current_content = response.text.strip()

except requests.exceptions.RequestException as e:
    print(f"通信エラー: {e}")
    exit(1)

if not os.path.exists(cache_file):
    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(current_content)
    print("初回取得完了（差分なし）")

else:
    with open(cache_file, "r", encoding="utf-8") as f:
        previous_content = f.read().strip()

    if current_content != previous_content:
        print("更新が検出されました！")
        print("前回:", previous_content)
        print("今回:", current_content)

        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(current_content)
    else:
        print("変更はありません。")
# test2