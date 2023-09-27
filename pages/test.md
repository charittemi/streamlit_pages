---
marp: false
footer: "スライド作成テスト"
theme: mytheme
paginate: true
size: 16:9
---

<!-- _paginate: false -->
![bg right](./imgs/stream.jpg)
# Marpでスライド作成テスト(作業中)
## レイアウトを使いこなしたい
### 目次

1. 標準レイアウト
2. ２カラム表示用サンプルスライド
3. ３カラム表示用サンプルスライド
4. 質問と回答
<br/>

---

# 標準レイアウト: アマゴとヤマメ
## 生息域の違い
**アマゴ**
「太平洋に注ぐ西日本の河川」
**ヤマメ**
「太平洋に注ぐ東日本の河川」と「日本海側に注ぐ河川」
## 見た目の違い
よく似ているがアマゴには赤い斑点が散りばめられている
'![](./imgs/amago.jpg)'

---
<style scoped>
.split-v>* {
  width: 100%;
} 
.split-v {
  align-items: flex-start;
} 
</style>

# ２カラム表示用サンプルスライド
<div class="split-v">
<div>

## Left Column
左右のカラムを均一に配置するために対象ページの冒頭にCSSで定義したスタイルを指定する

```
<style scoped>
.split-v>* {
  width: 100%;
} 
.split-v {
  align-items: flex-start;
} 
</style>
```

</div>
<div>

## Right Column
各カラムごとにdivで囲い込む

```
<div class="split-v">
テキスト
</div>
```

<div class="tweet">
あまり多くHTMLで指定すると「テキストの使い回ししやすさ」というMarkdown記法本来の良さが失われてしまうので注意
</div>
</div>

---

<style scoped>
.split-v>* {
  width: 100%
} 
.split-v {
  align-items: flex-start;
} 
</style>

# ３カラム表示用サンプルスライド
<div class="split-v">
<div>

## Left Column
divを3ブロックにすれば良いだけ

</div>
<div>

## Middle Column
テキスト

</div>

<div>

## Right Column

カラムレイアウトができると画像配置が捗って嬉しい
'![](./imgs/amago.jpg)'
</div>

---

<style scoped>
h2::before {
  content: "Q. "
}
section > *:not(h1):not(header):not(footer) {
  font-size: 20px;
}
h3::before {
  content: "A. "
}
</style>

# 質問と回答

## このスライドをどうやってつくったの？

### Marpライブラリを使って作成しました。

基本的にはMarkdown記法で作成した簡単な構造のテキストをMarpでpptxスライドとして出力するだけ。ただし、レイアウトを整えるためにCSSやHTMLも使用。
<br><br>

## 参考にしたサイトは？

### 「Marpでスライド作ってみよう」(https://tech.synapse.jp/entry/2022/04/15/110000)を参考にしています。

一度、基本的なテンプレートを用意しておけば、あとはページごとに好きなレイアウトを選んでコンテンツを当てはめていくだけで統一感のあるスライドができそう。
<br><br>

---


