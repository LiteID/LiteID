---
title: Repositories
menu: | 
 <a href="#liteid-android" style="margin-bottom:1px">LiteID-Android</a><br>
 <a href="#liteid-contract-tools" style="margin-bottom:1px">LiteID-Contract-Tools</a><br>
 <a href="#liteid-contract" style="margin-bottom:1px">LiteID-Contract</a><br>
 <a href="#liteid-simapp" style="margin-bottom:1px">LiteID-SimApp</a><br>
---

# Repositories
---
Here is an index of our repositories, and what is included in them:
<br><br>

### [LiteID-Android](https://github.com/LiteID/LiteID-Android)

Our cross platform Xamarin App, currently targeting Android 2.3+ including:

 - Gingerbread
 - Honeycomb
 - Ice Cream Sandwich
 - Jelly Bean
 - KitKat
 - Lollipop
 - Marshmallow
 - Nougat

### [LiteID-Contract-Tools](https://github.com/LiteID/LiteID-Contract-Tools)

Tools for interacting with the LiteID Ethereum Contract, as a Python package for Python 2.x.

Installation:

{% highlight python %}
pip install LiteID-Contract-Tools
{% endhighlight %}

Usage:

{% highlight python %}
>>> from LiteIDContractTools import LiteIDContract
>>> myContract = LiteIDContract()
# On enabled RPC servers allow you to unlock an account
>>> myContract.unlock_account(account, password)
>>> myContract.create_contract('Mark Omo')
>>> with open('DriversLicense.pdf') as file:
... 	myContract.add_hash(bytearray(file.read()))
>>> myContract.dump_hashes()
# Returns Salted Hash, Salt, Original Hash, Origanal Data
# You can also give it the address of an already existing contranct
>>> bobsContract = LiteIDContract(contract_id=bobsAddress)
>>> bobsContract.dump_hashes()
# Dump Bob's hashes
{% endhighlight %}

### [LiteID-Contract](https://github.com/LiteID/LiteID-Contract)

Ethereum Contract that powers LiteID.

### [LiteID-SimApp](https://github.com/LiteID/LiteID-SimApp)

Contains both the SIM app and the SMS server.

The SMS server is in the Server subdirectory, and is based on Flask and uses Shelve to store LiteIDContract instances.

The SIM app is in the SIM Client subdirectory, and is merely a skelton prototype at this time.