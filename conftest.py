"""pytestの設定ファイル。src/ディレクトリをモジュール検索パスに追加する。"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
