#! /bin/bash
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
