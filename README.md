# UnusedBoneRemover
![dde08b6364830ae812c70db81378c5f9 (online-video-cutter com)](https://github.com/user-attachments/assets/17f94044-a95b-4226-a98f-7b3c0fc4cf65)

## 概要
blenderで、選択メッシュが利用していないボーンをすべて削除するアドオンです。  
VRChat用衣装の作成時に、不必要なボーンを削除するのがめんどうだったため制作いたしました。  

## 動作環境
blender4.2で動作確認済みです。  

## 利用方法
1. メッシュを選択  
2. Armatureを選択  
3. Remove unused boneボタンを押す

## 利用上の注意
ウェイトが乗っていないボーンをすべて削除する仕様のため、endボーンなどはすべて削除されます。  
ご注意ください。

## 仕様詳細
内部的には、選択されているメッシュの頂点グループに同名の頂点グループがないボーンをすべて削除することで実現しています。    
そのため、不必要な頂点グループが含まれているモデルでは正常に動作しません。  

読み込んだ直後のfbxファイルだと問題なく動作すると思われます。  

## 参考
[ymg_bone_selector](https://github.com/naoya-horai/ymg_bone_selector)を参考にさせていただきました。  

## ライセンス
GPL-3.0 Licence
