#! /bin/bash
getJsonData(){
  result=$(grep $1 ../sauryInfo.js)
  result=${result//const $1=/}
  result=${result//\"/}
  echo $result
}

userName=$(getJsonData "userName")
password=$(getJsonData "password")

curl -c cookie.txt -d "usernameOrEmailAddress=$userName" -d "password=$password" -X post "https://host.ailinkedlaw.com/Account/Login"
curl -b cookie.txt "https://host.ailinkedlaw.com/api/services/web/language/exportLanguagesToXml?languages%5B0%5D=de&languages%5B1%5D=en&languages%5B2%5D=es&languages%5B3%5D=fr&languages%5B4%5D=ru&languages%5B5%5D=ar&languages%5B6%5D=hi&languages%5B7%5D=zh-Hant&languages%5B8%5D=zh-CN&languages%5B9%5D=ja-JP&languages%5B10%5D=ko-KR&sources%5B0%5D=System&sources%5B1%5D=General&sources%5B2%5D=App&sources%5B3%5D=Web" --output ~/Downloads/localization.zip

mkdir ~/Documents/localization
cp ~/Downloads/localization.zip ~/Documents/localization
unzip ~/Documents/localization/localization.zip -d  ~/Documents/localization/
rm ~/Downloads/localization.zip
./xmltrans.py
rm -r ~/Documents/localization
rm ~/Documents/language.js
rm ~/Documents/language_zh.js
cp ~/Documents/language*.js ~/CordovaProjects/Lzh_MiniProgram/src/language/
rm ~/Documents/language*.js
