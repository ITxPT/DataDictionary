This is the list current approved MQTT Function Group Names and MQTT Provider Names. 

All ITxPT MQTT Providers will have an onboard topic starting with `[itxpt-root]/[Function Group]/[Provider Name]` This document contains all ITxPT Function Group Names and Provider Names. 

# Format # 

This document will use this format to list Function Group Names and Provider Names: 

## function group name ## 

**Status:** Proposal (One of Proposal/Draft/Approve?)

**Description:** A description of what the Function Group contains and the rules for being added to it.

### Provider Name ###

Note: Providers in the function group.

**Status:** Proposal (One of Proposal/Draft/Approve?)

**Description:** Short description of Provider. This does not need to be detailed - the technical specification can be consulted for details.

# Non ITxPT Providers # 

The expectation is that the `[itxpt-root]` topic contains Providers specified in  ITxPT Technical Specifications only. Having non-ITxPT Functional Group Names or non-ITxPT Provider Names could cause conflicts with future ITxPT Functional Group Names and/or Provider Names. 

But there are situations where putting a non-ITxPT provider inside `[itxpt-root]` could be beneficial. To allow this, while at the same time preventing future conflicts, ITxPT will never use the following prefixes as part of Function Group Names or Provider Names

- `ext_` (short for extension) 
- `proposal_` 
- `draft_` 

Note: This is copied form JSON Style Guide. Perhaps there should be another one like `nonstd_` for more general non-standard stuff that does not match the three above? 

Note: This should probably apply to *all* topics, also those "inside" a Provider. 

# Style of Names #

Function Group Names, Provider Names, and other topic elements are by convention lower case without any punctuation. E.g. `somefunction` and `fancything` are used not `someFunction` / `fancyThing`, `some-function` / `fancy-thing`, `some_function` / `fancy_thing`, `SOMEFUNCTION` / `FANCYTHING`, etc

This is a convention, not a _rule_, and should not be relied on. 

# Function Group Names and Provider Names #

This is the list of defined ITxPT Function Group Names with defined Provider Names for each. 

## inventory ##

**Status:** Proposal

**Description:** Function Group for the all the inventory related information. This Function Group is wholly owned by the inventory (mqtt) specification (Note: TBD), all sub-topics (Provider Names) will be specified in that specification. 

## sensors ##

**Status:** Proposal 

**Description:** Function Group for sensors. For a Provider to fit the sensor group it should:

- Not belong to any other Function Group. There may be cases where a Provider fulfills all other requirements for being a sensor, but still would be better placed in another Function Group.
- Be a reasonably simple output corresponding to some physical quantities. 
- Not have complex dependencies to other providers as input. 

