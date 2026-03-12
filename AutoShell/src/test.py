# 测试脚本
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("1. 测试导入...")
try:
    from news import format_news
    from jobs import format_jobs
    from wechat import send_markdown_message
    print("2. 导入成功!")
except Exception as e:
    print(f"导入失败: {e}")
    sys.exit(1)

print("3. 测试新闻...")
try:
    news = format_news()
    print("新闻内容:")
    print(news[:200])
except Exception as e:
    print(f"获取新闻失败: {e}")

print("4. 测试招聘...")
try:
    jobs = format_jobs()
    print("招聘内容:")
    print(jobs[:200])
except Exception as e:
    print(f"获取招聘失败: {e}")

print("测试完成!")
