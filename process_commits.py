import subprocess
import datetime
import json


def get_git_commits():
    try:
        # 执行 git log 命令获取提交时间戳，当前目录即为仓库根目录
        result = subprocess.run(['git', 'log', '--pretty=format:"%at"'],
                                capture_output=True, text=True)
        if result.returncode == 0:
            timestamps = [int(line.strip().strip('"')) for line in result.stdout.splitlines()]
            return timestamps
        else:
            print(f"Error getting git commits: {result.stderr}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def process_commits(timestamps):
    # 统计每天的提交次数
    commit_counts = {}
    for timestamp in timestamps:
        date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        if date in commit_counts:
            commit_counts[date] += 1
        else:
            commit_counts[date] = 1

    # 生成 JSON 数据
    heatmap_data = []
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.datetime.now()
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        count = commit_counts.get(date_str, 0)
        heatmap_data.append({
            'date': date_str,
            'count': count
        })
        current_date += datetime.timedelta(days=1)

    return heatmap_data


if __name__ == "__main__":
    timestamps = get_git_commits()
    if timestamps:
        heatmap_data = process_commits(timestamps)
        # 将处理后的数据保存为 JSON 文件
        with open('heatmap_data.json', 'w') as f:
            json.dump(heatmap_data, f)
        print("Heatmap data generated successfully.")