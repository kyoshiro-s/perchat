from random import choice, sample

all_attr_and_vals = [
  ('姓', ['佐藤', '鈴木', '高橋', '田中', '伊藤', '渡辺', '山本', '中村', '小林', '加藤',], 0),
  ('名', ['悠真', '翔', '歩夢', 'さくら', '陽菜', '莉子', #2010
          '翔太', '大輝', '優斗', '優花', '美咲', '葵', #2000
          '健太', '拓也', '翼', '愛', '萌', '愛美', #1994
          '大輔', '誠', '直樹', '麻衣', '恵', '裕子', #1984
          '剛', '健一', '涼', '陽子', '真由美', '久美子', #1974
          ], 1),
  ('性別', ['男', '女'], 2),
  ('年齢', [str(i) for i in range(9, 50)], 3),
  ('職業', ['無職', '学生', '会社員', '自営業'], 4),
  ('所属', ['なし', 'A校', 'B社'], 5),
  ('趣味', ['なし', '読書', 'ゲーム', 'アウトドア', 'スポーツ観戦'], 6),
  ('居住地', ['東京', '大阪', '京都', '福岡', '広島'], 7),
]

def get_all():
  return all_attr_and_vals

def generate_random(num_attr=5):
  chosen = sorted(sample(all_attr_and_vals, num_attr), key=lambda x:x[2])
  # ret = {a[0]: choice(a[1]) for a in sample(all_attr_and_vals, num_attr)}
  ret = [(a[0], choice(a[1])) for a in chosen]
  # print(ret)
  return ret

def get_attr_list():
  return [p[0] for p in all_attr_and_vals]