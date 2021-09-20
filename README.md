# Homework 2
Nothing to see here again... Now optimized. It is a python script that downloads lots of hentai images based on random ids from [nhentai](https://nhentai.net).

With `nDownloder.py`, it writes one line per request. Use `nDownloader_clean.py` for a much cleaner look.

#

⚠️ If you download a lot of images, you might get banned! I am not responsible at all. ⚠️

Although the download rate will be slower, the `useTorProxy` option is recomended.

#

### Installing

``` shell
git clone https://github.com/r4v10l1/homework2/
cd homework2
python -m pip install -r requirements.txt
python nDownloader_clean.py
```

### Configuration

* You can edit the `debugPrint` variable to print some extra stuff.
* You can edit the `useTorProxy` variable to enable the use of a proxy during the requests. If you enable this, you will need to have tor open and the port it will use will be **9150**.
* You can edit the `sessionMode` variable to store the cookies.

### Logs

The script writes the following information into a log (`nDownloaded.log`):
* When the user starts the program.
* When the user stops the program.
* When the script detects an error.
