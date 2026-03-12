import requests
from bs4 import BeautifulSoup


def get_boss_jobs(keyword="Python", city="北京"):
    """获取Boss直聘热门岗位"""
    jobs_list = []
    try:
        url = f"https://www.zhipin.com/web/geek/job-detail?jobCity={city}&kw={keyword}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.zhipin.com/"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            # 尝试多种选择器
            job_cards = soup.select(".job-card")[:5]
            for job in job_cards:
                title = job.select_one(".job-title")
                salary = job.select_one(".salary")
                company = job.select_one(".company-name")
                
                job_info = []
                if title:
                    job_info.append(title.get_text(strip=True))
                if salary:
                    job_info.append(salary.get_text(strip=True))
                if company:
                    job_info.append(company.get_text(strip=True))
                
                if job_info:
                    jobs_list.append(" | ".join(job_info))
    except Exception as e:
        print(f"获取Boss直聘岗位失败: {e}")
    
    return jobs_list


def get_lagou_jobs(keyword="Python"):
    """获取拉勾网热门岗位"""
    jobs_list = []
    try:
        url = "https://www.lagou.com/jobs/list_Python"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://www.lagou.com/"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            job_items = soup.select(".con_list_item")[:5]
            for job in job_items:
                position = job.select_one(".position-link")
                salary = job.select_one(".money")
                
                job_info = []
                if position:
                    job_info.append(position.get_text(strip=True))
                if salary:
                    job_info.append(salary.get_text(strip=True))
                
                if job_info:
                    jobs_list.append(" | ".join(job_info))
    except Exception as e:
        print(f"获取拉勾网岗位失败: {e}")
    
    return jobs_list


def get_qiancheng_jobs(keyword="Python"):
    """获取前程无忧热门岗位"""
    jobs_list = []
    try:
        url = f"https://search.51job.com/list/000000,000000,0000,00,9,99,{keyword},2,1.html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            job_items = soup.select(".el")[:5]
            for item in job_items:
                title = item.select_one(".t")
                salary = item.select_one(".salary")
                
                job_info = []
                if title:
                    job_info.append(title.get_text(strip=True))
                if salary:
                    job_info.append(salary.get_text(strip=True))
                
                if job_info and len(job_info[0]) > 5:
                    jobs_list.append(" | ".join(job_info))
    except Exception as e:
        print(f"获取前程无忧岗位失败: {e}")
    
    return jobs_list


def format_jobs():
    """整合所有招聘岗位信息"""
    jobs_text = "💼 **热门岗位推荐**\n\n"
    
    # Python开发岗位
    jobs_text += "**【Python开发工程师】**\n"
    python_jobs = get_qiancheng_jobs("Python")
    if python_jobs:
        for i, job in enumerate(python_jobs, 1):
            jobs_text += f"{i}. {job}\n"
    else:
        jobs_text += "暂无数据\n"
    
    # 前端开发岗位
    jobs_text += "\n**【前端开发工程师】**\n"
    frontend_jobs = get_qiancheng_jobs("前端")
    if frontend_jobs:
        for i, job in enumerate(frontend_jobs, 1):
            jobs_text += f"{i}. {job}\n"
    else:
        jobs_text += "暂无数据\n"
    
    # 算法工程师
    jobs_text += "\n**【算法工程师】**\n"
    algo_jobs = get_qiancheng_jobs("算法工程师")
    if algo_jobs:
        for i, job in enumerate(algo_jobs, 1):
            jobs_text += f"{i}. {job}\n"
    else:
        jobs_text += "暂无数据\n"
    
    jobs_text += "\n*数据来源：前程无忧51Job*"
    
    return jobs_text


if __name__ == "__main__":
    print(format_jobs())
