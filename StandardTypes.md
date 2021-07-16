# ITxPT Standard Types

This is the ITxPT list of Standard Types. A standard type is defined on a higher level than a specific language/format. When used in different formats / specifications the naming and content defined here should be respected as far as possible. 

Since these standard types are independent of any specific type system, they do not have any type as such. However categories of types found in most languages/format like `STRING`, `LIST`, `FLOAT`, `INTEGER` etc are used in the descriptions. 

## language

**Name:** `language`

**Content:** String describing language according to RFC 5646. RFC 5646 uses the ISO 639-x series of specifications, with additional requirements on when to use which one.  

## languages

**Name:** `languages`

**Content:** LIST of [`language`](#language) items. 
