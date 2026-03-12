import requests
from bs4 import BeautifulSoup


def get_sina_news():
    """获取新浪新闻热点"""
    news_list = []
    try:
        url = "https://top.news.sina.com.cn/ws/Rank_apiInner_0_0_1_1_50_0_1_1.html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            items = soup.select(".news_item a")[:6]
            for item in items:
                title = item.get_text(strip=True)
                if title and len(title) > 5:
                    news_list.append({"title": title})
    except Exception as e:
        print(f"获取新浪新闻失败: {e}")
    
    return news_list


def get_tencent_news():
    """获取腾讯新闻热点"""
    news_list = []
    try:
        url = "https://r.inews.qq.com/gw/event/hot_ranking"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "id" in data:
                for item in data["idlist"][0]["itemlist"][:6]:
                    news_list.append({
                        "title": item.get("title", ""),
                        "hotEvent": item.get("hotEvent", "")
                    })
    except Exception as e:
        print(f"获取腾讯新闻失败: {e}")
    
    return news_list


def get_ifeng_news():
    """获取凤凰网新闻"""
    news_list = []
    try:
        url = "https://news.ifeng.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            items = soup.select(".box_01 h2 a, .news_list h2 a, .focus_news h2 a")[:6]
            for item in items:
                title = item.get_text(strip=True)
                if title and len(title) > 5:
                    news_list.append({"title": title})
    except Exception as e:
        print(f"获取凤凰新闻失败: {e}")
    
    return news_list


def get_wallstreetcn_news():
    """获取华尔街见闻新闻"""
    news_list = []
    try:
        url = "https://api.jin10.com/get_channel_list_all"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://wallstreetcn.com/"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                for item in data["data"][:6]:
                    news_list.append({
                        "title": item.get("title", ""),
                        "time": item.get("time", "")
                    })
    except Exception as e:
        print(f"获取华尔街见闻新闻失败: {e}")
    
    return news_list


def get_36kr_news():
    """获取36氪科技新闻"""
    news_list = []
    try:
        url = "https://36kr.com/newsflashes"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            articles = soup.select(".article-item a")[:6]
            for article in articles:
                title = article.get_text(strip=True)
                if title:
                    news_list.append({"title": title})
    except Exception as e:
        print(f"获取36氪新闻失败: {e}")
    
    return news_list


def format_news():
    """整合所有新闻来源"""
    news_text = "📰 **今日新闻速览**\n\n"
    
    # 尝试腾讯新闻
    tx_news = get_tencent_news()
    if tx_news:
        news_text += "**【腾讯新闻热点】**\n"
        for i, item in enumerate(tx_news, 1):
            title = item.get("title", "")
            if title:
                news_text += f"{i}. {title}\n"
        news_text += "\n"
    
    # 尝试新浪新闻
    if not tx_news:
        sina_news = get_sina_news()
        if sina_news:
            news_text += "**【新浪新闻热点】**\n"
            for i, item in enumerate(sina_news, 1):
                title = item.get("title", "")
                if title:
                    news_text += f"{i}. {title}\n"
            news_text += "\n"
    
    # 凤凰网新闻
    ifeng_news = get_ifeng_news()
    if ifeng_news:
        news_text += "**【凤凰网要闻】**\n"
        for i, item in enumerate(ifeng_news, 1):
            title = item.get("title", "")
            if title:
                news_text += f"{i}. {title}\n"
        news_text += "\n"
    
    # 财经新闻
    ws_news = get_wallstreetcn_news()
    if ws_news:
        news_text += "**【华尔街见闻 - 财经】**\n"
        for i, item in enumerate(ws_news, 1):
            title = item.get("title", "")
            if title:
                news_text += f"{i}. {title}\n"
    
    # 科技新闻
    kr_news = get_36kr_news()
    if kr_news:
        news_text += "\n**【36氪 - 科技前沿】**\n"
        for i, item in enumerate(kr_news, 1):
            title = item.get("title", "")
            if title:
                news_text += f"{i}. {title}\n"
    
    return news_text if news_text != "📰 **今日新闻速览**\n\n" else "📰 暂无新闻数据"


if __name__ == "__main__":
    print(format_news())
