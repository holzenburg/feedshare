feedshare.net
=============

Feedshare is a service to share and discover OPML feed lists.

The service can be found here: [feedshare.net](http://feedshare.net)

# Features
Currently the feature list is quite short:

- Users may upload or link to an OPML file
- The link list along with the file gets published under feedshare.net/user-defined-slug

# Future
These features would be quite nice to have. If somebody wants to work on them, please get in touch:

- Search: Implement a search engine  
	(currently basic text field lookup)
- Discovery: Find lists and feeds with specific tags
- Discovery: Find similar lists based on feeds and tags

## Required Technical Changes
To achive some of the planned features, the data models need some updates:

- Decouple tags from feeds  
	(currently stored in a text field)
- Decouple feeds from lists  
	(currently an actual feed exists multiple times, once for each list)

# Origin
[Brent Simmons](http://inessential.com), Author of NetNewsWire, MarsEdit, Glassboard and Vesper [posted his OPML file](http://inessential.com/2014/01/04/my_feeds), lamenting the lack of an OPML sharing service. That drove me to spend a weekend on Feedshare. Seemingly [there](https://twitter.com/search?q=feedshare.net) [is](http://blog.louisgray.com/2014/01/feedshareforrssopml.html) [some](http://inessential.com/2014/01/06/feedshare_net) [interest](http://rumproarious.com/2014/01/06/feedshare-an-opml-sharing-service/) in such a service. [Alex Kessinger](http://alexkessinger.net) encouraged me to open source the code. I think that's a great idea and hope that others might want to help improving it and adding features.

Arne Holzenburg  
[@holzenburg](https://twitter.com/holzenburg)  
January 2014