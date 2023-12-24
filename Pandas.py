import pandas as pd

# ユーザーデータをPandas DataFrameとして読み込む
userData = [
    {'name': 'John Doe', 'age': 25, 'hobby': 'Hiking', 'comment': 'Nice to meet you!', 'photo': 'john.jpg', 'latitude': 35.6895, 'longitude': 139.6917},
    # 他のユーザー情報も追加可能
]

user_df = pd.DataFrame(userData)

# HTMLのテンプレートを読み込む
with open(r'index.html', 'r') as template_file:
    html_template = template_file.read()

# ユーザーデータをHTMLに埋め込む
html_content = html_template.format(**user_df.iloc[0])

# HTMLファイルに保存
with open('output.html', 'w') as f:
    f.write(html_content)
