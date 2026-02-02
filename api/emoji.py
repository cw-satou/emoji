from http.server import BaseHTTPRequestHandler
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ここに候補の文字を指定
        candidates = [
            "🅰️", "🅱️", "🅾️", "⛎", 
            "♈️", "♉️", "♊️", "♋️", 
            "♌️", "♍️", "♎️", "♏️", 
            "♐️", "♑️", "♒️", "♓️"
        ]
        
        # ランダムに1つ選ぶ
        chosen_char = random.choice(candidates)
        
        # レスポンスの設定（成功:200, タイプ:テキスト）
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        # 文字を書き出す
        self.wfile.write(chosen_char.encode('utf-8'))
        return