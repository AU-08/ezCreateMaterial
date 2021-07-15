インストールの方法
==========================

1. Download ZIPからフォルダをダウンロードします。

2. ZIPファイルを解凍し以下の通りに配置します
* pythonファイル  
`ドキュメント > maya > 使用するmayaのバージョン > scripts`  

* pngファイル (シェルフに登録する場合使用して下さい)  
`ドキュメント > maya > 使用するmayaのバージョン > prefs > icons`

3. Mayaを再起動します。

4. 以下のコマンドを実行します。  
```py
import ezCreateMaterial
ezCreateMaterial.run()
```



使用方法
==========================

1. 使用したいテクスチャマップのチェックボックスにチェックを入れます。

2. "Select"ボタンをクリックし、画像ファイルを選択します。  
＊パスを変更したい場合は、再度"Select"ボタンをクリックするか、テキストフィールドのパスを書き換えてください。

3. "Create Material"をクリックしてマテリアルを作成します。
