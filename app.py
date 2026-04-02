#!/usr/bin/env python3
"""纳斯达克100 ETF 数据网站 - Flask后端"""
import json
import os
from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "nasdaq_etf_daily.json")


def load_data():
    """读取最新ETF数据"""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    """主页 - 渲染数据表格"""
    data = load_data()
    updated_at = data[0].get("日期", "未知") if data else "未知"
    return render_template("index.html", data=data, updated_at=updated_at)


@app.route("/api/data")
def api_data():
    """JSON API接口"""
    return jsonify(load_data())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
