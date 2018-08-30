from random import choice, sample

all_attributes = [
  ('姓', ['田中', '佐藤', '鈴木']),
  ('名', ['太郎', '花子', '次郎', '葵']),
  ('性別', ['男', '女']),
  ('年齢', [str(i) for i in range(9, 50)]),
  ('職業', ['無職', '学生', '会社員', '自営業']),
  ('所属', ['なし', 'A校', 'B社']),
  ('趣味', ['なし', '読書', 'ゲーム', 'アウトドア', 'スポーツ観戦']),
  ('居住地', ['東京', '大阪', '京都', '福岡', '広島']),
]

def generate_random(num_attr=5):
  return {a[0]: choice(a[1]) for a in sample(all_attributes, num_attr)}