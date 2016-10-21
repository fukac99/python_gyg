# python_gyg
> Python library for accessing the GetYourGuide API v1.

This is a pure Python library, handling all the connections to the GetYourGuide APIv1. It
supports searches for locations and tours by different parameters. Fro further information
on GetYourGuide API and for obtaining the api key look [here](https://partner.getyourguide.com/en/?cmp=brand&campaignid=173885129&adgroupid=10370624369&targetid=aud-57020326659:kwd-18417900866&loc_physical_ms=1001448&matchtype=e&network=g&device=c&creative=111291492689&partner_id=FDBE4&gclid=CLnPycqJ7M8CFeEV0wodvisCIg)

## Installation

```sh
pip install python_gyg
```

## Usage example

Create GetYourGuide object

```sh
from python_gyg import GetYourGuide
gyg = GetYourGuide(<your_api_key>)
```

Get New York by its id (59)
```sh
gyg.get_location(59)
```

Get New York Photography Experience by Night by its tour id (20434)
```sh
gyg.get_tour(20434)
```

Get tours today in New York by query search 
```sh
import datetime

gyg.search_tours(q="New York", date=datetime.datetime.now())
```

Get interesting POIs by coordinates
```sh
gyg.search_locations(coordinates=[40.75, -73.97, 10], location_type="poi")
```



## Development setup

To run development tests. Fill in your api key to test_location.py. 
Then run the following in the main directory:
```sh
python setup.py test
```

## Release History

* 0.1
    * All the functionality for API version 1

## Meta

Lukas Toma – [@lukas_toma](https://twitter.com/lukas_toma) – toma.lukas@gmail.com


