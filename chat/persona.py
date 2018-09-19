from random import choice, sample

all_attr_and_vals = [
  ('姓', ['田中', '佐藤', '鈴木']),
  ('名', ['太郎', '花子', '次郎', '葵']),
  ('性別', ['男', '女']),
  ('年齢', [str(i) for i in range(9, 50)]),
  ('職業', ['無職', '学生', '会社員', '自営業']),
  ('所属', ['なし', 'A校', 'B社']),
  ('趣味', ['なし', '読書', 'ゲーム', 'アウトドア', 'スポーツ観戦']),
  ('居住地', ['東京', '大阪', '京都', '福岡', '広島']),
]

def get_all():
  return all_attr_and_vals

def generate_random(num_attr=5):
  ret = {a[0]: choice(a[1]) for a in sample(all_attr_and_vals, num_attr)}
  print(ret)
  return ret

def get_attr_list():
  return [p[0] for p in all_attr_and_vals]