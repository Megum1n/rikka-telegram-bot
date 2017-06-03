![Rikka Bot Logo](http://madi.so/rikka-bot.png)

*My personal multipurpose chat bot with completely random features*  
*Can be found at [@Rikka_Bot](https://telegram.me/Rikka_Bot)*

![Python ver](http://img.shields.io/badge/Python-3.6-yellow.svg) [![Build Status](https://scrutinizer-ci.com/g/MadiNyan/rikka-telegram-bot/badges/build.png?b=master)](https://scrutinizer-ci.com/g/MadiNyan/rikka-telegram-bot/build-status/master) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/MadiNyan/rikka-telegram-bot/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/MadiNyan/rikka-telegram-bot/?branch=master) [![Code Climate](https://codeclimate.com/github/MadiNyan/rikka-telegram-bot/badges/gpa.svg)](https://codeclimate.com/github/MadiNyan/rikka-telegram-bot) [![Contact Me](https://img.shields.io/badge/Contact-Me-blue.svg)](https://telegram.me/Madi_Nyan) 

----------

## Requirements:
+ Python 3.5+
+ ImageMagick

### Libraries:
+ [python-telegram-bot](https://github.com/python-telegram-bot)
+ [py-ms-cognitive](https://github.com/tristantao/py-ms-cognitive)
+ [legofy](https://github.com/JuanPotato/Legofy)
+ [PyBooru](https://github.com/LuqueDaniel/pybooru)
+ psutil
+ uptime

## How to
Run `update_deps.bat` to automatically install `requirements.txt` libraries
Configure your token, api keys and paths in config.yml (without any quotations), and don't forget the font
```
    keys:
        telegram_token: 123455
        bing_api_key: 123456

    path:
        gifs: examples/gifs/
        memes: examples/memes/
        meme_font: resources/font_name.ttf
        lego: examples/lego/
        nya: examples/nya/
        kek: examples/kek/
        instagram: examples/instagram/
        anime: examples/
        liquid: examples/liquid
```

## Available functions:
+ /a [tag] - get pic from yande.re
+ /gif - get random gif, "/gif help" to see folders
+ /glitch - glitch an image
+ /img, /vid, /news [query] - Bing search for random result
+ /instagram or /ig - add filter to an image
+ /kek [-l, -r, -t, -b] - mirror one side of an image to another
+ /leet - convert text to 1337 5P34K
+ /lego [from 1 to 100] - legofy image
+ /liq [from 1 to 100] - liquid rescale image
+ /meme [top text] @ [bottom text] - make a meme from image
+ /nya - get random asian girl pic
+ /roll - fortune tell
+ /roll [1] or [2] - choose one option randomly
+ /roll [X-Y] - returns random number between X and Y
+ /say - TTS
+ /start - start a bot or view welcome message
+ /status - show server cpu, ram, hdd load and uptime
+ /toribash [username] - show Toribash stats
