PyMinerStat
===========
PyMinerStats is a Python script to generate charts with your mining rewards from bitcoin.cz account.

The script is based on [SQLITE3](http://www.sqlite.org/) and [pygal](http://pygal.org/).


# Configuration #

## Step 1. ##

execute those two commands as root:
```
#!bash

mkdir /var/www/mining
chmod a+w /var/www/mining

```


## Step 2. ##
You will find your API key to [bitcoin.cz here](https://mining.bitcoin.cz/accounts/token-manage/).
In the script set two variable:
```
#!python
api="YOUR API KEY"

path="/var/www/mining"

```


## Step 3. ##

Copy index.html and css to your folder:

```
#!bash

cp src/index.html /var/www/mining
cp -r src/css /var/www/mining
```



PRO TIP:
add this script to your crontab
```
#!bash
0 0,4,8,12,16,20 * * * root python /var/www/miner/PiMinerStats.py
```
