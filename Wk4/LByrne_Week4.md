##### Liam Byrne
##### DATA 620 - Web Analytics
##### Fall - 2017

# Homework 4

**Centrality measures can be used to predict (positive or negative) outcomes for a node.**

**Your task in this week’s assignment is to identify an interesting set of network data that is available on the web (either through web scraping or web APIs) that could be used for analyzing and comparing centrality measures across nodes.  As an additional constraint, there should be at least one categorical variable available for each node (such as “Male” or “Female”; “Republican”, “Democrat,” or “Undecided”, etc.)**

**In addition to identifying your data source, you should create a high level plan that describes how you would load the data for analysis, and describe a hypothetical outcome that could be predicted from comparing degree centrality across categorical groups.**

### *Blockchain as a Network*
The general definition of most cryptocurrencies (e.g. *Bitcoin*) is a pseudonymized, decentralized monetary system where transactions consist of a cryptographically signed message which transfers funds from one address to another via a public key. These transactions are available to the public via the currency's respective blockchain, which can be imagined as a public ledger.

The blockchain provides a certain level of anonymity, but if one were to discover an individual's public address, their transaction history on the blockchain would be immediately available via a simple network analysis; namely by looking at the public address's centrality within a subnetwork.

### *Uses of Network Analysis in the Blockchain*
The adoptive phase of cryptocurrencies (crypto) saw a large use in illegal purchases and money laundering. One of the relatively new illegal practices being carried out with crypto now are payment of ransoms. Being able to track down a addressee’s location would require a lot of reverse engineering and scouring of the web, but it would be possible. Using network analysis and the respective centrality of addresses, in what could be a vast network, would make the first step in this process, i.e. isolating addresses to a user or group, at least possible.

### *Accessing the Blockchain*
There are a few ways to access the blockchain. One use is through an [API provided by blockchain.info](https://blockchain.info/api), which looks at *Bitcoin* transactions. Through this API, one can look at a specific address to see the total amount of *Bitcoin* sent and received throughout its history . By using the block (a group of transactions within the blockchain) API, one would be able to see the transaction history that the address has had.

### *Possible Step-by-Step*
Let us say that we knew addresses, *Address A* for example, in which ransoms were paid. The following method could be used to document the transaction history:

* Using an API call ```https://blockchain.info/address/[Address A]?format=json``` would return all blocks associated with that address in json format. This would give us the *block height*'s (block ID's) in which that address has appeared.
* We then call ```https://blockchain.info/block-height/[associated block heights of Address A]?format=json``` to view the transaction activity associated with each address in all its associated blocks.
* This would be done repeatedly for all addresses associated with this address until a network is formed with any address that has a path to *Address A*
* This network should be stored in some manner for analysis, e.g. a .csv file.
* This network can be analyzed to find centralities in the network, namely *betweenness centrality* which quantifies the number of times a node acts as a bridge along the shortest path between two other nodes<sup>1</sup>.

By analyzing this network, one could find similar ransom transactions, central nodes that tie this network together and zero-sum addresses (addresses in which the sum of deposits and withdraws are zero). These things would lead to further understanding of a criminal network and key associated addresses within.

### *Reference and Inspiration*
The inspiration for this assignment came from a [blogpost on DZone](https://dzone.com/articles/analyzing-bitcoin-network) by Michael Hunger calling out the work of David Fauth in analyzing the blockchain using Neo4j.

<sup>1</sup>: Wiki [Betweenness Centrality](https://en.wikipedia.org/wiki/Betweenness_centrality)
