# Examples

The following section shows some simple examples.
### Fetching the latest prices

After you successfully installed the library you can now start to play around with it.

```python
>>> from Pycurrency import Pycur
>>>
>>> cur = Pycur('USD')
>>>
>>> cur.get_currency()
{'INR': 65.01, 'BGN': 1.6549, 'GBP': 0.75836, 'ZAR': 13.684, 'ILS': 3.4876, 'EUR': 0.84617, 'SGD': 1.3584, 'SEK': 8.1609, 'JPY': 113.17, 'KRW': 1130.6, 'MXN': 18.893, 'CNY': 6.6185, 'RUB': 57.428, 'MYR': 4.225, 'DKK': 6.2987, 'PLN': 3.5846, 'CZK': 21.738, 'THB': 33.16, 'CHF': 0.9813, 'BRL': 3.1747, 'NZD': 1.4288, 'IDR': 13510.0, 'PHP': 51.502, 'HUF': 260.73, 'AUD': 1.2739, 'HKD': 7.803, 'NOK': 7.9662, 'HRK': 6.3518, 'CAD': 1.2494, 'RON': 3.8899, 'TRY': 3.663}
```
The function ```get_currency()``` will return an ordinary Python dict where you can access the value by your country key.
### Filter countries

```python
>>> sek = cur.get_currency()['SEK']
>>> sek
8.1609
```
So here we can se that for $1 you'll need to pay 8.1609 Swedish kronor.

### Iterate through a list of countries
```python
>>> c_list = ['SEK', 'NOK', 'DKK']
>>> for c in c_list:
...     cur.get_currency()[c]
...
8.1609
7.9662
6.2987
```

### Access historical data
The method ```get_historical()``` requires one argument and it should be formatted ```yyy-mm-dd```.
```python
>>> cur = Pycur('EUR')
>>> cur.get_historical('2001-08-09')
{'ROL': 26380.0, 'ZAR': 7.3259, 'SKK': 42.815, 'CZK': 33.85, 'SGD': 1.5721, 'EEK': 15.647, 'TRL': 1221000.0, 'USD': 0.8853, 'HKD': 6.9049, 'CHF': 1.5057, 'PLN': 3.7345, 'ISK': 86.95, 'CYP': 0.57362, 'SIT': 219.42, 'HUF': 246.5, 'CAD': 1.3584, 'BGN': 1.947, 'NOK': 7.985, 'KRW': 1137.6, 'AUD': 1.7135, 'DKK': 7.4422, 'SEK': 9.1734, 'JPY': 109.16, 'NZD': 2.0836, 'LTL': 3.541, 'LVL': 0.5598, 'GBP': 0.6234, 'MTL': 0.4021}
>>>
```

If you only want one country, you can filter with your country key as we saw in the previous examples.

```python
>>> hist = cur.get_historical('2001-08-09')
>>> hist['SEK']
9.1734
>>>
```

### Supported countries
The following countries are supported by Pycurrency. For more information see [fixer.io](http://fixer.io).

Key | Country
------------ | -------------
AUD | Australia
BGN | Bulgaria
BRL | Brazil
CAD | Canada
CHF | Liechtenstein
CNY | China
CZK | Czech Republic
DKK | Denmark
GBP | South Georgia Island (UK)
HKD | Hong Kong
HRK | Croatia
HUF | Hungary
IDR | Indonesia
ILS | Isle of Man (UK)
INR | India
JPY | Japan
KRW | South Korea
MXN | Mexico
MYR | Malaysia
NOK | Norway
NZD | New Zealand
PHP | Philippines
PLN | Poland
RON | Romania
RUB | Russia
SEK | Sweden
SGD | Singapore
THB | Thailand
TRY | Turkey
USD | United States Of America
ZAR | South Africa
