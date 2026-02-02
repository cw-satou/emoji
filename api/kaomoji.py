from http.server import BaseHTTPRequestHandler
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 顔文字のリスト
        candidates = [
            "՞⸝⸝> ̫ <⸝⸝՞♡",
            "(◜~◝⸝⸝ )",
            "⸝⸝ᵒ̴̶̷᷄ᴗᵒ̴̶̷᷅⸝⸝",
            "(՞ ᵒ̴̶̷̤-ᵒ̴̶̷̤՞)",
            "ᐡ⸝⸝𖦹 ·̫ 𖦹⸝⸝ᐡ",
            "(⸝⸝ᐡ. ̫ .ᐡ⸝⸝)",
            "(ᐡ ̳ᴗ ̫ ᴗ ̳ᐡ)",
            "₍ᐢ⸝⸝•ω•⸝⸝ᐢ₎",
            "(ᐡ ̥ × ̫ × ̥ᐡ)",
            "(◍´͈ ᵕ `͈ ◍)",
            "(///з///)♡",
            "(〃ω〃)"
        ]
        
        # ランダムに1つ選ぶ
        chosen_char = random.choice(candidates)
        
        # レスポンス設定
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # 結果を書き出す
        self.wfile.write(chosen_char.encode('utf-8'))
        return