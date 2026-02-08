ファイル自動操作 - 完全マニュアル

## 目次

1. [環境作成手順](#環境作成手順)
2. [実際の操作手順](#実際の操作手順)
3. [バッチプログラム](#バッチプログラム)
4. [Seleniumプログラム](#seleniumプログラム)
5. [トラブルシューティング](#トラブルシューティング)

---

## 環境作成手順

### 1. Python と Selenium の準備

#### 1-1. Python をインストール
Windows で Python 3.x をインストール
インストール時に「Add Python to PATH」にチェックを入れる

#### 1-2. Selenium をインストール
コマンドプロンプトで実行：
bash
pip install selenium

### 2. Chrome と ChromeDriver の準備
#### 2-1. Chrome のインストール・更新
Google Chrome を最新版にアップデート

#### 2-2. Chrome のバージョン確認
Chrome右上メニュー → ヘルプ → Chrome について

バージョン番号をメモしておく

#### 2-3. ChromeDriver をダウンロード
ChromeDriver 公式ページで、Chrome バージョンに対応する Windows 用をダウンロード

zip を展開し、C:\webdrivers\chromedriver.exe など任意の場所に配置

### 3. ユーザーデータディレクトリの準備
#### 3-1. フォルダを作成
エクスプローラで C:\ChromeMulti フォルダを新規作成

#### 3-2. 作業フォルダを作成
C:\PocochaAutomation のような作業フォルダを作成

この中に後述のバッチファイルとPythonスクリプトを保存する

### 4. プロファイルの初期設定
#### 4-1. バッチファイルを実行
後述の profiles_setup.bat を作成し、ダブルクリックして実行

12個の Chrome ウィンドウが起動する

#### 4-2. 各プロファイルで Google ログイン
起動した 12個の Chrome それぞれで Google アカウントにログイン

同じアカウントでも、別々のアカウントでもOK

#### 4-3. 各プロファイルで Pococha ログイン
各 Chrome で https://pococha.com/diamonds にアクセス

「Googleでログイン」を選択して Pococha にログイン

ダイヤページが正常に表示されることを確認

#### 4-4. タレントAPIテスター拡張の確認
chrome://extensions/ を開く

タレントAPIテスター拡張が「有効」になっていることを確認

1つのプロファイルで chrome-extension://aejoelaoggembcahagimdiliamlcdmfm/index.html#scenarios を開いて動作確認