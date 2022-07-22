# ip-management-system

## What
- 研究室で使用するIPアドレスを管理するシステム

## Will
- コンテナ技術を使うことでサーバ移行を簡単にできるようにする
- なるべくドキュメントを残し、誰でも改良できるようにする
- 使いやすさを優先し、今よりも使いやすいシステムを目指す(JavaScriptを使って画面遷移を減らす)
- ドメインを設定するとDNSの設定を変更する機能を追加する

## Now
- 1ヶ月くらいは3年生向けPython演習の見本置き場として使う(ログイン処理等共通の機能があるため)

## 使い方(見本プログラム)
- 実行にはDockerおよびdocker-composeが必要です
- リポジトリからクローン
  -  `git clone https://github.com/munvei/ip-management-system.git`
- 本ディレクトリへ移動
  - `cd ip-management-system`
- ビルド&バックグラウンドで実行
  -  `docker-compose up --build -d `
- 停止&削除
  -  `docker-compose down`
- バックグラウンドで実行した場合のログは以下で確認できます
  -  `docker-compose logs`
- Webページ
  - [localhost](http://localhost) 
