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

For some commonly used types it is a clear benefit for ITxPT if these types are 'reserved' on the top level, rather than being different in each specification. This applies to both recommended name of a property with such content, and the content itself. 

Location for this is [ITxPT Standard Types](./StandardTypes.md).

## Format Style Guides ##

While not developed by Data Dictionary Committee, the Data Dictionary Committee is guardian of ITxPT Format Styles Guides, and will do minor changes to keep the Format Styles Guides in line with other Data Dictionary Artifacts, e.g. Standard Types. 

### Format Rules JSON (TR-004)

[TR-004 JSON Format Rules](./FormatRules/TR-004-JSON.md)

## MQTT ##

Several things relating to ITxPT usage of MQTT is related to Data Dictionary Responsibilities. 

### Function group names and Provider names ###

MQTT Function group names and Providers Names are approved by Data Dictionary Work Group and documented at [MQTT Names](./MQTT/MQTTNames.md)

### MQTT Provider Topic structure ###

It is possible that Data Dictionary group will take over responsibility for the rules/guideline on how each provider should be organized internally. However, this is for now not decided. The current guidelines, as they are, are part of TR-003 MQTT.

### MQTT User Properties ###

MQTT v5 adds User Properties (aka metadata) that can be added to the header of messages and provide additional information to the payload itself. Data Centric requires the payload to enough information on its own; but User Properties can be very useful for adding data during system integration, analysis of message losses, timing analysis, and other things not directly related the function of the payload. ITxPT standardized User Properties will often relate to Standard Types. 

ITxPT standardized [MQTT User Properties](./MQTT/MQTTUserProperties.md)

## Tools ## 

Various scripts etc with (potential) usage for Data Dictionary. 
