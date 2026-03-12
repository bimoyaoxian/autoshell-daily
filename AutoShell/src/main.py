import sys
import io
from datetime import datetime

# 解决Windows控制台编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from wechat import send_markdown_message
from news import format_news
from jobs import format_jobs


def generate_daily_report():
    """生成每日简报"""
    date_str = datetime.now().strftime("%Y年%m月%d日")
    
    report = f"📅 **{date_str} 每日简报**\n"
    report += f"> 更新时间: {datetime.now().strftime('%H:%M:%S')}\n\n"
    
    # 添加新闻
    news_content = format_news()
    report += news_content + "\n\n"
    
    # 添加招聘
    jobs_content = format_jobs()
    report += jobs_content + "\n\n"
    
    report += "---\n"
    report += "*每天8点自动推送 · AutoShell*"
    
    return report


def main():
    """主函数"""
    print("=" * 50)
    print("AutoShell 每日简报生成器")
    print("=" * 50)
    
    print("\n[1/3] 正在获取新闻资讯...")
    print("[2/3] 正在获取热门岗位...")
    print("[3/3] 正在整合数据并发送...")
    
    try:
        report = generate_daily_report()
        print("\n简报内容预览：")
        print(report[:500] + "..." if len(report) > 500 else report)
        
        # 发送到微信
        success = send_markdown_message(report)
        
        if success:
            print("\n✅ 每日简报发送成功！")
        else:
            print("\n❌ 每日简报发送失败，请检查配置")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ 程序执行出错: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
