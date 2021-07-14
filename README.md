インストールの方法
==========================

1. Download ZIPからフォルダをダウンロードします。

2. ZIPファイルを解凍し、
* pythonファイル  
`ドキュメント > maya > 使用するmayaのバージョン > scripts`  

* pngファイル (シェルフに登録する場合使用して下さい)  
`ドキュメント > maya > 使用するmayaのバージョン > prefs > icons` へ入れます。

3. Mayaを再起動します。

4. 以下のコマンドを実行します。  
        import ezCreateMaterial
        reload(ezCreateMaterial)
        ezCreateMaterial.run()
