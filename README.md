# DataDictionary #

This is the repository for the ITxPT Data Dictionary

It contains the ITxPT Data Dictionary Terms and Definitions, Instructions and Guidelines, etc, etc 

(Fill this out more once it is a bit more decided.)

## What is the ITxPT Data Dictionary? And why? ##

(Fill out)

## Usage, Instructions and Guidelines ##

See the [DataDictionary Wiki](../../wiki) for how to use the Data Dictionary, instructions for how to add items to the Data Dictionary and Guidelines for defining Terms & Definitions and modeling data. 

## Concepts ##

[ITxPT Concepts](./Concepts/Concepts.md) Includes Transmodel Concepts.

## Modeling Guideline ##

In [DataDictionary Wiki](../../wiki)

# Other responsibilities #

In addition to the Data Dictionary itself the Data Dictionary Working Group is responsible for a few other things that has to do with naming and data in ITxPT.

## Standard Types ##

For some commonly used types, e.g. timestamps or sequence-numbers, it is a clear benefit for ITxPT if these types are 'reserved' on the top level, rather than being different in each specification. This applies to both recommended name of a property with such content, and the content itself. 

Location for this is TDB.

## MQTT ##

Several things relating to ITxPT usage of MQTT is related to Data Dictionary Responsibilities. 

### Function group names and Provider names ###

MQTT Function group names and Providers Names are approved by Data Dictionary Work Group and documented at [MQTT Names](./MQTT/MQTTNames.md)

### MQTT User Properties ###

MQTT v5 adds User Properties (aka metadata) that can be added to the header of messages and provide additional information to the payload itself. Data Centric requires the payload to enough information on its own; but User Properties can be very useful for adding data during system integration, analysis of message losses, timing analysis, and other things not directly related the function of the payload. ITxPT standardized User Properties will often relate to Standard Types. 

ITxPT standardized [MQTT User Properties](./MQTT/MQTTUserProperties.md)

## Tools ## 

Various scripts etc with (potential) usage for Data Dictionary. 
