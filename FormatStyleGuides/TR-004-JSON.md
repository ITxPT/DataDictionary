| Version    | Document History | Date       | By  |
|------------|------------------|------------|-----|
| 1.0.0-rc.1 | First version    | 2021-05-20 | OAB |
|            |                  |            |     |

**Document intent**

*This document is intended to be used by TC as "design guideline" for a
specific domain while creating Technical Specifications (TS) and its
solutions.*

*The initial work of RC is to consolidate incoming requests into a
"Functional Requirements" document, that eventually can generate a
"Functional Specification" for an INTERFACE.*

*The following step (for TC) will be to create a "Technical
Specification" where relevant TR documents is used to make sure that the
designs of TS are streamlined and consistent.*

*Be aware, this is NOT a complete "System Specification", That is a
system supplier’s documentation of how they created a system from a
"Technical Specification".*

**Document Objectives**

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 66%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Subject</th>
<th>Description</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Concept</td>
<td>JSON format</td>
<td></td>
</tr>
<tr class="even">
<td>Document Level</td>
<td>Format</td>
<td></td>
</tr>
<tr class="odd">
<td>Requirement relation</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Epic story</td>
<td>Guidelines/rules for using JSON in ITxPT specifications</td>
<td>New, Draft, <strong>Completed</strong>,<br />
Approved</td>
</tr>
<tr class="odd">
<td>Stakeholder</td>
<td>TS writers and users</td>
<td></td>
</tr>
<tr class="even">
<td>Justification</td>
<td>Having a common guideline for JSON means specifications are more uniform and each TS work group does not need to spend time on basic formatting.</td>
<td></td>
</tr>
</tbody>
</table>

**------------------------------------------ Edit below this line
------------------------------------------------**

# Table of Contents

[1 JSON overview](#1-json-overview)

[1.1 JSON Standards](#1.1-json-standards)

[1.2 JSON introduction](#1.2-json-introduction)

[1.3 JSON Schema](#1.3-json-schema)

[2 ITxPT JSON rules](#2-itxpt-json-rules)

[2.1 Google JSON Style Guide](#2.1-google-json-style-guide)

[2.2 JSON Schema](#2.2-json-schema)

[2.2.1 Additional Properties](#2.1.1-additional-properties)

[2.3 JSON top-level](#2.3-json-top-level)

[2.4 Selecting good property names](#2.4-selecting-good-property-names)

[2.5 Whitespace](#2.5-whitespace)

[2.6 Comments](#2.6-comments)

[2.7 Google defined property names and structure](#2.7-google-defined-property-names-and-structure)

[2.8 Reserved names](#2.8-reserved-names)

[2.9 Reserved prefixes](#2.9-reserved-prefixes)

[2.9.1 Extensions](#2.9.1-extensions)

[2.9.2 Draft and Proposal](#2.9.2-draft-and-proposal)

[2.10 Existing JSON](#2.10-existing-json)

[2.11 Versioning](#2.11versioning)

[2.12 Usage of null](#2.12-usage-of-null)

[2.13 Binary data](#2.13-binary-data)

[2.14 Google time and position values](#2.14-google-time-and-position-values)

# 1 JSON overview

JSON is a text based format used to store and transmit data objects
consisting of attribute–value pairs and array data types (or any other
serializable value). JSON has supplanted xml as the most used format to
exchange information between ip-based APIs/services/applications.

## 1.1 JSON Standards

JSON is covered by several standards. RFC 8259 is a good starting point
(<https://tools.ietf.org/html/rfc8259>).

## 1.2 JSON introduction

The internet is full of good Json introductions, starting with the Json
Wikipedia page <https://en.wikipedia.org/wiki/JSON>

## 1.3 JSON Schema

A "recent" addition to JSON is a schema language. It currently exists as
a draft at <http://json-schema.org/> and at ietf.org. Once approved it
will be released as a set of RFCs.

# 2 ITxPT JSON rules

As with other ITxPT Technical Requirement the TS may deviate from these
rules if there are compelling reasons for doing so, and the alternative
rule and the justification for it is stated in the TS, or in other
documentation submitted to TC.

## 2.1 Google JSON Style Guide

ITxPT have reviewed the Google JSON Style Guide and found that it fits
ITxPT usage well.

Any ITxPT work following this TR **shall follow the Google JSON Style
Guide** <https://google.github.io/styleguide/jsoncstyleguide.xml>

and apply **all exceptions, additions, etc found in this TR**.

The Google JSON Style Guide was at version 0.9 when this decision was
taken.

## 2.2 JSON Schema

All usages of JSON format in ITxPT specification **shall** be
accompanied by a JSON Schema according to

<https://json-schema.org/>

### 2.2.1 Additional Properties

Schemas should allow for additional not know properties. This allows
later version of a TS, and others, to extend the objects/functionality
without breaking clients using a Schema without those properties. (This
is the default behaviour)

## 2.3 JSON top-level 

The top-level JSON used for transfer and storage shall be object {}.
E.g. even if data is float, the data shall be encapsulated in object

```json
{"doorCloseTime": [12.6, 13, 6, 19.3]}  
```
never  
```json
[12.6, 13, 6, 19.3]
```

The exception is if several objects of the same type, or if the objects
contain type information. Then they may be transmitted/stored as

```json
[{<obj1>}, {<obj2>}, …, {<objN>}]
```

For streaming objects either over the wire or to storage, separating
JSON objects with newline is allowed:

```json
{"prop1": 43, "prop2": "text"}  
{"prop1": 61, "prop2": "text"}  
{"prop1": 90, "prop2": "text"}  
{"prop1": 104, "prop2": "text"}
```

Both of these are exceptions and will only be handled by the client if
the TS explicitly states it.

## 2.4 Selecting good property names

When choosing a property name, consider if that name or part of the
name, is a defined term in the Data Dictionary. If possible, avoid names
that would conflict with terms in the data dictionary, or other common
usage in Public Transport and IT.

## 2.5 Whitespace 

When transmitted ("over the wire") there shall be a minimum of
whitespace and newlines.

```json
{"prop1":43,"subobj":{"subprop1":6,"subprop2":"hello"}}
```

When examples etc are presented in specification, newlines and an
indentation of 2 spaces per level is recommended.

```json
{  
    "prop1": 43,  
    "subobj": {  
        "subprop1": 6,  
        "subprop2": "hello"  
    }  
}
```

## 2.6 Comments

The Google JSON Style Guide uses ‘//’ for comments in JSON examples,
which ITxPT specifications and other documents should also do.

```json
{  
    "prop1": 43,  
    "subobj": {  
    // subprop contains an integer value! ‘//’ are NOT valid JSON!  
    "subprop": 6  
    }  
}
```

Note: ‘// \<comment>’ is *not* valid JSON. It can only be used in
documents as example, not in JSON that is parseable.

## 2.7 Google defined property names and structure

The Google JSON Style Guide defines several properties names and their
structure, e.g. data and properties of a data object. These definitions
are mostly not applicable for ITxPT usage. The Google JSON Style Guide
should be respected, but in many cases avoiding conflict by using
another property name, e.g. payload, is preferable.

## 2.8 Reserved names

In addition to the reserved names in the Google JSON Style Guide, the
ITxPT Data Dictionary may reserve JSON property names for specific
usages/formats.

## 2.9 Reserved prefixes

### 2.9.1 Extensions

The prefix **‘ext\_‘** will never be used by any ITxPT specification. It
is reserved for organizations/suppliers/developer that want to add
additional properties to standardized objects.

Using **ext\_** does not protect against conflicts with other
organizations/suppliers/developer also using **ext\_**. For those
situations adding e.g., a supplier abbreviation/acronym will minimize
the risk for conflicts.

"**ext\_**busId" will never conflict with ITxPT specification but
*could* conflict with another supplier adding that with other
meaning/semantics of the data. Using "**ext\_\<supplierName>\_**busId"
makes conflict extremely unlikely.

It is strongly recommended that the property name after the prefix
follows the rules in this TR, and the conventions of the dataset where
it is being added. Doing so aids readability and makes it possible to
add the property to a later version of the ITxPT specification by
removing the prefix.

### 2.9.2 Draft and Proposal

Similarly, to **ext\_**, **draft\_** and **proposal\_** will never be
used by an officially *released* ITxPT specification. **draft\_** is
used to indicate that something is in the standard but may change.
**proposal\_** is used for a proposal put forward but not discussed or
agreed by the Technical Work Group.

## 2.10 Existing JSON

Both in existing ITxPT specifications and in other
standards/protocols/APIs there are JSON that to some degree or another
does not follow this Style Guide.

If an addition can be considered part of an existing set of JSON
definitions, and those definitions have a clear style of their own, then
it is recommended that additions stay with that style instead of
following this style guide. E.g. if some existing specification is
written with snake case

```json
{"this_is_the_first_prop": "value"}
```

then it should be extended in that manner, even if this TR mandates use
of camelCase:

```json
{"this_is_the_first_prop": "value", "this_an_added_prop": 42}
```

If this TR is *not* used, it must be clearly stated in the Technical
Specification.

## 2.11 Versioning

The property apiVersion is a reserved name and is used to indicate what
version of an API/TS data model a JSON object belongs to.

A TS is not *required* to have apiVersion as property for all objects,
but in general not having versioned data is a decision that seems good
initially, until the time a larger change is needed/preferable, after
which it may be deeply problematic.

Versioning of JSON objects (and of data model in general) will be
covered by the Data Dictionary group.

## 2.12 Usage of null

The general recommendation would be that properties that does not yet
have a value, has value null.

For *optional* properties, they should have the value null if they will
have a value later, and not be present if they will never have a value.

## 2.13 Binary data

Binary data encoded inside JSON should generally be base64 encoded. The
Technical Specification should state the encoding.

## 2.14 Google time and position values

The Google JSON Style Guide strictly defines the format of a UTC
timestamp, a duration, and a position value. For now, these definitions
shall not be considered mandatory for ITxPT JSON.
