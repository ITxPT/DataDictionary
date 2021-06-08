The specification of MQTT User Properties is **TBD**. 


# Mandatory Properties #

Of the Standardized Properties, the following are Mandatory and must be supported by ITxPT Providers: 

- [NO MANDATORY ATTRIBUTES DEFINED YET]

Each Technical Specification may modify the list of Mandatory Properties. 

# Standardized Properties #

**No standardization have happened yet, below only example**

## timestamp ##

**Name:** timestamp

**Value:** Timestamp according to TR-001, preferably with ms.

## Sequence Number ##

**Name:** MQTTPublishSeqNbr

**Value:** MQTT specific Sequence Number that increments with 1 for each Publish on that specific topic. Starts at 1. Max value 4 294 967 296 (2^32). Value 0 (zero) means wrap-around. 
