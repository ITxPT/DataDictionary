# ITxPT Data Dictionary Concepts #

This is the ITxPT Data Dictionary Concepts with Concept Definitions, incorporating the Transmodel Definitions. ...

## ABSENCE ##

**Source:** Transmodel

**Definition:** An ABSENCE represents an actual absence of an EMPLOYEE from work on a particular OPERATING DAY for a specified time.

## ACCESS ##

**Source:** Transmodel

**Definition:** The physical (spatial) possibility for a passenger to access or leave the public transport system. This link may be used during a trip for:- the walking movement of a passenger from a PLACE (origin of the trip) to a SCHEDULED STOP POINT (origin of the PT TRIP), or- the walking movement from a SCHEDULED STOP POINT (destination of the PT TRIP) to a PLACE (destination of the trip).

## ACCESS END ##

**Source:** Transmodel

**Definition:** Origin or destination end of an ACCESS link. May indicate a POINT and/or PLACE.

## ACCESS LEG ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN corresponding to the movement of a passenger when not on a public transport vehicle, from an origin PLACE to a SCHEDULED STOP POINT, or a SCHEDULED STOP POINT to a destination PLACE. May reference an ACCESS.

## ACCESS MODE ##

**Source:** Transmodel

**Definition:** A characterisation of the passenger movement according to the means of transport different from public transport (e.g. walk, bicycle, etc)

## ACCESS RIGHT IN PRODUCT ##

**Source:** Transmodel

**Definition:** A VALIDABLE ELEMENT as a part of a PRE-ASSIGNED FARE PRODUCT, including its possible order in the set of all VALIDABLE ELEMENTs grouped together to define the access right assigned to that PRE-ASSIGNED FARE PRODUCT.

## ACCESS RIGHT PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of a fare collection parameter (referring to geography, time, quality or usage) to an element of a fare system (access right, validated access, control mean, etc.).

## ACCESS SPACE ##

**Source:** Transmodel

**Definition:** A passenger area within a STOP PLACE such as a concourse or booking hall, immigration hall or security area that is accessible by passengers, but without a direct access to vehicles. Direct access to a VEHICLE is always from a QUAY and/or BOARDING POSITION. An ACCESS SPACE may be a Room, Hall, Concourse, Corridor, or bounded open space within a STOP PLACE.

## ACCESS ZONE ##

**Source:** Transmodel

**Definition:** A ZONE for which the duration to cover any ACCESS link to a particular SCHEDULED STOP POINT is the same.

## ACCESSED FARE STRUCTURE ELEMENT ##

**Source:** Transmodel

**Definition:** A validated use of a FARE STRUCTURE ELEMENT, composed of CONTROLLED ACCESSes.

## ACCESSIBILITY ASSESSMENT ##

**Source:** Transmodel

**Definition:** The accessibility characteristics of an entity used by passengers such as a STOP PLACE, or a STOP PLACE COMPONENT. Described by ACCESSIBILITY LIMITATIONs, and/or a set of SUITABILITies

## ACCESSIBILITY LIMITATION ##

**Source:** Transmodel

**Definition:** A categorisation of the accessibility characteristics of a SITE, e.g. a STOP PLACE or a STOP PLACE COMPONENT to indicate its usability by passengers with specific needs, for example, those needing wheelchair access, step-free access or wanting to avoid confined spaces such as lifts. A small number of well-defined categories are used that are chosen to allow the consistent capture of data and the efficient computation of routes for different classes of user.

## ACCOMODATION ##

**Source:** Transmodel

**Definition:** A combination of accommodation characteristics available on a service, e.g. First Class Couchette with shower and 2 bunks"."

## ACCOUNT AUTO RENEWAL EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System that a renewable product such as a pass needs to be renewed. Depending on configuration may trigger either an automatic renewal or a notice to the customer.

## ACCOUNT AUTO TOP UP EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System that the account balance has fallen below a threshold which needs to be topped up using a preset payment method and increment.

## ACCOUNT AWARD REFUND EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System that a refund needs to be awarded, for example because guaranteed performance targets have not been met

## ACCOUNT DETECT ELIGIBILITY CHANGE EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System of a change in the eligibility of a user for a product they currently own, requiring an adjustment of some sort.

## ACCOUNT DETECT NO CHECK IN EVENT ##

**Source:** Transmodel

**Definition:** The detection that a passenger has failed to check in at the beginning of a trip. This may be triggered by a subsequent check out or by back office processes looking for unmatched check in and check out events within a specified window.

## ACCOUNT DETECT NO CHECK OUT EVENT ##

**Source:** Transmodel

**Definition:** The detection that a passenger has failed to check out at the end of a trip. This may be triggered by a subsequent check in on a new journey or by back office processes looking for unmatched check in and check out events within a specified window..

## ACCOUNT DETECT REENTRY EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System of reentry at the same station within a specified threshold period.

## ACCOUNT DETECT SUSPICIOUS BEHAVIOUR EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System of suspicious or fraudulent use of a TRAVEL DOCUMENT, for example being used in two different places at the same time.

## ACCOUNT DETECT TRIP EVENT ##

**Source:** Transmodel

**Definition:** The detection by an ABT System of a trip made by the user that needs to be accounted for.

## ACCOUNT ENTRY ##

**Source:** Transmodel

**Definition:** An ACCOUNT ENTRY is a record of aggregated ACTIVITY LOG ENTRY data per WAGE TYPE, EMPLOYEE and COST CENTRE for one OPERATING DAY that is used to transfer information on duties actually worked by drivers to an external accounting system.

## ACCOUNT PROCESSING EVENT ##

**Source:** Transmodel

**Definition:** An event initiated by the processing of a CUSTOMER ACCOUNT by an ABT System.

## ACCOUNT PROVIDER ROLE ##

**Source:** Transmodel

**Definition:** In Account Based Ticketing, the ACCOUNT PROVIDER provides the online account by means of which the product is delivered. Normally this involves a direct relationship with the CUSTOMER, though it may also be done as a white-labelled service for a another party

## ACCOUNT REVIVE ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the reinstatement of a CUSTOMER ACCOUNT.

## ACCOUNT REVIVE EVENT ##

**Source:** Transmodel

**Definition:** The reinstatement of a suspended CUSTOMER ACCOUNT.

## ACCOUNT SALES EVENT ##

**Source:** Transmodel

**Definition:** A sales event affecting a CUSTOMER ACCOUNT.

## ACCOUNT SECURITY EVENT ##

**Source:** Transmodel

**Definition:** A securty event initiated by the processing of a CUSTOMER ACCOUNT by an ABT System.

## ACCOUNT SUSPEND ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the denying of access to the transport network by the addition to a BLACK LIST or removal from a WHITE LIST of a token that identifies a CUSTOMER, CUSTOMER ACCOUNT, FARE CONTRACT, TRAVEL DOCUMENT, etc.

## ACCOUNT SUSPEND EVENT ##

**Source:** Transmodel

**Definition:** The suspension of a CUSTOMER ACCOUNT.

## ACCOUNTING PERIOD ##

**Source:** Transmodel

**Definition:** An ACCOUNTING PERIOD is a continuous interval between two OPERATING DAYs which will be used for accounting purposes.

## ACTIVATED EQUIPMENT ##

**Source:** Transmodel

**Definition:** An equipment activated by the passage of a vehicle at an ACTIVATION POINT or on an ACTIVATION LINK.

## ACTIVATION ASSIGNMENT ##

**Source:** Transmodel

**Definition:** An assignment of an ACTIVATION POINT/LINK to an ACTIVATED EQUIPMENT related on its turn to a TRAFFIC CONTROL POINT. The considered ACTIVATION POINT/LINK will be used to influence the control process for that TRAFFIC CONTROL POINT (e.g. to fix priorities as regards the processing of competing requests from different ACTIVATION POINTs/LINKs).

## ACTIVATION LINK ##

**Source:** Transmodel

**Definition:** A LINK where a control process is activated when a vehicle passes it.

## ACTIVATION POINT ##

**Source:** Transmodel

**Definition:** A POINT where a control process is activated when a vehicle passes it. Equipment may be needed for the activation.

## ACTIVITY LOG ENTRY ##

**Source:** Transmodel

**Definition:** An ACTIVITY LOG ENTRY is a record, including data needed for accounting, of the actual time worked, planned as well as unplanned,in a STRETCH, or spent for a BREAK, by an EMPLOYEE on a specified OPERATING DAY.

## ACTUAL VEHICLE EQUIPMENT ##

**Source:** Transmodel

**Definition:** An item of equipment of a particular type in an individual VEHICLE.

## ADDRESS ##

**Source:** Transmodel

**Definition:** The descriptive data associated with a PLACE that can be used to describe the unique geographical context of a PLACE for the purposes of identifying it. May be refined as either a ROAD ADDRESS, a POSTAL ADDRESS or both.

## ADDRESSABLE PLACE ##

**Source:** Transmodel

**Definition:** A type of PLACE to which passengers may refer to indicate the origin or a destination of a trip and that is so specific that it has an ADDRESS.

## ADJUST BALANCE ON CHECK IN ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the adjustment of the balance from an amount deposited on account on a MEDIUM ACCESS DEVICE when a passenger checks in or interacts with a system.

## ADMINISTRATIVE ORGANISATION ROLE ##

**Source:** Transmodel

**Definition:** Any organisational role involving some aspect of the management of data or the use of data.

## ADMINISTRATIVE ZONE ##

**Source:** Transmodel

**Definition:** The area of a district, a region, a city, a municipality, or other area with which an ORGANIZATION has a RESPONSIBILITY ROLE;

## ALARM ##

**Source:** Transmodel

**Definition:** An EVENT alerting the staff in charge of operations control on a probable dysfunction: operational threshold exceeded (e.g. delay), emergency call, failure, etc.

## ALLOW ACCOUNT ON SECURITY LIST EVENT ##

**Source:** Transmodel

**Definition:** The granting of rights by placing an ENTITY on a WHITE LIST and/or removing it from a BLACK LIST.

## ALLOWED LINE DIRECTION ##

**Source:** Transmodel

**Definition:** An allowed DIRECTION that can be used on a given ROUTE. This can be used to validate the selection of allowed values.

## ALTERNATIVE NAME ##

**Source:** Transmodel

**Definition:** Alternative name for the entity.

## ALTERNATIVE TEXT ##

**Source:** Transmodel

**Definition:** Alternative text for any textual attribute of an ENTITY.

## AMOUNT OF PRICE UNIT ##

**Source:** Transmodel

**Definition:** A FARE PRODUCT consisting in a stored value of PRICE UNITs: an amount of money on an electronic purse, amount of units on a value card etc.

## ARRIVAL ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the arrival to a POINT IN JOURNEY PATTERN in a VEHICLE JOURNEY.

## ASSIGNED DUTY ##

**Source:** Transmodel

**Definition:** An ASSIGNED DUTY is a DUTY to which specific timed work has been assigned.

## ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The association of one or more other assigned ENTITies with a primary ENTITY in order to describe some characteristic of the 'assigned to' ENTITY. The assignment may itself also have attributes.  There may be multiple assignments applying to the same entity in which case an order and or VALIDITY CONDITIONs may apply in order to determine the current assignment to use.

## ASSISTANCE SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of LOCAL SERVICE for ASSISTANCE providing information like language, accessibility trained staff, etc.

## AUTHORITY ##

**Source:** Transmodel

**Definition:** The organisation under which the responsibility of organising the transport service in a certain area is placed.

## AVAILABILITY CONDITION ##

**Source:** Transmodel

**Definition:** A VALIDITY CONDITION expressed in terms of temporal parameters and referring to DAY TYPEs.

## BEACON POINT ##

**Source:** Transmodel

**Definition:** A POINT where a beacon or similar device to support the automatic detection of vehicles passing by is located.

## BECOMES ELIGIBLE ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the detection that a user has become eligible for a product for which they were previously ineligible, e.g. by virtue of growing older, changing employment status, or residence.

## BLACKLIST ##

**Source:** Transmodel

**Definition:** A list of items (TRAVEL DOCUMENTs, CONTRACTs etc) the validity of which has been cancelled temporarily or permanently, for a specific reason like loss of the document, technical malfunction, no credit on bank account, offences committed by the customer, etc.

## BLOCK ##

**Source:** Transmodel

**Definition:** The work of a vehicle from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT. Any subsequent departure from a PARKING POINT after parking marks the start of a new BLOCK. The period of a BLOCK has to be covered by DUTies.

## BLOCK PART ##

**Source:** Transmodel

**Definition:** Part of a BLOCK corresponding to the different JOURNEY PARTs of the VEHICLE JOURNEYs in a BLOCK.

## BOARDING AND ALIGHTING ##

**Source:** Transmodel

**Definition:** The numbers of passengers boarding and alighting at a STOP POINT during a RECORDED STOP.

## BOARDING BASED PASSENGER COUNT ##

**Source:** Transmodel

**Definition:** Possible implementation of LOGGABLE OBJECT designed for passenger counting based on BOARDING AND ALIGHTHING (independent from the counting method)

## BOARDING POSITION ##

**Source:** Transmodel

**Definition:** A location within a QUAY from which passengers may directly board, or onto which passengers may directly alight from a VEHICLE.

## BOOKING ARRANGEMENTS ##

**Source:** Transmodel

**Definition:** Booking arrangements for FLEXIBLE LINE.

## BOOKING DEBIT ##

**Source:** Transmodel

**Definition:** A log entry providing data for a debiting action for a booking fee.

## BOOKING POLICY ##

**Source:** Transmodel

**Definition:** Details of the booking arrangements  for a service.

## BORDER POINT ##

**Source:** Transmodel

**Definition:** A POINT on the network marking a boundary for the fare calculation. May or may not be a SCHEDULED STOP POINT.

## BREAK ##

**Source:** Transmodel

**Definition:** A BREAK is a period of time within a DUTY PART during which the driver is not responsible for a vehicle and can rest, usually at a BREAK FACILITY.

## BREAK FACILITY ##

**Source:** Transmodel

**Definition:** A BREAK FACILITY is a canteen, cafe, kiosk or any place where drivers have toilet and refreshment facilities.

## CALL ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the individual visit to a POINT IN JOURNEY PATTERN in a VEHICLE JOURNEY.

## CALL FOR MEANS ##

**Source:** Transmodel

**Definition:** A MESSAGE of a controller sent to a PARKING POINT to ask for the disposal of resources in stand-by.

## CALL FOR REPAIRS ##

**Source:** Transmodel

**Definition:** A MESSAGE of a controller sent to a GARAGE to ask for repair of a VEHICLE.

## CALL PART ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the arrival to or the departure from a POINT IN JOURNEY PATTERN in a VEHICLE JOURNEY.

## CANCELLING ##

**Source:** Transmodel

**Definition:** A parameter giving conditions for cancelling of a booked access right.

## CAPPED DISCOUNT RIGHT ##

**Source:** Transmodel

**Definition:** A specialisation of SALE DISCOUNT RIGHT where the discount is expressed as a rule specifying a ceiling for a given time interval. For example, the London Oyster card fare, which charges for each journey until travel equivalent to a day pass has been consumed after which further travel is free at that day.

## CAPPING RULE ##

**Source:** Transmodel

**Definition:** A capping limit for a given time interval, where the capping is expressed by another product. For example, the London Oyster card fare, which charges for each journey until travel equivalent to a day pass for the mode of travel has been consumed.

## CAPPING RULE PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a CAPPING RULE: default total price, discount in value or percentage etc.

## CASUALTIES ##

**Source:** Transmodel

**Definition:** A description of the number of persons that have been injured or died.

## CATERING SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of LOCAL SERVICE dedicated to catering service.

## CEASES TO BE ELIGIBLE ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the detection that a user has ceased to be eligible for a product for which they were previously eligible, e.g. by virtue of growing older, changing employment status, or residence.

## CELL ##

**Source:** Transmodel

**Definition:** An unique individual combination of features within a FARE TABLE, used to associate a FARE PRICE with a fare element.

## CHANGE OF DRIVER ##

**Source:** Transmodel

**Definition:** A CHANGE OF DRIVER is a CONTROL ACTION consisting in removing, at a certain point in time and space (in principle a RELIEF POINT), all work assigned to a LOGICAL DRIVER and of assigning it to another LOGICAL DRIVER.

## CHANGE OF JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in assigning a new JOURNEY PATTERN (and the ROUTE supporting it) to a DATED VEHICLE JOURNEY.

## CHANGE OF JOURNEY TIMING ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in changing one or several characteristics of a DATED VEHICLE JOURNEY, in particular the departure time of the journey.

## CHANGE OF VEHICLE ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in removing, at a certain point in time and space, all work assigned to a LOGICAL VEHICLE and of assigning it to another LOGICAL VEHICLE.

## CHARGING MOMENT ##

**Source:** Transmodel

**Definition:** A classification of FARE PRODUCTs according to the payment method and the account location: pre-payment with cancellation (throw-away), pre-payment with debit on a value card, pre-payment without consumption registration (pass), post-payment etc.

## CHARGING POLICY ##

**Source:** Transmodel

**Definition:** A parameter governing minimum amount and credit allowed when consuming a FARE PRODUCT.

## CHECK CONSTRAINT ##

**Source:** Transmodel

**Definition:** Characteristics of a process that takes place at a SITE COMPONENT, such as check-in, security screening, ticket control or immigration, that may potentially incur a time penalty that should be allowed for when journey planning.

## CHECK CONSTRAINT DELAY ##

**Source:** Transmodel

**Definition:** Time penalty associated with a CHECK CONSTRAINT.

## CHECK CONSTRAINT THROUGHPUT ##

**Source:** Transmodel

**Definition:** Throughput of a CHECK CONSTRAINT: the number of passengers who can pass through it in a specified interval.

## CLASS ATTRIBUTE ##

**Source:** Transmodel

**Definition:** Any attribute of a class. (metalevel component)

## CLASS IN FRAME ##

**Source:** Transmodel

**Definition:** The different CLASSEes IN REPOSITORY which can be relevant for corresponding VERSION FRAMEs.

## CLASS IN REPOSITORY ##

**Source:** Transmodel

**Definition:** Any ENTITY name belonging to the repository. E.g. DAY TYPE, PROPERTY OF DAY, TIME BAND, VEHICLE TYPE, etc, are relevant instances of CLASS IN REPOSITORY in the context of version management.

## CLASS OF USE ##

**Source:** Transmodel

**Definition:** A classification of fare and other service classes by category of user entitled to use them.

## COLUMN/DAY ##

**Source:** Transmodel

**Definition:** A COLUMN/DAY is a column in a ROSTER MATRIX which is related to an OPERATING DAY.

## COMMERCIAL PROFILE ##

**Source:** Transmodel

**Definition:** A category of users depending on their commercial relations with the operator (frequency of use, amount of purchase etc.), often used for allowing discounts.

## COMMERCIAL PROFILE ELIGIBILITY ##

**Source:** Transmodel

**Definition:** A parameter indicating whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT linked to a specific COMMERCIAL PROFILE.

## COMMON SECTION ##

**Source:** Transmodel

**Definition:** A part of a public transport network where the ROUTEs of several JOURNEY PATTERNs are going in parallel and where the synchronisation of SERVICE JOURNEYs may be planned and controlled with respect to commonly used LINKs and SCHEDULED STOP POINTs. COMMON SECTIONs are defined arbitrarily and need not cover the total lengths of topologically bundled sections.

## COMMUNICATION SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of LOCAL SERVICE dedicated to communication services.

## COMPANION PROFILE ##

**Source:** Transmodel

**Definition:** The number and characteristics of the persons entitled to travel in a group or as companions to another USER PROFILE.

## COMPANION ROLE ##

**Source:** Transmodel

**Definition:** The role of accompanying another PASSENGER under the access rights granted by the other PASSENGER's ticket.

## COMPLAINTS SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of CUSTOMER SERVICE for COMPLAINTs

## COMPLEX FEATURE ##

**Source:** Transmodel

**Definition:** An aggregate of SIMPLE FEATUREs and/or other COMPLEX FEATUREs.

## COMPLEX FEATURE PROJECTION ##

**Source:** Transmodel

**Definition:** An oriented correspondence: from one COMPLEX FEATURE in the source layer, onto an entity in a target layer: e.g. POINT, COMPLEX FEATURE, within a defined TYPE OF PROJECTION.

## COMPOSITE FRAME ##

**Source:** Transmodel

**Definition:** A set of VERSION FRAMEs to which the same VALIDITY CONDITIONs have been assigned.

## COMPOSITE JOURNEY CONTROL ACTION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION affecting a set of DATED VEHICLE JOURNEYs with a correlated set of adjustments.

## COMPOUND BLOCK ##

**Source:** Transmodel

**Definition:** The work of a vehicle during the time it is coupled to another vehicle.

## COMPOUND TRAIN ##

**Source:** Transmodel

**Definition:** A VEHICLE TYPE composed of a sequence of more than one vehicles of the type TRAIN.

## CONDUCTOR ROLE ##

**Source:** Transmodel

**Definition:** The CONDUCTOR ROLE is to manage the on-board delivery of services and undertakes control and validation of TRAVEL DOCUMENTS.

## CONNECTION ##

**Source:** Transmodel

**Definition:** The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip, determined by two SCHEDULED STOP POINTs. Different times may be necessary to cover the link between these points, depending on the kind of passenger.

## CONNECTION END ##

**Source:** Transmodel

**Definition:** One end of a CONNECTION.

## CONTACT DETAILS ##

**Source:** Transmodel

**Definition:** Contact details for ORGANISATION for public use.

## CONTINUOUS DUTY ##

**Source:** Transmodel

**Definition:** A CONTINUOUS DUTY is a classification of a DUTY, in terms of working hours within the day comprising a single period of paid work.

## CONTROL ACTION ##

**Source:** Transmodel

**Definition:** An action resulting from a decision taken by the controller causing an amendment of the operation planned in the PRODUCTION PLAN.

## CONTROL CENTRE ##

**Source:** Transmodel

**Definition:** An ORGANISATION PART for an operational team who are responsible for issuing commands to control the services.

## CONTROL ENTRY ##

**Source:** Transmodel

**Definition:** The description of a control action, i.e. the comparison of actual and current parameters (time, location, ...) to the access rights to which the holder of a TRAVEL DOCUMENT is entitled.

## CONTROL MEANS ##

**Source:** Transmodel

**Definition:** A particular means (control device or manual control procedure) used to control TRAVEL DOCUMENTs.

## CONTROL PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** An ACCESS RIGHT PARAMETER ASSIGNMENT relating a fare collection parameter to a CONTROL ENTRY.

## CONTROL PASSENGER TRIP ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the control of the consumption of access rights by the inspection of a TRAVEL DOCUMENT by a TRAVEL DOCUMENT CONTROLLER. May include marking (cancellation) of the TRAVEL DOCUMENT.

## CONTROL PASSENGER TRIP EVENT ##

**Source:** Transmodel

**Definition:** The control of the consumption of access rights by the inspection of a TRAVEL DOCUMENT by a travel document inspector.

## CONTROL RECORD ##

**Source:** Transmodel

**Definition:** A log entry providing general audit properties of a validation or control action.

## CONTROL TYPE ##

**Source:** Transmodel

**Definition:** A classification of passenger controls, e.g. entry, exit, en route or occasional controls.

## CONTROLLABLE ELEMENT ##

**Source:** Transmodel

**Definition:** The smallest controllable element of public transport consumption, all along which any VALIDITY PARAMETER ASSIGNMENT remains valid.

## CONTROLLABLE ELEMENT IN SEQUENCE ##

**Source:** Transmodel

**Definition:** A CONTROLLABLE ELEMENT as a part of a FARE STRUCTURE ELEMENT, including its possible order in the sequence of CONTROLLABLE ELEMENTs grouped together to form that FARE STRUCTURE ELEMENT, and its possible quantitative limitation.

## CONTROLLABLE ELEMENT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a CONTROLLABLE ELEMENT: default total price, discount in value or percentage etc.

## CONTROLLED ACCESS ##

**Source:** Transmodel

**Definition:** A validated use of a CONTROLLABLE ELEMENT.

## CORPORATE PURCHASER ROLE ##

**Source:** Transmodel

**Definition:** The role of purchasing FARE PRODUCTs on behalf of a corporate body such as a company, school, government department, etc.

## COST CENTRE ##

**Source:** Transmodel

**Definition:** A COST CENTRE is a business unit, or other type of classification used by the companyâ€™s accountancy department, to which costs can be collected or attributed according to cost type and origin.

## COUNTRY ##

**Source:** Transmodel

**Definition:** A jurisdictional geographic boundary. A COUNTRY normally has a two character IANA identifier.

## COUPLED JOURNEY ##

**Source:** Transmodel

**Definition:** A complete journey operated by a coupled train, composed of two or more VEHICLE JOURNEYs remaining coupled together all along a JOURNEY PATTERN. A COUPLED JOURNEY may be viewed as a single VEHICLE JOURNEY.

## COURSE OF JOURNEYS ##

**Source:** Transmodel

**Definition:** A part of a BLOCK composed of consecutive VEHICLE JOURNEYs defined for the same DAY TYPE, all operated on the same LINE.

## CREW BASE ##

**Source:** Transmodel

**Definition:** A place where operating employees (e.g. drivers) report on and register their work.

## CROSSING EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT for CROSSING EQUIPMENTs (zebra, pedestrian lights, acoustic device sensors, tactile guide strips, etc.).

## CUSTOMER ACCOUNT ##

**Source:** Transmodel

**Definition:** A registration of the TRANSPORT CUSTOMER with an ACCOUNT PROVIDER to obtain travel services.

## CUSTOMER ACCOUNT ENTRY ##

**Source:** Transmodel

**Definition:** An abstract FARE CONTRACT ENTRY relating to a CUSTOMER ACCOUNT.

## CUSTOMER ACCOUNT EVENT ##

**Source:** Transmodel

**Definition:** An action performed by a TRANSPORT CUSTOMER relating to a CUSTOMER ACCOUNT.

## CUSTOMER ACCOUNT SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of a specific CUSTOMER ACCOUNT on a SECURITY LIST.

## CUSTOMER BOOKING CANCELLATION ENTRY ##

**Source:** Transmodel

**Definition:** A SALES TRANSACTION recording the cancellation of a reservation.

## CUSTOMER BOOKING ENTRY ##

**Source:** Transmodel

**Definition:** A SALES TRANSACTION recording the reservation of an access right.

## CUSTOMER BOOKING EVENT ##

**Source:** Transmodel

**Definition:** The booking or modification of a reservation by a TRANSPORT CUSTOMER, possibly without purchase.

## CUSTOMER COLLECT EVENT ##

**Source:** Transmodel

**Definition:** The collection by the TRANSPORT CUSTOMER of a TRAVEL DOCUMENT and/or MEDIUM ACCESS DEVICE from any FULFILMENT CHANNEL.

## CUSTOMER DEREGISTER EVENT ##

**Source:** Transmodel

**Definition:** The closing of a CUSTOMER ACCOUNT and the removal of all personal details.

## CUSTOMER DEREGISTRATION ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the closing of an account and the clearing from record of all personal details of a TRANSPORT CUSTOMER.

## CUSTOMER ELIGIBILITY ##

**Source:** Transmodel

**Definition:** A parameter indicating whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a specific validity parameter. This may be subject to a particular VALIDITY CONDITION.

## CUSTOMER EXCHANGE EVENT ##

**Source:** Transmodel

**Definition:** The exchange by a TRANSPORT CUSTOMER of a product for another product.

## CUSTOMER FULFILMENT EVENT ##

**Source:** Transmodel

**Definition:** The delivery to a TRANSPORT CUSTOMER of a materialisation of a FARE PRODUCT as a TRAVEL DOCUMENT.

## CUSTOMER MEDIA APPLICATION RESTORE EVENT ##

**Source:** Transmodel

**Definition:** The reinstallation to replacement media of an electronic travel document on a MEDIA DEVICE, usually as a MEDIA APPLICATION, possibly with recovered stored value.

## CUSTOMER MEDIA INSTALL EVENT ##

**Source:** Transmodel

**Definition:** The installation of an electronic travel document on a MEDIA DEVICE, usually as a MEDIA APPLICATION.

## CUSTOMER MEDIA REGISTRATION ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the registration of a media item against a CUSTOMER ACCOUNT, such as an EMV card as a payment method for the account.

## CUSTOMER MEDIA RESTORE EVENT ##

**Source:** Transmodel

**Definition:** The replacement of an electronic MEDIA DEVICE.

## CUSTOMER MODIFY PROFILE EVENT ##

**Source:** Transmodel

**Definition:** The modification by a TRANSPORT CUSTOMER of his CUSTOMER ACCOUNT details.

## CUSTOMER PAYMENT MEANS ##

**Source:** Transmodel

**Definition:** A registered means with which a TRANSPORT CUSTOMER wishes to make payments for a CUSTOMER ACCOUNT, e.g. by nominated EMV card,

## CUSTOMER PRODUCT ACTIVATION EVENT ##

**Source:** Transmodel

**Definition:** The activation of a FARE PRODUCT, e.g. on an installed MEDIA or for a CUSTOMER ACCOUNT.

## CUSTOMER PRODUCT PURCHASE ENTRY ##

**Source:** Transmodel

**Definition:** An abstract SALES TRANSACTION recording a purchase of any sort by a TRANSPORT CUSTOMER.

## CUSTOMER PRODUCT PURCHASE EVENT ##

**Source:** Transmodel

**Definition:** The purchase of a FARE PRODUCT by a TRANSPORT CUSTOMER.

## CUSTOMER PROFILE MODIFICATION ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the updating of a TRANSPORT CUSTOMER's account information.

## CUSTOMER PURCHASE PACKAGE ##

**Source:** Transmodel

**Definition:** A purchase of a SALES OFFER PACKAGE by a TRANSPORT CUSTOMER, giving access rights corresponding to those of one or several FARE PRODUCTs materialised as one or several TRAVEL DOCUMENTs.

## CUSTOMER PURCHASE PACKAGE ELEMENT ##

**Source:** Transmodel

**Definition:** A purchase of a SALES OFFER PACKAGE ELEMENT by a TRANSPORT CUSTOMER, with an indication of all selected parameters.

## CUSTOMER PURCHASE PACKAGE PRICE ##

**Source:** Transmodel

**Definition:** A specialisation of FARE PRICE that defines the price of a CUSTOMER PURCHASE PACKAGE.

## CUSTOMER PURCHASE PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A VALIDITY PARAMETER ASSIGNMENT specifying detailed parameters corresponding to a particular CUSTOMER PURCHASE PACKAGE, chosen from those available for a given fare structure (e.g. the origin or destination zone in a zone-counting system).

## CUSTOMER PURCHASE STATUS ##

**Source:** Transmodel

**Definition:** A classification of possible statuses of CUSTOMER PURCHASE PACKAGE, e.g. booked, paid for, consumed.

## CUSTOMER REFUND EVENT ##

**Source:** Transmodel

**Definition:** The giving of a refund to a TRANSPORT CUSTOMER for a product previously purchased.

## CUSTOMER REGISTER EVENT ##

**Source:** Transmodel

**Definition:** The registration by the TRANSPORT CUSTOMER for a new account.

## CUSTOMER REGISTER MEDIA EVENT ##

**Source:** Transmodel

**Definition:** The registration of a specific MEDIA instance such as an EMV card against a CUSTOMER ACCOUNT.

## CUSTOMER REGISTRATION ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the registration of a CUSTOMER and the creating of a new account.

## CUSTOMER SALES EVENT ##

**Source:** Transmodel

**Definition:** The purchase or subsequent alteration of a FARE PRODUCT by a TRANSPORT CUSTOMER.

## CUSTOMER SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of an specific TRANSPORT CUSTOMER on a SECURITY LIST.

## CUSTOMER SERVICE ##

**Source:** Transmodel

**Definition:** Generic specialisation of LOCAL SERVICE for CUSTOMER SERVICEs (lost properties, meeting point, complaints, etc.).

## CUSTOMER SERVICE PROVIDER ROLE ##

**Source:** Transmodel

**Definition:** The organisation role of providing help line" and similar retail and fulfilment support facilities for CUSTOMERs, including replacement of stolen or damaged customer medium and assistance with the installation of applications. "

## CUSTOMER SERVICE ROLE ##

**Source:** Transmodel

**Definition:** The CUSTOMER SERVICE ROLE is to provide retail and assistance services through multiple channels, and works for a CUSTOMER SERVICE PROVIDER.

## CYCLE STORAGE EQUIPMENT ##

**Source:** Transmodel

**Definition:** A specialisation of PLACE EQUIPMENT describing cycle parking equipment.

## ComparisonOperatorEnum ##

**Source:** Transmodel

**Definition:** Allowed values for Comparison Operator

## DATA COLLECTOR ROLE ##

**Source:** Transmodel

**Definition:** The ADMINISTRATIVE ORGANISATION ROLE of collecting and forwarding data between the various parties concerned with product delivery, such as PRODUCT RETAILER, PRODUCT OWNER etc. May be undertaken by a separate intermediary.

## DATA SOURCE ##

**Source:** Transmodel

**Definition:** The DATA SOURCE identifies the system which has produced the data. References to a data source are useful in an interoperated computer system.

## DATED ARRIVAL ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the arrival to a POINT IN JOURNEY PATTERN in a DATED VEHICLE JOURNEY.

## DATED BLOCK ##

**Source:** Transmodel

**Definition:** The work of a vehicle on a particular OPERATING DAY from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT.

## DATED CALL ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the individual visit to a POINT IN JOURNEY PATTERN in a DATED VEHICLE JOURNEY.

## DATED CALL PART ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the arrival to or the departure from a POINT IN JOURNEY PATTERN in a DATED VEHICLE JOURNEY.

## DATED DEPARTURE ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the departure from a POINT IN JOURNEY PATTERN in a DATED VEHICLE JOURNEY.

## DATED JOURNEY INFORMATION RECORDING ##

**Source:** Transmodel

**Definition:** Possible implementation of LOGGABLE OBJECT designed for recording DATED VEHICLE JOURNEY information

## DATED JOURNEY PART ##

**Source:** Transmodel

**Definition:** A JOURNEY PART taking place on a particular OPERATING DAY.

## DATED PASSING TIME ##

**Source:** Transmodel

**Definition:** A PASSING TIME on a particular OPERATING DAY.

## DATED SPECIAL SERVICE ##

**Source:** Transmodel

**Definition:** A SPECIAL SERVICE taking place on a particular OPERATING DAY. It may derive from a planned SPECIAL SERVICE, or be only occasional.

## DATED VEHICLE JOURNEY ##

**Source:** Transmodel

**Definition:** A particular journey of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff.

## DATED VEHICLE JOURNEY INTERCHANGE ##

**Source:** Transmodel

**Definition:** A VEHICLE JOURNEY INTERCHANGE between two DATED VEHICLE JOURNEYs. It could be created ad-hoc or be based on a planned interchange such as a SERVICE JOURNEY INTERCHANGE, a SERVICE JOURNEY PATTERN INTERCHANGE, or an INTERCHANGE RULE.

## DATED VEHICLE SERVICE ##

**Source:** Transmodel

**Definition:** A VEHICLE SERVICE taking place on a particular OPERATING DAY.

## DATED VEHICLE SERVICE PART ##

**Source:** Transmodel

**Definition:** A VEHICLE SERVICE PART taking place on a particular OPERATING DAY.

## DAY OF WEEK ##

**Source:** Transmodel

**Definition:** A particular week day (from Monday to Sunday).

## DAY TYPE ##

**Source:** Transmodel

**Definition:** A type of day characterised by one or more properties which affect public transport operation. For example: weekday in school holidays.

## DAY TYPE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of operational characteristics, expressed by DAY TYPEs, to particular OPERATING DAYs within a SERVICE CALENDAR.

## DEAD RUN ##

**Source:** Transmodel

**Definition:** A non-service VEHICLE JOURNEY.

## DEAD RUN PATTERN ##

**Source:** Transmodel

**Definition:** A JOURNEY PATTERN to be used for DEAD RUNs.

## DEFAULT CONNECTION ##

**Source:** Transmodel

**Definition:** The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip.   It specifies default times to be used to change from one mode of transport to another at an area or national level as specified by a TOPOGRAPHIC PLACE, STOP AREA or SITE ELEMENT. It may be restricted to a specific MODE or OPERATOR or only apply in a particular direction of transfer, e.g. bus to rail may have a different time for rail to bus.

## DEFAULT CONNECTION END ##

**Source:** Transmodel

**Definition:** One end of a DEFAULT CONNECTION.

## DEFAULT DEAD RUN RUN TIME ##

**Source:** Transmodel

**Definition:** The time taken to traverse a TIMING LINK during a DEAD RUN, for a specified TIME DEMAND TYPE. This time may be superseded by the JOURNEY PATTERN RUN TIME or VEHICLE JOURNEY RUN TIME if these exist.

## DEFAULT INTERCHANGE ##

**Source:** Transmodel

**Definition:** A quality parameter fixing the acceptable duration (standard and maximum) for an INTERCHANGE to be planned between two SCHEDULED STOP POINTs. This parameter will be used to control whether any two VEHICLE JOURNEYs serving those points may be in connection.

## DEFAULT SERVICE JOURNEY RUN TIME ##

**Source:** Transmodel

**Definition:** The default time taken by a vehicle to traverse a TIMING LINK during a SERVICE JOURNEY, for a specified TIME DEMAND TYPE. This time may be superseded by the JOURNEY PATTERN RUN TIME or VEHICLE JOURNEY RUN TIME if these exist.

## DELAY ##

**Source:** Transmodel

**Definition:** A description of deviations from the public transport timetable.

## DELIVERY VARIANT ##

**Source:** Transmodel

**Definition:** A variant text of a NOTICE for use in a specific media or delivery channel (voice, printed material, etc).

## DELTA ##

**Source:** Transmodel

**Definition:** A record of the detailed changes of a given ENTITY IN VERSION from one VERSION to the next one. A DELTA contains pairs of attributes' old values - new values.

## DENY ACCOUNT ON SECURITY LIST EVENT ##

**Source:** Transmodel

**Definition:** The denial of rights by placing an ENTITY on a BLACK LIST and/or removing it from a WHITE LIST.

## DEPARTMENT ##

**Source:** Transmodel

**Definition:** An ORGANIZATION PART specific to a purpose and/or organisational structure.

## DEPARTURE ##

**Source:** Transmodel

**Definition:** A view that brings together data relating to the departure from a POINT IN JOURNEY PATTERN in a VEHICLE JOURNEY.

## DEPARTURE EXCHANGE ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in permuting at one POINT the departure times of two or several DATED VEHICLE JOURNEYs.

## DEPARTURE LAG ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in gradually shifting a set of departures at one POINT. It allows a change of the timetable without abrupt variations in the intervals.

## DESIGN WEEK ##

**Source:** Transmodel

**Definition:** A DESIGN WEEK is a week viewed as a part of a ROSTER DESIGN with a specified order in that design.

## DESIGN WEEK ELEMENT ##

**Source:** Transmodel

**Definition:** A DESIGN WEEK ELEMENT is an element of a DESIGN WEEK representing a particular DAY OF WEEK designating if it is a day of rest or work according to a specific DUTY TYPE for a theoretically available driver.

## DESTINATION DISPLAY ##

**Source:** Transmodel

**Definition:** An advertised destination of a specific JOURNEY PATTERN, usually displayed on a headsign or at other on-board locations.

## DESTINATION DISPLAY VARIANT ##

**Source:** Transmodel

**Definition:** An advertised destination of a specific JOURNEY PATTERN, usually displayed on a headsign or at other on-board locations.

## DETECTED OPERATION ##

**Source:** Transmodel

**Definition:** An actual data detected in a VEHICLE DETECTING event: detection of an actual vehicle coupling, of an INCIDENT, of an actual relief, etc.

## DEVICE PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** An ACCESS RIGHT PARAMETER ASSIGNMENT expressing the location (or other fixed parameters) of a CONTROL MEANS.

## DEVICE RELATED CONTROL MEANS ##

**Source:** Transmodel

**Definition:** A specific device constituting the CONTROL MEANS to control TRAVEL DOCUMENTs.

## DIRECTION ##

**Source:** Transmodel

**Definition:** A classification for the general orientation of ROUTEs.

## DISCOUNTING RULE ##

**Source:** Transmodel

**Definition:** A price calculation rule determined by a discount.

## DISPLAY ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of one SCHEDULED STOP POINT and one JOURNEY PATTERN to a PASSENGER INFORMATION EQUIPMENT specifying that information on the SCHEDULED STOP POINT and the JOURNEY PATTERN will be provided (e.g. displayed, printed).

## DISTANCE MATRIX ELEMENT ##

**Source:** Transmodel

**Definition:** A cell of an origin-destination matrix for TARIFF ZONEs or SCHEDULED STOP POINTs, expressing a fare distance for the corresponding trip: value in km, number of fare units etc.

## DISTANCE MATRIX ELEMENT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a DISTANCE MATRIX ELEMENT: default total price etc.

## DISTRIBUTION ASSIGNMENT ##

**Source:** Transmodel

**Definition:** An assignment of the COUNTRY and/or DISTRIBUTION CHANNEL through which a FARE PRODUCT may or may not be distributed.

## DISTRIBUTION CHANNEL ##

**Source:** Transmodel

**Definition:** A type of outlet for selling of a FARE PRODUCT.

## DRIVER ##

**Source:** Transmodel

**Definition:** A DRIVER is an EMPLOYEE whose usual work is to drive a public transport vehicle.

## DRIVER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A DRIVER ASSIGNMENT is an assignment of an EMPLOYEE to a ROW/DRIVER in a ROSTER MATRIX for a specified OPERATING DAY.

## DRIVER CONTROL ACTION ##

**Source:** Transmodel

**Definition:** A DRIVER CONTROL ACTION is a CONTROL ACTION affecting a LOGICAL DRIVER.

## DRIVER INCIDENT ##

**Source:** Transmodel

**Definition:** An INCIDENT concerning LOGICAL DRIVERs.

## DRIVER ROLE ##

**Source:** Transmodel

**Definition:** The DRIVER ROLE is to drive a VEHICLE. May also perform the ACCESS RIGHT CONTROLLER ROLE.

## DRIVER SCHEDULE FRAME ##

**Source:** Transmodel

**Definition:** A DRIVER SCHEDULE FRAME is a coherent set of DUTies to which the same set of VALIDITY CONDITIONs have been assigned.

## DRIVER TRIP ##

**Source:** Transmodel

**Definition:** A DRIVER TRIP is a planned non-driving movement of a driver within a DUTY PART between two TIMING POINTs that may include using one or several VEHICLE JOURNEYs on vehicles driven by other drivers.

## DRIVER TRIP TIME ##

**Source:** Transmodel

**Definition:** A DRIVER TRIP TIME is the time allowed for a driver to cover a particular DRIVER TRIP during a specified TIME BAND.

## DRIVING SPELL ##

**Source:** Transmodel

**Definition:** A DRIVING SPELL is a continuous period in a STRETCH, during which a driver is on duty in one vehicle.

## DUTY ##

**Source:** Transmodel

**Definition:** A DUTY describes the work to be performed by a driver on a particular DAY TYPE.

## DUTY PART ##

**Source:** Transmodel

**Definition:** A DUTY PART is a continuous part of a driver DUTY during which the driver is under the management of the company and may include BREAKs.

## DUTY TYPE ##

**Source:** Transmodel

**Definition:** A DUTY TYPE is a classification of a DUTY, in terms of working hours within the day.

## DYNAMIC STOP ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The dynamic association of a SCHEDULED STOP POINT (i.e. a SCHEDULED STOP POINT of a SERVICE PATTERN or JOURNEY PATTERN) with the next available STOP PLACE, QUAY or BOARDING POSITION within a STOP PLACE.

## EASEMENT ##

**Source:** Transmodel

**Definition:** A description of temporary (fare) exceptions allowed because of disruptions.

## ELEMENTARY JOURNEY CONTROL ACTION ##

**Source:** Transmodel

**Definition:** A non-composite CONTROL ACTION affecting DATED VEHICLE JOURNEYs.

## EMPLOYEE ##

**Source:** Transmodel

**Definition:** An employee of the public transport company.

## EMPLOYEE ROLE ##

**Source:** Transmodel

**Definition:** The EMPLOYEE ROLE is to work for an organisation providing any aspect of the travel services.

## EMV CARD ##

**Source:** Transmodel

**Definition:** A standardised payment card (Europay MasterCard Visa etc) , capable of being used as token for an ABT system

## ENCUMBRANCE NEED ##

**Source:** Transmodel

**Definition:** A specific USER NEED, i.e. a requirement of a passenger travelling with luggage, animal or any other object requiring special arrangements to access public transport.

## ENTITLEMENT GIVEN ##

**Source:** Transmodel

**Definition:** A parameter indicating whether a particular FARE PRODUCT provides an entitlement to buy or use an access right.

## ENTITLEMENT PRODUCT ##

**Source:** Transmodel

**Definition:** A precondition to access a service or to purchase a FARE PRODUCT issued by an organisation that may not be a PT operator (e.g. military card).

## ENTITLEMENT REQUIRED ##

**Source:** Transmodel

**Definition:** A parameter indicating whether a particular FARE PRODUCT requires an entitlement to by or use an access right.

## ENTITY ##

**Source:** Transmodel

**Definition:** Any data instance to be managed in an operational Version Management System. When several data sources coexist (multimodality and/or interoperability), an ENTITY has to be related to a given DATA SOURCE in which it is defined.

## ENTITY IN VERSION ##

**Source:** Transmodel

**Definition:** The ENTITY associated to a given VERSION.

## ENTRANCE ##

**Source:** Transmodel

**Definition:** A physical entrance or exit to/from a SITE. May be a door, barrier, gate or other recognizable point of access.

## ENTRANCE EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT for ENTRANCEs (door, barrier, revolving door, etc.).

## EQUIPMENT ##

**Source:** Transmodel

**Definition:** An item of equipment installed either fixed (PLACE EQUIPMENT) or on-board vehicles (VEHICLE EQUIPMENT). A service (LOCAL SERVICE such as LEFT LUGGAGE, TICKETING SERVICE) is considered as immaterial equipment as well.

## ENTRANCE FOR PASSENGER SPACE ## 

**Source:** ITxPT

**Definition:** A PASSENGER ENTRANCE used as an entry- and/or exit- point to or from a certain PASSENGER SPACE along with information if the designated exit and entry directions of the PASSENGER ENTRANCE are aligned or reversed in relation to the PASSENGER SPACE.

## EQUIPMENT PLACE ##

**Source:** Transmodel

**Definition:** A SITE COMPONENT containing EQUIPMENT

## EQUIPMENT POSITION ##

**Source:** Transmodel

**Definition:** The precise position within an EQUIPMENT PLACE where particular equipment is placed.

## ESCALATOR EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of STAIR EQUIPMENT for ESCALATORs.

## ESTIMATED PASSING TIME ##

**Source:** Transmodel

**Definition:** A time data, calculated from the latest available input, about when a public transport vehicle will pass a particular POINT IN JOURNEY PATTERN on a specified DATED VEHICLE JOURNEY. These are mainly used to inform passengers about expected times of arrival and/or departure, but may also be used for monitoring and re-planning.

## EVENT ##

**Source:** Transmodel

**Definition:** Any time-stamped event recorded in the system, having some consequences on entities.

## EXCHANGE POINTS DELIVERY ##

**Source:** Transmodel

**Definition:** The result returned by an EXCHANGE POINTS REQUEST.

## EXCHANGE POINTS REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST to find EXCHANGE POINTs.

## EXCHANGE POINTS REQUEST FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the results of the EXCHANGE POINTS REQUEST.

## EXCHANGE POINTS REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used to when finding EXCHANGE POINTs.

## EXCHANGING ##

**Source:** Transmodel

**Definition:** Parameters indicating whether indicating whether and how the access right may be exchanged for another access right.

## EXTRA DATED VEHICLE JOURNEY ##

**Source:** Transmodel

**Definition:** A DATED VEHICLE JOURNEY added to the PRODUCTION PLAN in addition to the long term planned NORMAL DATED VEHICLE JOURNEYs.

## FACILITY ##

**Source:** Transmodel

**Definition:** A named amenity available to the public at a SITE or on a SERVICE. A facility has no further properties other than a name. An EQUIPMENT or LOCAL SERVICE is used to describe the further properties provided as part of particular facility.

## FACILITY CONDITION ##

**Source:** Transmodel

**Definition:** A FACILITY CONDITION describes a changed state of availability for a MONITORED FACILITY

## FACILITY MONITORING METHOD ##

**Source:** Transmodel

**Definition:** A description of the method and circumstances used to monitor a facility such as if it is manual or automatic, the frequency of monitoring or if it is done at certain times. (Named MONITORING INFO in SIRI FM)

## FACILITY OPERATIONAL EVENT ##

**Source:** Transmodel

**Definition:** An OPERATIONAL EVENT concerning a FACILITY.

## FACILITY REQUIREMENT ##

**Source:** Transmodel

**Definition:** A classification of public transport vehicles according to the facilities available on the vehicle.

## FACILITY SET ##

**Source:** Transmodel

**Definition:** Set of FACILITies available for a SERVICE JOURNEY or a JOURNEY PART. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor).

## FACILITY STATUS ##

**Source:** Transmodel

**Definition:** A FACILITY STATUS categorizes the change to availability of the facility, such as being removed, unavailable or only partially available.

## FARE CONTRACT ##

**Source:** Transmodel

**Definition:** A contract with a particular (but possibly anonymous) customer, ruling the consumption of transport services (and joint services). A FARE CONTRACT may be designed for a fixed SALES OFFER PACKAGE (e.g. ticket) or to allow successive purchases of SALES OFFER PACKAGEs.

## FARE CONTRACT ENTRY ##

**Source:** Transmodel

**Definition:** An LOG ENTRY associated with of a FARE CONTRACT.

## FARE CONTRACT EVENT ##

**Source:** Transmodel

**Definition:** An event associated with a FARE CONTRACT.

## FARE CONTRACT SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of an specific FARE CONTRACT on a SECURITY LIST.  .

## FARE CONTRACT STATUS ##

**Source:** Transmodel

**Definition:** A classification of possible status of a CUSTOMER ACCOUNT, e.g. active, suspended, archived, etc.

## FARE DATA COLLECTOR ROLE ##

**Source:** Transmodel

**Definition:** The role of collecting and forwarding fare data between the various parties concerned with product delivery, such as PRODUCT RETAILER, PRODUCT OWNER etc. May be undertaken by a separate intermediary.

## FARE DAY TYPE ##

**Source:** Transmodel

**Definition:** A type of day used in the fare collection domain, characterised by one or more properties which affect the definition of access rights and prices in the fare system.

## FARE DEBIT ##

**Source:** Transmodel

**Definition:** A log entry providing data for a debiting action in case of post-payment or value card debiting.

## FARE DEMAND FACTOR ##

**Source:** Transmodel

**Definition:** A named set of parameters defining a period of travel with a given price, for example off peak, peak, super off peak, etc.

## FARE EASEMENT ##

**Source:** Transmodel

**Definition:** A change to the normal access rights given to PASSENGERS because of a disruption to the network, for example permission for metro ticket holders to use local rail and bus services if the metro is suspended.

## FARE EASEMENT PARAMETER CHANGE ##

**Source:** Transmodel

**Definition:** A change to an access right because of a disruption to the network, expressed in terms of ACCESS RIGHT PARAMETERs.

## FARE ELEMENT IN SEQUENCE ##

**Source:** Transmodel

**Definition:** A part of an access right, including its possible order in the sequence of elementary access rights.

## FARE FRAME ##

**Source:** Transmodel

**Definition:** A set of FARE data elements to which the same VALIDITY CONDITIONs have been assigned.

## FARE FRAME DEFAULTS ##

**Source:** Transmodel

**Definition:** A set of pricing parameters and values to apply to an individual element in the FARE FRAME if no explicit value is specified on the element.

## FARE INTERVAL ##

**Source:** Transmodel

**Definition:** An interval based aspect of the fare structure.

## FARE ORGANISATION ROLE ##

**Source:** Transmodel

**Definition:** Any corporate role in providing or managing transport services.

## FARE POINT IN JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** A POINT IN JOURNEY PATTERN which represents the start or end of a FARE SECTION, or a point used to define a SERIES CONSTRAINT.

## FARE PRICE ##

**Source:** Transmodel

**Definition:** Price features for a PRICEABLE OBJECT.

## FARE PRODUCT ##

**Source:** Transmodel

**Definition:** An immaterial marketable element (access rights, discount rights, etc.), specific to a CHARGING MOMENT.

## FARE PRODUCT ATTRIBUTOR ROLE ##

**Source:** Transmodel

**Definition:** The role of being an agent of a FARE PRODUCT OWNER, i.e. the role of an intermediary organisation to whom certain responsibilities have been delegated by the FARE PRODUCT OWNER, for instance to provide the technical implementation of the products defined by the FARE PRODUCT OWNER.

## FARE PRODUCT DELIVERY ##

**Source:** Transmodel

**Definition:** A specialization of PI DELIVERY that returns details of FARE PRODUCTS.

## FARE PRODUCT DISTRIBUTOR ROLE ##

**Source:** Transmodel

**Definition:** The role, in large networks, of organising and accounting for the wholesale distribution of FARE PRODUCTs, as delegated by the FARE PRODUCT OWNER ROLE and to supply products to the FARE PRODUCT RETAILER ROLE.

## FARE PRODUCT EXCHANGE ENTRY ##

**Source:** Transmodel

**Definition:** A SALES TRANSACTION recording the alteration or exchange of a FARE PRODUCT for another by a TRANSPORT CUSTOMER.

## FARE PRODUCT FILTER ##

**Source:** Transmodel

**Definition:** Parameters controlling the type of fares returned by a FARE FRODUCT REQUEST.

## FARE PRODUCT ISSUER ROLE ##

**Source:** Transmodel

**Definition:** A role of an organisation introduced when there are a large number of fare product owners and a large number of distributors. The FARE PRODUCT ISSUER ROLE makes a portfolio of products available to a product distributor to be sold via product retailers to TRANSPORT CUSTOMERs.

## FARE PRODUCT OWNER ROLE ##

**Source:** Transmodel

**Definition:** The role of the organisation which has commercial ownership of a FARE PRODUCT and is responsible for specifying pricing, usage conditions and commercial rules for the product, for ensuring there are processes for marketing and retailing the product, customer payment, control and validation, back office accounting and settlement and for customer service.

## FARE PRODUCT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a FARE PRODUCT: default total price, discount in value or percentage etc.

## FARE PRODUCT PURCHASE ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER PURCHASE ENTRY recording the purchase of a FARE PRODUCT by a TRANSPORT CUSTOMER.

## FARE PRODUCT REFUND ENTRY ##

**Source:** Transmodel

**Definition:** A SALES TRANSACTION recording a refund given to a TRANSPORT CUSTOMER.

## FARE PRODUCT RENEWAL ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER PRODUCT PURCHASE ENTRY recording the renewal of a FARE PRODUCT such as a pass by a TRANSPORT CUSTOMER.

## FARE PRODUCT REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST to find details about a FARE PRODUCT or SALES OFFER PACKAGE.

## FARE PRODUCT REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used when computing and decorating FARE PRODUCT REQUEST results.

## FARE PRODUCT RETAILER ROLE ##

**Source:** Transmodel

**Definition:** The role of an organisation to sell products to TRANSPORT CUSTOMERs, as authorised by a FARE PRODUCT OWNER ROLE. The FARE PRODUCT RETAILER ROLE may be undertaken by the same party as the FARE PRODUCT OWNER ROLE, the ACCOUNT PROVIDER ROLE, or a secondary outlet such as a TRAVEL AGENT or, newsagent, or other third party, etc.

## FARE PRODUCT SALE DEBIT ##

**Source:** Transmodel

**Definition:** A log entry providing data for a debiting action in case of a FARE PRODUCT purchase, e.g. a product value card debiting.

## FARE PRODUCT VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** A type of SCOPING VALIDITY PARAMETER linked to FARE PRODUCTS and/or their distribution.

## FARE QUOTA FACTOR ##

**Source:** Transmodel

**Definition:** A named set of parameters defining a number of quota fares available of a given denomination.

## FARE REGISTRAR ROLE ##

**Source:** Transmodel

**Definition:** The ADMINISTRATIVE ORGANISATION ROLE of coordinating the issue of unique registration codes (for example, by determining rules for generating unique codes) for data linked to fare management such as FARE CONTRACTs, TRAVEL DOCUMENTs, etc.

## FARE SCHEDULED STOP POINT ##

**Source:** Transmodel

**Definition:** A specialisation of SCHEDULED STOP POINT describing a stop with fare accounting and routing characteristics.

## FARE SECTION ##

**Source:** Transmodel

**Definition:** A subdivision of a JOURNEY PATTERN consisting of consecutive POINTs IN JOURNEY PATTERN, used to define an element of the fare structure.

## FARE SECURITY MANAGER ROLE ##

**Source:** Transmodel

**Definition:** The ADMINISTRATIVE ORGANISATION ROLE of establishing and coordinating a security policy for fare data across the provider organisations, and of the certifying and auditing of organisations, applications, etc for their conformance to the security policy.

## FARE STRUCTURE ELEMENT ##

**Source:** Transmodel

**Definition:** A sequence or set of CONTROLLABLE ELEMENTs to which rules for limitation of access rights and calculation of prices (fare structure) are applied.

## FARE STRUCTURE ELEMENT IN SEQUENCE ##

**Source:** Transmodel

**Definition:** A FARE STRUCTURE ELEMENT as a part of a VALIDABLE ELEMENT, including its possible order in the sequence of FARE STRUCTURE ELEMENTs forming that VALIDABLE ELEMENT, and its possible quantitative limitation.

## FARE STRUCTURE ELEMENT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a FARE STRUCTURE ELEMENT: default total price, discount in value or percentage etc.

## FARE STRUCTURE FACTOR ##

**Source:** Transmodel

**Definition:** A factor influencing access rights definition or calculation of prices.

## FARE TABLE ##

**Source:** Transmodel

**Definition:** A grouping of prices (specialization of PRICE GROUP) that may be associated with all or any of DISTANCE MATRIX ELEMENT, FARE STRUCTURE ELEMENT GEOGRAPHICAL INTERVAL, GROUP OF ACCESS RIGHT PARAMETER, CLASS OF USE, OPERATOR, VEHICLE MODE, FARE PRODUCT.

## FARE TRIP ACTIVATION ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the initiation of the consumption of access rights by a PASSENGER making a trip, for example by means of marking a TRAVEL DOCUMENT using a ticket validator machine.

## FARE UNIT ##

**Source:** Transmodel

**Definition:** A unit associated with a FARE STRUCTURE FACTOR.

## FARE ZONE ##

**Source:** Transmodel

**Definition:** A specialization of TARIFF ZONE to include FARE SECTIONs.

## FC Control & Validation - Control Step ##

**Source:** Transmodel

**Definition:** _No definition in Transmodel source pdf_

## FC Control & Validation - Control Structure ##

**Source:** Transmodel

**Definition:** _No definition in Transmodel source pdf_

## FC Control & Validation - Document Cancellation ##

**Source:** Transmodel

**Definition:** _No definition in Transmodel source pdf_

## FC Control & Validation - Validation ##

**Source:** Transmodel

**Definition:** _No definition in Transmodel source pdf_

## FILL IN TIME ##

**Source:** Transmodel

**Definition:** A FILL IN TIME is a non-productive period of driver time that is the result of the duty cutting procedure or is introduced to prolong a DRIVING SPELL to a minimum length.

## FLEXIBLE AREA ##

**Source:** Transmodel

**Definition:** Specialisation of a FLEXIBLE QUAY (which is abstract) to identify what is the catchment area for a flexible service (so that a stop finder can find the nearest available types of transport). It is a named zone visited by a particular mode of transport. It is part of the SITE data set rather than the service data set, since it can be defined and exists independently of an actual service.

## FLEXIBLE JOURNEY ACTIVATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in activating a DATED VEHICLE JOURNEY that has a booking pre-condition.

## FLEXIBLE LINE ##

**Source:** Transmodel

**Definition:** Specialisation of LINE for flexible service. As all the service on a LINE may not all be flexible, flexibility itself is described at JOURNEY PATTERN level (meaning that a separate JOURNEY PATTERN is needed for each type of flexibility available for the line).    Types of flexible services are :  - Virtual line service  - Flexible service with main route  - Corridor service   - Fixed stop area-wide flexible service  - Free area-wide flexible service  - Mixed types of flexible service  - Mixed type of flexible and regular services

## FLEXIBLE LINK PROPERTIES ##

**Source:** Transmodel

**Definition:** Set of properties describing the flexible characteristics of a LINK.        A composition is used with LINK in order to avoid multiple inheritance and a type explosion of link subtypes

## FLEXIBLE POINT PROPERTIES ##

**Source:** Transmodel

**Definition:** Set of characteristics describing the possible flexibility of POINTs. A composition is used with POINT in order to avoid multiple inheritance.

## FLEXIBLE QUAY ##

**Source:** Transmodel

**Definition:** A physical ZONE such as a section of a road where a flexible service is available on demand.  The existence of the zone makes the services visible to journey planners looking for available services for an area.

## FLEXIBLE ROUTE ##

**Source:** Transmodel

**Definition:** Specialisation of ROUTE for flexible service. May include both point and zonal areas and ordered and unordered sections.

## FLEXIBLE SERVICE PROPERTIES ##

**Source:** Transmodel

**Definition:** Additional characteristics of flexible service. A service may be partly fixed, partly flexible.

## FLEXIBLE STOP ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The allocation of a SCHEDULED STOP POINT (i.e. a STOP POINT of a SERVICE PATTERN or JOURNEY PATTERN) to a specific FLEXIBLE STOP PLACE, and also possibly a FLEXIBLE AREA or HAIL AND RIDE AREA. May be subject to a VALIDITY CONDITION.

## FLEXIBLE STOP PLACE ##

**Source:** Transmodel

**Definition:** A specialisation of the STOP PLACE describing a stop of a FLEXIBLE SERVICE. It may be composed of FLEXIBLE AREAs or HAIL AND RIDE AREAs identifying the catchment areas for flexible services (when they use areas or flexible quays). Some FLEXIBLE SERVICE also use regular STOP PLACEs for their stops. When assigned to a SCHEDULED STOP POINT the corresponding SCHEDULED STOP POINT is supposed to be a ZONE (the centroid point of the ZONE being the SCHEDULED STOP POINT).

## FREQUENCY OF USE ##

**Source:** Transmodel

**Definition:** The limits of usage frequency for a FARE PRODUCT (or one of its components) or a SALES OFFER PACKAGE during a specific VALIDITY PERIOD. There may be different prices depending on how often the right is consumed during the period.

## FULFILMENT ENTRY ##

**Source:** Transmodel

**Definition:** An abstract FARE CONTRACT ENTRY relating to delivery of a purchase.

## FULFILMENT METHOD ##

**Source:** Transmodel

**Definition:** The means by which the TRAVEL DOCUMENT is delivered to the TRANSPORT CUSTOMER, e.g. online, collection, etc.

## FULFILMENT METHOD PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a FULFILMENT METHOD default total price etc.

## GARAGE ##

**Source:** Transmodel

**Definition:** A facility used for parking and maintaining vehicles. PARKING POINTs in a GARAGE are called GARAGE POINTs.

## GARAGE POINT ##

**Source:** Transmodel

**Definition:** A subtype of PARKING POINT located in a GARAGE.

## GENERAL EVENT ##

**Source:** Transmodel

**Definition:** Conrete class for generic events

## GENERAL FRAME ##

**Source:** Transmodel

**Definition:** Set of data containing information, to which the same VALIDITY CONDITIONs have been assigned.

## GENERAL OBSERVER ROLE ##

**Source:** Transmodel

**Definition:** The general role of observing the passenger information

## GENERAL SECTION ##

**Source:** Transmodel

**Definition:** A specifc ordered sequence of POINTs or LINKs.

## GENERAL SIGN ##

**Source:** Transmodel

**Definition:** Specialisation of SIGN EQUIPMENT which are not HEADING SIGNs nor PLACE SIGNs.

## GENERIC PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A VALIDITY PARAMETER ASSIGNMENT specifying generic access rights for a class of products (e.g. a time band limit - 7 to 10 a.m. - for trips made with a student pass).

## GEOGRAPHICAL INTERVAL ##

**Source:** Transmodel

**Definition:** A geographical interval specifying access rights for the FARE STRUCTURE ELEMENTs within the range of this interval: 0-5 km, 4-6 zones etc.

## GEOGRAPHICAL INTERVAL PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a GEOGRAPHICAL INTERVAL: default total price, etc.

## GEOGRAPHICAL STRUCTURE FACTOR ##

**Source:** Transmodel

**Definition:** The value of a GEOGRAPHICAL INTERVAL or a DISTANCE MATRIX ELEMENT expressed by a GEOGRAPHICAL UNIT.

## GEOGRAPHICAL UNIT ##

**Source:** Transmodel

**Definition:** A unit for calculating geographical graduated fares.

## GEOGRAPHICAL UNIT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a GEOGRAPHICAL UNIT: default total price etc.

## GROUP MEMBER ROLE ##

**Source:** Transmodel

**Definition:** The role of a passenger travelling under the access rights granted by a GROUP TICKET.

## GROUP OF DISTANCE MATRIX ELEMENTS ##

**Source:** Transmodel

**Definition:** A grouping of DISTANCE MATRIX ELEMENTS. May be used to provide reusable Origin / Destination pairs (and associate them a PRICE).

## GROUP OF DISTRIBUTION CHANNELS ##

**Source:** Transmodel

**Definition:** A grouping of DISTRIBUTION CHANNELs.

## GROUP OF ENTITIES ##

**Source:** Transmodel

**Definition:** A set of ENTITies grouped together according to a PURPOSE OF GROUPING, e.g. grouping of stops known to the public by a common name.

## GROUP OF LINES ##

**Source:** Transmodel

**Definition:** A grouping of lines which will be commonly referenced for a specific purpose.

## GROUP OF LINK SEQUENCES ##

**Source:** Transmodel

**Definition:** A grouping of LINK SEQUENCEs.

## GROUP OF LINKS ##

**Source:** Transmodel

**Definition:** A grouping of LINKs. E.g. one GROUP OF LINKs may be managed by a same AUTHORITY.

## GROUP OF OPERATORS ##

**Source:** Transmodel

**Definition:** A group of OPERATORs having for instance common schemes for fare collection or passenger information.

## GROUP OF POINTS ##

**Source:** Transmodel

**Definition:** A grouping of POINTs of a certainTYPE OF POINT and dedicated to a FUNCTIONAL PURPOSE.

## GROUP OF SALES OFFER PACKAGES ##

**Source:** Transmodel

**Definition:** A grouping of SALES OFFER PACKAGEs.

## GROUP OF SERVICES ##

**Source:** Transmodel

**Definition:** A group of SERVICEs, often known to its users by a name or a number.

## GROUP OF TIMEBANDS ##

**Source:** Transmodel

**Definition:** A grouping of TIME BANDs.

## GROUP OF TIMING LINKS ##

**Source:** Transmodel

**Definition:** A set of TIMING LINKs grouped together according to the similarity of TIME BANDs which are relevant to them. There may be a GROUP OF TIMING LINKS which covers all TIMING LINKs, for use when different GROUPs OF TIMING LINKS are not needed.

## GROUP TICKET ##

**Source:** Transmodel

**Definition:** The number and characteristics of persons entitled to travel in addition to the holder of an access right.

## HAIL AND RIDE AREA ##

**Source:** Transmodel

**Definition:** Specialisation of a FLEXIBLE QUAY to identify what is the catchment zone for a hail and ride service (so that a stop finder can find the nearest available types of transport). It is a named zone visited by a particular mode of transport and may be designated by a start point and end point on the road     It is part of the Site data set rather than the service data set, since it can be defined and exists indepently of an actual service.

## HEADING SIGN ##

**Source:** Transmodel

**Definition:** Specialisation of SIGN EQUIPMENT for headings providing information like direction name, line name, etc.

## HEADWAY INTERVAL ##

**Source:** Transmodel

**Definition:** A time interval or a duration defining a headway period and characterizing HEADWAY JOURNEY GROUP (e.g. every 10 min, every 4-6 min).

## HEADWAY JOURNEY GROUP ##

**Source:** Transmodel

**Definition:** A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN having the same HEADWAY INTERVAL between a specified start and end time (for example, every 10 min). This is especially useful for passenger information.

## HIRE SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of LOCAL SERVICE dedicated to hire services (e.g. cycle hire, car hire).

## IDENTITY PROVIDER ROLE ##

**Source:** Transmodel

**Definition:** The role of supplying a trusted identity token that can be associated with a CUSTOMER ACCOUNT, TRAVEL DOCUMENT, etc.  The IDENTITY PROVIDER ROLE may be undertaken by transport AUTHORITies and OPERATORs , but also non-transport organisations such as governments central and local, mobile network operators, or online service providers (e,g. Google, Facebook) and banks.

## IMPEDED TIME ##

**Source:** Transmodel

**Definition:** The difference between the impeded and non-impeded passage of a LINK. It consists of slow down time, waiting time, and accelerating time.

## IMPOSSIBLE MANOEUVRE ##

**Source:** Transmodel

**Definition:** A specification of impossible move for a certain type of vehicle. It specifies from which INFRASTRUCTURE LINK to which other (adjacent) INFRASTRUCTURE LINK a certain VEHICLE TYPE cannot proceed, due to physical restrictions.

## INCIDENT ##

**Source:** Transmodel

**Definition:** An unforeseen EVENT influencing the operation of the network.

## INDIVIDUAL PASSENGER ROLE ##

**Source:** Transmodel

**Definition:** The role of a passenger consuming a travel service as a single individual.

## INDIVIDUAL PURCHASER ROLE ##

**Source:** Transmodel

**Definition:** The role of a person in purchasing a FARE PRODUCT as a private individual. Often, but not necessarily the same as the PASSENGER ROLE.

## INFRASTRUCTURE FRAME ##

**Source:** Transmodel

**Definition:** A set of infrastructure network data (and other data logically related to these) to which the same VALIDITY CONDITIONs have been assigned.

## INFRASTRUCTURE LINK ##

**Source:** Transmodel

**Definition:** A super-type including all LINKs of the physical network (e.g. RAILWAY ELEMENT).

## INFRASTRUCTURE POINT ##

**Source:** Transmodel

**Definition:** A super-type including all POINTs of the physical network (e.g. RAILWAY JUNCTION).

## INSTALLED EQUIPMENT ##

**Source:** Transmodel

**Definition:** An item of equipment either fixed (PLACE EQUIPMENT) or on board i.e. associated with vehicles. This equipment is materialised as opposed to a service (LOCAL SERVICE) considered as an immaterial equipment.

## INSUFFICIENT ACCESS RIGHTS ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the result of the comparison between one or several CONTROL ENTRies and the theoretical access rights attached to the TRAVEL DOCUMENT controlled, detecting insufficient rights to

## INTERCHANGE ##

**Source:** Transmodel

**Definition:** The scheduled possibility for transfer of passengers at the same or different SCHEDULED STOP POINTs.

## INTERCHANGE CANCELLATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in deleting a DATED VEHICLE JOURNEY INTERCHANGE from the latest valid plan so that a distributor DATED VEHICLE JOURNEY no longer needs to wait for a feeder DATED VEHICLE JOURNEY.

## INTERCHANGE CONTROL ACTION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION affecting a DATED VEHICLE JOURNEY INTERCHANGE.

## INTERCHANGE CREATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in adding a completely new DATED VEHICLE JOURNEY INTERCHANGE between a feeder DATED VEHICLE JOURNEY and a distributor DATED VEHICLE JOURNEY to the latest valid plan.

## INTERCHANGE MODIFICATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION expressing that the duration a distributor DATED VEHICLE JOURNEY needs to wait for a feeder DATED VEHICLE JOURNEY in a DATED VEHICLE JOURNEY INTERCHANGE is changed or that a different DATED VEHICLE JOURNEY is to wait for the feeder.

## INTERCHANGE RULE ##

**Source:** Transmodel

**Definition:** Conditions for considering JOURNEYs to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE.

## INTERCHANGE RULE PARAMETER ##

**Source:** Transmodel

**Definition:** Assignment of parameters characterising an INTERCHANGE RULE.

## INTERCHANGE RULE TIMING ##

**Source:** Transmodel

**Definition:** Timings for an INTERCHANGE RULE for a given TIME DEMAND TYPE or TIME BAND.

## INTERCHANGE STATUS ##

**Source:** Transmodel

**Definition:** The information about the actual status of a SERVICE JOURNEY INTERCHANGE on a specified OPERATING DAY. Recorded information on missed interchanges may be of particular interest.

## INTERCHANGING ##

**Source:** Transmodel

**Definition:** Parameters expressing limitations on making changes within a trip.

## JOURNEY ##

**Source:** Transmodel

**Definition:** Common properties of VEHICLE JOURNEYs and SPECIAL SERVICEs, e.g. their link to accounting characteristics.

## JOURNEY ACCOUNTING ##

**Source:** Transmodel

**Definition:** Parameters characterizing VEHICLE JOURNEYs or SPECIAL SERVICEs used for accounting purposes in particular in contracts between ORGANISATIONs.

## JOURNEY CANCELLATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in deleting a DATED VEHICLE JOURNEY from the latest valid plan.

## JOURNEY CREATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in adding a completely new DATED VEHICLE JOURNEY to the latest valid plan.

## JOURNEY FREQUENCY GROUP ##

**Source:** Transmodel

**Definition:** A group of JOURNEYs defined in order to describe special behaviour like frequency based services or rhythmical services (runs all xxh10, xxh25 and xxh45... for example; this is especially useful for passenger information).

## JOURNEY HEADWAY ##

**Source:** Transmodel

**Definition:** Headway interval information that is available for all the VEHICLE JOURNEYs running on the JOURNEY PATTERN for a given TIME DEMAND TYPE, at a given TIMING POINT. This is a default value that can be superseded by VEHICLE JOURNEY HEADWAY. This information must be consistent with HEADWAY JOURNEY GROUP if available (HEADWAY JOURNEY GROUP being a more detailed way of describing headway services).

## JOURNEY LAYOVER ##

**Source:** Transmodel

**Definition:** Time allowance at the end of each journey to allow for delays and for other purposes.

## JOURNEY MEETING ##

**Source:** Transmodel

**Definition:** A time constraint for one or several SERVICE JOURNEYs fixing interchanges between them and/or an external event (e.g. arrival or departure of a feeder line, opening time of the theatre, etc.).

## JOURNEY PART ##

**Source:** Transmodel

**Definition:** A part of a VEHICLE JOURNEY created according to a specific functional purpose, for instance in situations when vehicle coupling or separating occurrs.

## JOURNEY PART COUPLE ##

**Source:** Transmodel

**Definition:** Two JOURNEY PARTs of different VEHICLE JOURNEYs served simultaneously by a train set up by coupling their single vehicles.

## JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles.A JOURNEY PATTERN may pass through the same POINT more than once. The first point of a JOURNEY PATTERN is the origin. The last point is the destination.

## JOURNEY PATTERN HEADWAY ##

**Source:** Transmodel

**Definition:** Headway interval information that is available for all the VEHICLE JOURNEYs running on the JOURNEY PATTERN. This is a default value that can be superseded by the VEHICLE JOURNEY HEADWAY on a specific journey. This information must be consistent with HEADWAY JOURNEY GROUP if available (HEADWAY JOURNEY GROUP being a more detailed way of describing headway services).

## JOURNEY PATTERN LAYOVER ##

**Source:** Transmodel

**Definition:** Time allowance at the end of each journey on a specified JOURNEY PATTERN, to allow for delays and for other purposes. This layover supersedes any global layover and may be superseded by a specific VEHICLE JOURNEY LAYOVER.

## JOURNEY PATTERN RUN TIME ##

**Source:** Transmodel

**Definition:** The time taken to traverse a TIMING LINK in a particular JOURNEY PATTERN, for a specified TIME DEMAND TYPE. If it exists, it will override the DEFAULT SERVICE JOURNEY RUN TIME and DEFAULT DEAD RUN RUN TIME.

## JOURNEY PATTERN WAIT TIME ##

**Source:** Transmodel

**Definition:** The time a vehicle has to wait at a specific TIMING POINT IN JOURNEY PATTERN, for a specified TIME DEMAND TYPE. This

## JOURNEY RUN TIME ##

**Source:** Transmodel

**Definition:** The time taken to traverse a TIMING LINK in a particular JOURNEY PATTERN, for a specified TIME DEMAND TYPE. If it exists, it will override the DEFAULT SERVICE JOURNEY RUN TIME and DEFAULT DEAD RUN RUN TIME.

## JOURNEY TIMING ##

**Source:** Transmodel

**Definition:** A time-related information referring to journey timing whose value depends on the time of use and so can be associated with a TIME DEMAND TYPE, TIME BAND or OPERATIONAL CONTEXT.

## JOURNEY WAIT TIME ##

**Source:** Transmodel

**Definition:** The time a vehicle has to wait at a specific TIMING POINT IN JOURNEY PATTERN, for a specified TIME DEMAND TYPE.This wait time can be superseded by a VEHICLE JOURNEY WAIT TIME.

## LAYER ##

**Source:** Transmodel

**Definition:** A user-defined GROUP OF ENTITies, specified for a particular functional purpose, associating data referring to a particular LOCATING SYSTEM.

## LEFT LUGGAGE SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of CUSTOMER SERVICE for left luggage (provides left luggage information like self service locker, locker free, etc.).

## LEG ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN corresponding to the movement of a user in a single vehicle, or a pedestrian mode such as walking.

## LEG TRACK ##

**Source:** Transmodel

**Definition:** The spatial projection of the leg as set of coordinate points for a specific purpose., such as displaying it on a map.

## LEVEL ##

**Source:** Transmodel

**Definition:** An identified storey (ground, first, basement, mezzanine, etc) within an interchange building or SITE on which SITE COMPONENTs reside. A PATH LINK may connect components on different levels.

## LIFT EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT for LIFTs (provides lift characteristics like depth, maximum load, etc.).

## LIMITING RULE ##

**Source:** Transmodel

**Definition:** A rule for limiting the results of a price calculation.

## LINE ##

**Source:** Transmodel

**Definition:** A group of ROUTEs which is generally known to the public by a similar name or number.

## LINE NETWORK ##

**Source:** Transmodel

**Definition:** The topological structure of a NETWORK as a graph of LINE SECTIONs. This allows the branches and loops of a LINE to be described as a whole.

## LINE SECTION ##

**Source:** Transmodel

**Definition:** A part of a NETWORK comprising an edge between two nodes. Not directional.

## LINE SHAPE ##

**Source:** Transmodel

**Definition:** The graphical shape of a LINK obtained from a formula or other means, using the LOCATION of its limiting POINTs and depending on the LOCATING SYSTEM used for the graphical representation.

## LINK ##

**Source:** Transmodel

**Definition:** An oriented spatial object of dimension 1 with view to the overall description of a network, describing a connection between two POINTs.

## LINK IN LINK SEQUENCE ##

**Source:** Transmodel

**Definition:** The order of a LINK in a LINK SEQUENCE to which it belongs.

## LINK PROJECTION ##

**Source:** Transmodel

**Definition:** An oriented correspondence from one LINK of a source layer, onto an entity in a target layer: e.g. LINK SEQUENCE, COMPLEX FEATURE, within a defined TYPE OF PROJECTION.

## LINK SEQUENCE ##

**Source:** Transmodel

**Definition:** An ordered sequence either of POINTs or of LINKs, defining a path through the network.

## LOCAL SERVICE ##

**Source:** Transmodel

**Definition:** A named service relating to the use of the SITE or transport services at a particular location, for example porterage, assistance for disabled users, booking offices etc. The service may have a VALIDITY CONDITION associated with it. A LOCAL SERVICE is treated as a form of immaterial EQUIPMENT.

## LOCATED EVENT ##

**Source:** Transmodel

**Definition:** An EVENT with additional location and timing information

## LOCATING SYSTEM ##

**Source:** Transmodel

**Definition:** The system used as reference for location and graphical representation of the network and other spatial objects.

## LOCATION ##

**Source:** Transmodel

**Definition:** The position of a POINT with a reference to a given LOCATING SYSTEM (e. g. coordinates).

## LOCATION DELIVERY ##

**Source:** Transmodel

**Definition:** A specialization of PI DELIVERY to make one or more LOCATION REQUESTs.

## LOCATION GEOMETRY RESTRICTION ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the spatial results of the LOCATION REQUEST.

## LOCATION PLACE FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the PLACE related results of the LOCATION REQUEST.

## LOCATION REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST to find a stop.

## LOCATION REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used to when finding and decorating trip stops.

## LOG ##

**Source:** Transmodel

**Definition:** A Collection of LOG ENTRIES grouped together in a file or any other kind of storage.

## LOG ENTRY ##

**Source:** Transmodel

**Definition:** A time-stamped record of an event or change of state.

## LOGGABLE OBJECT ##

**Source:** Transmodel

**Definition:** An entity for which LOG ENTRies may be made..

## LOGICAL DISPLAY ##

**Source:** Transmodel

**Definition:** A set of data that can be assembled for assignment to a physical PASSENGER INFORMATION EQUIPMENT or to a logical channel such as web or media. It is independent of any physical embodiment.   A LOGICAL DISPLAY may have a set of DISPLAY ASSIGNMENTS each of which associates a  JOURNEY PATTERN whose journeys are to be shown at the LOGICAL DISPLAY. It may also be associated with a SCHEDULED STOP POINT. A LOGICAL DISPLAY corresponds to a SIRI STOP MONITORING point.

## LOGICAL DRIVER ##

**Source:** Transmodel

**Definition:** A theoretically available driver resource for an OPERATING DAY, foreseen to be monitored.

## LOGICAL DRIVER CANCELLATION ##

**Source:** Transmodel

**Definition:** A LOGICAL DRIVER CANCELLATION is a CONTROL ACTION consisting in removing a LOGICAL DRIVER from the production plan.

## LOGICAL DRIVER CREATION ##

**Source:** Transmodel

**Definition:** A LOGICAL DRIVER CREATION is a CONTROL ACTION consisting in creating a completely new LOGICAL DRIVER and assigning dated spells to this LOGICAL DRIVER.

## LOGICAL VEHICLE ##

**Source:** Transmodel

**Definition:** A theoretically available vehicle resource for an OPERATING DAY, foreseen to be monitored.

## LOGICAL VEHICLE CANCELLATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in removing a LOGICAL VEHICLE from the production plan.

## LOGICAL VEHICLE CREATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in creating a completely new LOGICAL VEHICLE and assigning DATED VEHICLE JOURNEYs to the new LOGICAL VEHICLE.

## LOST PROPERTY SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of CUSTOMER SERVICE for lost properties.

## LUGGAGE ALLOWANCE ##

**Source:** Transmodel

**Definition:** The number and characteristics (weight, volume) of luggage that a holder of an access right is entitled to carry.

## LUGGAGE LOCKER EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of STOP PLACE EQUIPMENT for luggage lockers.

## LUGGAGE SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of CUSTOMER SERVICE for luggage services (provides luggage service facilites and characteristics like luggage trolley, free to use, etc.).

## LogicalOperatorEnum ##

**Source:** Transmodel

**Definition:** Allowed values for Comparison Operator

## MANAGEMENT AGENT ##

**Source:** Transmodel

**Definition:** Specialisation of ORGANISATION for MANAGEMENT AGENTs.

## MANOEUVRING REQUIREMENT ##

**Source:** Transmodel

**Definition:** A classification of requirements for a public transport VEHICLE according to the Maneuvering capabilities of the vehicle.

## MEAN INTERCHANGE TIME ##

**Source:** Transmodel

**Definition:** An estimated value of the mean time to make an INTERCHANGE, used to inform passengers on the mean duration of trips. May be derived from low level breakdown.

## MEAN PASSENGER WAIT TIME ##

**Source:** Transmodel

**Definition:** An estimated mean waiting time for a passenger at a SCHEDULED STOP POINT, used to calculate the approximate duration of a trip.This value is estimated from the mean interval between vehicles on a JOURNEY PATTERN or a COMMON SECTION.

## MEAN RUN TIME ##

**Source:** Transmodel

**Definition:** An estimated value of the mean run time on a TIMING LINK, used to inform passengers on the mean duration of trips.

## MEDIA APPLICATION RESTORE ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the reinstallation of a previously purchased application on a MEDIA ACCESS DEVICE, possibly with the recovery of value.

## MEDIA PRODUCT ACTIVATION ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the activation of a previously purchased or installed product. Might for example also involve placing on a WHITE LIST.

## MEDIA PRODUCT DEACTIVATION ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the deactivation of a previously purchased or installed product.

## MEDIA PRODUCT INSTALLATION ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the installation of a previously purchased product on a MEDIA ACCESS DEVICE.

## MEDIA PROVIDER ROLE ##

**Source:** Transmodel

**Definition:** The role of supplying the media used for the TRAVEL DOCUMENT, that is a physical support containing a machine readable/writable data/processor application. This can include transport industry smartcards, payment industry contactless cards, public sector issued cards, mobile phones or paper (for barcodes), new formats such as watches and key fobs, and NFC enabled devices.

## MEDIA RECHARGE PURCHASE ENTRY ##

**Source:** Transmodel

**Definition:** A SALES TRANSACTION recording the purchase of a recharge of stored value by a TRANSPORT CUSTOMER.

## MEDIA RESTORE ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the replacement of the MEDIUM ACCESS DEVICE.

## MEDICAL NEED ##

**Source:** Transmodel

**Definition:** A specific USER NEED, i.e. a requirement of a passenger as regards medical constraint (e.g. allergy) to access public transport .

## MEDIUM ACCESS DEVICE ##

**Source:** Transmodel

**Definition:** A component (mobile phone, smart card, etc) with the necessary facilities (hardware and software) to host a MEDIUM APPLICATION INSTANCE and communicate with a control device.

## MEDIUM ACCESS DEVICE SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of an specific MEDIUM ACCESS DEVICE on a SECURITY LIST.

## MEDIUM APPLICATION INSTANCE ##

**Source:** Transmodel

**Definition:** Initialized instance of a software application that runs on a MEDIUM ACCESS DEVICE.

## MEDIUM APPLICATION OWNER ROLE ##

**Source:** Transmodel

**Definition:** For media-centric products, the APPLICATION OWNER ROLE has commercial ownership of the software MEDIA APPLICATION hosting a product and is contracted by the PRODUCT OWNER for the use of the application with the customer.

## MEDIUM APPLICATION PROVIDER ROLE ##

**Source:** Transmodel

**Definition:** For media-centric products, the APPLICATION PROVIDER supplies the software application that hosts a TRAVEL DOCUMENT and presents it to CONTROL DEVICEs for automatic control and validation.

## MEETING POINT SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of CUSTOMER SERVICE for meeting points (provides characteristics like description, label, etc.).

## MEETING RESTRICTION ##

**Source:** Transmodel

**Definition:** A pair of INFRASTRUCTURE LINKs where vehicles of specified VEHICLE TYPEs are not allowed to meet.

## MESSAGE ##

**Source:** Transmodel

**Definition:** A communicated information.

## MESSAGE PART ##

**Source:** Transmodel

**Definition:** A partial or complete information adapted for a specific type of usage and type of media.

## MESSAGE PRIORITY ##

**Source:** Transmodel

**Definition:** An arbitrary rating of how a MESSAGE ranks in relation to other potentially conflicting MESSAGEs when presentation bandwidth is limited.

## MESSAGE REQUEST FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the results of the SITUATION REQUEST.

## METHOD OF BOOKING ##

**Source:** Transmodel

**Definition:** A method by which a booking or reservation may be made, e.g. on line, telephone, in person, etc.,

## METHOD OF CAPTURE ##

**Source:** Transmodel

**Definition:** A classification of the method used to acquire knowledge of the deviation or incident.

## MINIMUM STAY ##

**Source:** Transmodel

**Definition:** Parameters expressing details of any minimum stay at the destination required to use an access right.

## MIXED TRIP ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN from one PLACE of any sort to another. A MIXED TRIP may consist of two or more consecutive LEGs of both PT and non PT modes, having some common characteristics.

## MOBILE DEVICE ##

**Source:** Transmodel

**Definition:** A mobile device (mobile phone, tablet, etc) with the necessary facilities (hardware and software) to host a MEDIUM APPLICATION INSTANCE and communicate with a control device.

## MOBILITY NEED ##

**Source:** Transmodel

**Definition:** A specific USER NEED, i.e. a constraint of a passenger as regards his mobility, e.g. wheelchair, assisted wheelchair, etc.

## MODE ##

**Source:** Transmodel

**Definition:** Any means of transport.

## MONEY SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of LOCAL SERVICE dedicated to money services.

## MONITORED FACILITY ##

**Source:** Transmodel

**Definition:** A monitored FACILITY that may have different states of availability.

## MONITORED JOURNEY PART FACILITY ##

**Source:** Transmodel

**Definition:** A monitored named amenity or capability enhancing a JOURNEY PART.

## MONITORED LEG ##

**Source:** Transmodel

**Definition:** A part of a MONITORED TRIP PATTERN corresponding to the movement of a user in a single vehicle, or a pedestrian mode such as walking.

## MONITORED LEG ARRIVAL ##

**Source:** Transmodel

**Definition:** A view that brings together data to present to a passenger making a specific MONITORED TRIP relating to the arrival at a POINT IN JOURNEY PATTERN of a DATED VEHICLE JOURNEY.

## MONITORED LEG CALL ##

**Source:** Transmodel

**Definition:** Data to present to a passenger making a specific MONITORED TRIP relating to the status of a individual visit by a VEHICLE JOURNEY to a POINT IN JOURNEY PATTERN. May be for origin, destination , and intermediate points.

## MONITORED LEG CALL PART ##

**Source:** Transmodel

**Definition:** A view that brings together data to present to a passenger making a specific MONITORED TRIP relating to the arrival to or the departure from a POINT IN JOURNEY PATTERN in a DATED VEHICLE JOURNEY.

## MONITORED LEG DEPARTURE ##

**Source:** Transmodel

**Definition:** A view that brings together data to present to the passenger making a specific MONITORED TRIP relating to the departure from a POINT IN JOURNEY PATTERN in a DATED VEHICLE JOURNEY.

## MONITORED LEG PROGRESS ##

**Source:** Transmodel

**Definition:** The relative progress of a passenger along a LEG.

## MONITORED LOCAL SERVICE FACILITY ##

**Source:** Transmodel

**Definition:** A monitored named amenity or capability related to a LOCAL SERVICE.

## MONITORED OPERATION ##

**Source:** Transmodel

**Definition:** An operational data monitored in a VEHICLE MONITORING event (e.g. monitoring a LOGICAL VEHICLE, coupled to others, as operating a planned TRAIN BLOCK).

## MONITORED PLACE EQUIPMENT FACILITY ##

**Source:** Transmodel

**Definition:** A monitored named amenity or capability related to a PLACE EQUIPMENT.

## MONITORED SPECIAL SERVICE ##

**Source:** Transmodel

**Definition:** A special service that is monitored as being operated by a LOGICAL VEHICLE.

## MONITORED TRIP ##

**Source:** Transmodel

**Definition:** A part of a MONITORED TRIP PATTERN corresponding to the movement of a passenger from one PLACE of any sort to another in any one mode.

## MONITORED TRIP PATTERN ##

**Source:** Transmodel

**Definition:** A monitored passenger movement from an origin to a destination PLACE, consisting of one or more MONITORED LEGs undertaken in sequence.

## MONITORED VEHICLE EQUIPMENT FACILITY ##

**Source:** Transmodel

**Definition:** A monitored named amenity or capability enabled by ACTUAL VEHICLE EQUIPMENT.

## MONITORED VEHICLE JOURNEY ##

**Source:** Transmodel

**Definition:** A journey that is monitored as being operated by a LOGICAL VEHICLE. According to the monitoring system capabilities, a MONITORED VEHICLE JOURNEY may be related to a DATED VEHICLE JOURNEY, or only to a JOURNEY PATTERN.

## MONITORED VEHICLE JOURNEY FACILITY ##

**Source:** Transmodel

**Definition:** A monitored named amenity or capability enhancing a VEHICLE JOURNEY.

## MONTH VALIDITY OFFSET ##

**Source:** Transmodel

**Definition:** Days before (negative) or after (positive) the start of the month that a product with a calendar period driven activation becomes valid.

## NAVIGATION PATH ##

**Source:** Transmodel

**Definition:** A designated path between two places. May include an ordered sequence of PATH LINKs.

## NAVIGATION PATH ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The allocation of a NAVIGATION PATH to a specific STOP POINT ASSIGNMENT, for example to indicate the path to be taken to make a CONNECTION

## NETWORK ##

**Source:** Transmodel

**Definition:** A named grouping of LINEs under which a transport network is known.

## NETWORK VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** A type of VALIDITY PARAMETER related to the network structure.

## NO ACCESS RIGHTS ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the detection of a TRANSPORT CUSTOMER travelling without having purchased access rights

## NO CHECK IN DETECTED ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the detection that a passenger has failed to check in at the end of a journey. This may be triggered by a subsequent check in or by back office processes looking for unmatched waypoint check in and check out events within a specified window.

## NO CHECK OUT DETECTED ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the detection that a passenger has failed to check out at the end of a journey. This may be triggered by a subsequent check in or by back office processes looking for unmatched check in and check out events within a specified window.

## NO PROOF ON PERSON ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the detection of a customer who claims to have purchased access rights but has no proof, e.g. TRAVEL DOCUMENT on their person.

## NON-DRIVING SPELL ##

**Source:** Transmodel

**Definition:** A NON DRIVING SPELL is a continuous period in a STRETCH when a driver is performing some non-driving TASK or waiting on STAND-BY.

## NON-PT TRIP ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN  from one PLACE of any sort to another, made on means other than Public Transport. A NON-PT TRIP may consist of consecutive ACCESS LEGs or OTHER LEGs.

## NORMAL DATED BLOCK ##

**Source:** Transmodel

**Definition:** A DATED BLOCK identical to a long-terms planned BLOCK, possibly updated according to short-term modifications decided by the control staff.

## NORMAL DATED VEHICLE JOURNEY ##

**Source:** Transmodel

**Definition:** A DATED VEHICLE JOURNEY identical to a long-term planned VEHICLE JOURNEY, possibly updated according to short-term modifications of the PRODUCTION PLAN decided by the control staff.

## NOTICE ##

**Source:** Transmodel

**Definition:** A text for informational purposes on exceptions in a LINE, a JOURNEY PATTERN, etc. The information may be usable for passenger or driver information.

## NOTICE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively.

## OBSERVED PASSING TIME ##

**Source:** Transmodel

**Definition:** The actual passing of a public transport vehicle at a pre-defined POINT during a MONITORED VEHICLE JOURNEY.

## OFFENCE ##

**Source:** Transmodel

**Definition:** A log entry providing data on a violation of fare rules.

## OFFENCE DEBIT ##

**Source:** Transmodel

**Definition:** A log entry providing data for a debiting action in case of a fine for an offence or penalty fare.

## OFFENDER ROLE ##

**Source:** Transmodel

**Definition:** The role enacted by someone attempting to travel with no or insufficient access rights.

## OFFERED TRAVEL SPECIFICATION ##

**Source:** Transmodel

**Definition:** A set of parameters giving details of the intended consumption of access rights associated with a SALES PACKAGE OFFER or a CUSTOMER PURCHASE PACKAGE. (e.g. origin and destination of a travel, class of travel, etc.).

## ONBOARD DEVICE BASED PASSENGER COUNT ##

**Source:** Transmodel

**Definition:** Possible implementation of LOGGABLE OBJECT designed for passenger counting based on onboard counting device (counting the number of passenger in the VEHICLE)

## ONBOARD STAY ##

**Source:** Transmodel

**Definition:** Permission to board early before the journey or stay on board after the journey.

## OPERATING DAY ##

**Source:** Transmodel

**Definition:** A day of public transport operation of which the characteristics are defined within in a specific SERVICE CALENDAR. An OPERATING DAY may last more than 24 hours.

## OPERATING DEPARTMENT ##

**Source:** Transmodel

**Definition:** A specific DEPARTMENT which administers certain LINEs.

## OPERATING PERIOD ##

**Source:** Transmodel

**Definition:** A continuous interval of time between two OPERATING DAYs which will be used to define validities.

## OPERATIONAL CONTEXT ##

**Source:** Transmodel

**Definition:** Characterization of a set of operational objects, such as timing or links determined either by a DEPARTMENT or by an ORGANISATIONAL UNIT.

## OPERATIONAL EVENT ##

**Source:** Transmodel

**Definition:** Any event affecting the public transport operation (production follow-up, management of information or the technical functioning), occurring on an OPERATING DAY and recorded in the system. An OPERATIONAL EVENT is generally causing a CONTROL ACTION.

## OPERATIONAL MESSAGE ##

**Source:** Transmodel

**Definition:** An information exchange between an EMPLOYEE (e.g. a controller), a LOGICAL DRIVER or a LOGICAL VEHICLE, used to inform about a CONTROL ACTION or an EVENT.

## OPERATOR ##

**Source:** Transmodel

**Definition:** A company providing public transport services.

## ORGANISATION ##

**Source:** Transmodel

**Definition:** A legally incorporated body associated with any aspect of the transport system.

## ORGANISATION DAY TYPE ##

**Source:** Transmodel

**Definition:** DAY TYPE that is defined in terms of operation or not operation of a referenced SERVICED ORGANISATION.

## ORGANISATION PART ##

**Source:** Transmodel

**Definition:** A part of an ORGANISATION to which specific responsibilities upon the data and data management may be assigned.

## ORGANISATION ROLE ##

**Source:** Transmodel

**Definition:** Generic corporate role to provide or manage transport services.

## ORGANISATIONAL UNIT ##

**Source:** Transmodel

**Definition:** An ORGANISATION PART to which a set of responsibilities in a public transport company for planning and control is assigned.

## ORGANISATIONAL VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** A type of VALIDITY PARAMETER related to organisational issues.

## OTHER CONTROL MEANS ##

**Source:** Transmodel

**Definition:** A particular means other than a control device, for example a manual procedure, used to control apply control processes.

## OTHER DEBIT ##

**Source:** Transmodel

**Definition:** A log entry providing data for a debiting action in case of other payment type than OFFENCE DEBIT or BOOKING DEBIT..

## OTHER LEG ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN corresponding to the movement of a user (passenger, driver) on a non-PT mode from one PLACE to another and that is not an ACCESS LEG or a PT CONNECTION LEG.

## OTHER ORGANISATION ##

**Source:** Transmodel

**Definition:** Generic ORGANISATION being neither an AUTHORITY, neither a public transport OPERATOR (TRAVEL AGENT, MANAGEMENT AGENT, etc.).

## OVERTAKING POSSIBILITY ##

**Source:** Transmodel

**Definition:** NETWORK RESTRICTION specifying a POINT or a LINK where vehicles of specified VEHICLE TYPEs are or are not allowed to overtake each other.

## PARKING ##

**Source:** Transmodel

**Definition:** Designated locations for leaving vehicles such as cars, motorcycles and bicycles.

## PARKING AREA ##

**Source:** Transmodel

**Definition:** A marked zone within a PARKING containing PARKING BAYs.

## PARKING BAY ##

**Source:** Transmodel

**Definition:** A place to park an individual vehicle.

## PARKING CAPACITY ##

**Source:** Transmodel

**Definition:** PARKING properties providing information about its CAPACITY.

## PARKING CHARGE BAND ##

**Source:** Transmodel

**Definition:** Parking charges that describe the cost of using a PARKING or PARKING AREA for a given period.

## PARKING COMPONENT ##

**Source:** Transmodel

**Definition:** Generic COMPONENT of a PARKING (e.g. PARKING AREA or PARKING BAY)

## PARKING ENTRANCE FOR VEHICLES ##

**Source:** Transmodel

**Definition:** An entrance for vehicles to the PARKING from the road.

## PARKING PASSENGER ENTRANCE ##

**Source:** Transmodel

**Definition:** An entrance to the PARKING for passengers on foot or other out-of-vehicle mode, such as wheelchair.

## PARKING POINT ##

**Source:** Transmodel

**Definition:** A TIMING POINT where vehicles may stay unattended for a long time. A vehicle's return to park at a PARKING POINT marks the end of a BLOCK.

## PARKING PRICE ##

**Source:** Transmodel

**Definition:** A specialisation of FARE PRICE that defines the price of a PARKING CHARGE BAND.

## PARKING PROPERTIES ##

**Source:** Transmodel

**Definition:** PARKING specific properties other than its capacity.

## PARKING TARIFF ##

**Source:** Transmodel

**Definition:** A set of parking CHARGE BANDS that describe the cost of using a PARKING or PARKING AREA.

## PARTIAL JOURNEY CANCELLATION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in assigning a JOURNEY PATTERN that is a subset of the original JOURNEY PATTERN to a DATED VEHICLE JOURNEY; thus specifically expressing that a part of a DATED VEHICLE JOURNEY has been cancelled.

## PARTICIPANT SYSTEM ##

**Source:** Transmodel

**Definition:** A SYSTEM supporting a service to fulfill specific types of  PI REQUESTs. May be associated with one or more DATA SOURCEs.

## PASSENGER ACCESSIBILITY NEED ##

**Source:** Transmodel

**Definition:** A passenger's requirement for accessibility, comprising one or more USER NEEDs. For example, that he is unable to navigate stairs, or lifts, or has visual or auditory impairments. PASSENGER ACCESSIBILITY NEEDS can be used to derive an accessibility constraint for the passenger, allowing the computation of paths for passengers with specifically constrained mobility. Example: Wheelchair, No Lifts, No Stairs.

## PASSENGER ACTIVATE TRIP EVENT ##

**Source:** Transmodel

**Definition:** A passenger action to initiate the consumption of access rights, usually at the start of a trip, for example by stamping a ticket at a validator device, or by an online interaction.

## PASSENGER CARRYING REQUIREMENT ##

**Source:** Transmodel

**Definition:** A classification of requirements for a public transport vehicle according to the passenger carrying capabilities of the vehicle.

## PASSENGER CHECK IN ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the check in of a passenger at a barrier or validation point at the start of a journey. May trigger prepayment.

## PASSENGER CHECK IN EVENT ##

**Source:** Transmodel

**Definition:** A passenger action to check in at the start of a trip.

## PASSENGER CHECK OUT ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the check out of a passenger at a barrier or exit validation point. May trigger post payment.

## PASSENGER CHECK OUT EVENT ##

**Source:** Transmodel

**Definition:** A passenger action to check out at the end of a trip.

## PASSENGER ENTRANCE ##

**Source:** ITxPT

**Definition:** A physical or virtual boundary point through which passengers can enter or exit, e.g. a vehicle door. A PASSENGER ENTRANCE has a designated enter-direction and a designated exit-direction.

## PASSENGER ENTRANCE COUNT ##

**Source:** ITxPT

**Definition:**  Number of passengers and other objects that have entered and exited through a specific PASSENGER ENTRANCE during a time span or since some implicit or explicit previous time/event. A possible implementation of LOGGABLE OBJECT.

## PASSENGER EQUIPMENT ##

**Source:** Transmodel

**Definition:** An item of equipment of a particular type actually available at a location within a PLACE or a VEHICLE

## PASSENGER INFORMATION EQUIPMENT ##

**Source:** Transmodel

**Definition:** A public transport information piece of equipment, as for instance terminals (on street, at information desks, telematic, ...) or printed material (leaflets displayed at stops, booklets, ...).

## PASSENGER ROLE ##

**Source:** Transmodel

**Definition:** The general role of consuming a travel service.

## PASSENGER SAFETY EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PASSENGER EQUIPMENT for passenger safety.

## PASSENGER SPACE ##

**Source:** ITxPT

**Definition:** A passenger area within a VEHICLE. It may be limited to only a part of a VEHICLE such as a TRAIN ELEMENT, upper deck/lower deck, first class compartment or a bounded open space. A PASSENGER SPACE can be part of, overlap with, and be made up of other PASSENGER SPACEs.

## PASSENGER SPACE CAPACITY ##

**Source:** ITxPT

**Definition:** The number of passengers and other objects that are present in a PASSENGER SPACE when it is at 100% capacity.

## PASSENGER SPACE ENTRANCE COUNT ##

**Source:** ITxPT

**Definition:** Number of passengers and other objects that entered and exited a specific PASSENGER SPACE during a time span or since some implicit or explicit previous time/event. A possible implementation of LOGGABLE OBJECT. It is in essence an aggregation of relevant PASSENGER ENTRANCE COUNTs according to ENTRANCE FOR PASSENGER SPACE information.

## PASSENGER SPACE OCCUPANCY COUNT ##

**Source:** ITxPT

**Definition:** Number of passengers and other objects that are in a PASSENGER SPACE at a given time. A possible implementation of LOGGABLE OBJECT.

## PASSENGER STOP ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The allocation of a SCHEDULED STOP POINT (i.e. a SCHEDULED STOP POINT of a SERVICE PATTERN or JOURNEY PATTERN) to a specific STOP PLACE for a SERVICE JOURNEY, and also possibly a QUAY and BOARDING POSITION.

## PASSENGER TRAVEL CONTROL EVENT ##

**Source:** Transmodel

**Definition:** _No definition in Transmodel source pdf_

## PASSENGER TRAVEL ENTRY ##

**Source:** Transmodel

**Definition:** An abstract VALIDATION ENTRY relating to control of the PASSENGER.

## PASSENGER USED SAME STOP ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the detection of a passenger re-entering a station within a threshold period.

## PASSENGER WAY POINT ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording a passenger checking in at a way point while in a trip so as to indicate travel by a specific itinerary.

## PASSENGER WAY POINT EVENT ##

**Source:** Transmodel

**Definition:** A passenger action to check in at a way point along a trip.

## PASSING TIME ##

**Source:** Transmodel

**Definition:** Time data concerning public transport vehicles passing a particular POINT; e.g. arrival time, departure time, waiting time.

## PATH GUIDANCE ##

**Source:** Transmodel

**Definition:** An instruction to a passenger for an individual step when following a path to interchange between two SCHEDULED STOP POINTs at a CONNECTION.

## PATH JUNCTION ##

**Source:** Transmodel

**Definition:** A designated point, inside or outside of a STOP PLACE or POINT OF INTEREST, at which two or more PATH LINKs may connect or branch.

## PATH LINK ##

**Source:** Transmodel

**Definition:** A link within a PLACE of or between two PLACEs (that is STOP PLACEs, ACCESS SPACEs or QUAYs,BOARDING POSITIONs,, POINTs OF INTEREST etc or PATH JUNCTIONs) that represents a step in a possible route for pedestrians, cyclists or other out-of-vehicle passengers within or between a PLACE.  NOTE: It is possible but not mandatory that a PATH LINK projects onto a more detailed set of infrastructure or mapping links that plot the spatial course, allowing it to be represented on maps and to tracking systems.

## PATH LINK END ##

**Source:** Transmodel

**Definition:** Beginning or end SITE for a PATH LINK. May be linked to a specific LEVEL of the SITE.

## PATH LINK IN SEQUENCE ##

**Source:** Transmodel

**Definition:** A step of a NAVIGATION PATH indicating traversal of a particular PATH LINK as part of a recommended route.  The same PATH LINK may occur in different sequences in different NAVIGATION PATHs.

## PAUSE ##

**Source:** Transmodel

**Definition:** A PAUSE is a period of paid driver time at the end of a SERVICE JOURNEY or during or after a DEAD RUN when the driver is responsible for the VEHICLE, but resting in the VEHICLE or in a designated BREAK FACILITY near the POINT where the VEHICLE has stopped.

## PAYMENT PROVIDER ROLE ##

**Source:** Transmodel

**Definition:** The role of channelling funds from the CUSTOMER to the FARE PRODUCT RETAILER for travel services, and particularly for usage-based travel products. For example EMV provider, ApplePay, PayPal, Android PAy, etc

## PENALTY POLICY ##

**Source:** Transmodel

**Definition:** Parameters determining a policy regarding different aspects of penalty charges, for example repeated entry at the same station, not having a ticket etc.

## PI DELIVERY ##

**Source:** Transmodel

**Definition:** A connection of a passenger to the operator information system, directly or via an employee, including one or several queries, and returning results.

## PI REQUEST ##

**Source:** Transmodel

**Definition:** A request for a specific information on public transport, expressed during a PI REQUEST.

## PI REQUEST FILTER ##

**Source:** Transmodel

**Definition:** Filtering criteria to be used when computing the results for a PI REQUEST.

## PI REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used when computing and decorating the results for the PI REQUEST.

## PLACE ##

**Source:** Transmodel

**Definition:** A geographic place of any type which may be specified as the origin or destination of a trip. A PLACE may be represented as a POINT (dimension 0) , a road section (dimension 1) or a ZONE (dimension 2).

## PLACE ACCESS EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT dedicated to access (e.g. lifts, entrances, stairs, ramps, etc.).

## PLACE EQUIPMENT ##

**Source:** Transmodel

**Definition:** An item of equipment of a particular type actually available at a location within a PLACE.

## PLACE IN SEQUENCE ##

**Source:** Transmodel

**Definition:** Point traversed by a NAVIGATION PATH in sequence, connected by a PATH LINK to the next point. May be a Place, PATH JUNCTION or POINT.

## PLACE LIGHTING ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT for LIGHTING EQUIPMENT (e.g. lamp post).

## PLACE RESULT ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the results of the LOCATION REQUEST.

## PLACE SIGN ##

**Source:** Transmodel

**Definition:** Sign with the name of a PLACE on it.

## PLANNED REMEDY ##

**Source:** Transmodel

**Definition:** A pre-prepared REMEDY that could include utilizing an alternative FACILITY as a replacement.

## POINT ##

**Source:** Transmodel

**Definition:** A 0-dimensional node of the network used for the spatial description of the network. POINTs may be located by a LOCATION in a given LOCATING SYSTEM.

## POINT IN JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** A SCHEDULED STOP POINT or TIMING POINT in a JOURNEY PATTERN with its order in that JOURNEY PATTERN.

## POINT IN LINK SEQUENCE ##

**Source:** Transmodel

**Definition:** A POINT in a LINK SEQUENCE indicating its order in that particular LINK SEQUENCE.

## POINT OF INTEREST ##

**Source:** Transmodel

**Definition:** A type of PLACE to or through which passengers may wish to navigate as part of their journey and which is modelled in detail by journey planners.

## POINT OF INTEREST CLASSIFICATION ##

**Source:** Transmodel

**Definition:** A classification of a POINT OF INTEREST that may be used in a CLASSIFICATION HIERARCHY to categorise the point by nature of interest using a systematic taxonomy, for example Museum, Football, Stadium.

## POINT OF INTEREST CLASSIFICATION HIERARCHY ##

**Source:** Transmodel

**Definition:** A logical hierarchy for organizing POINT OF INTEREST CLASSIFICATIONs. A POINT OF INTEREST CLASSIFICATION can belong to more than one hierarchy.

## POINT OF INTEREST CLASSIFICATION MEMBERSHIP ##

**Source:** Transmodel

**Definition:** The POINT OF INTEREST CLASSIFICATION and POINT OF INTEREST CLASSIFICATION MEMBERSHIP are used to encode a hierarchy of classifications to index and find different types of POINT OF INTEREST. For example, Educational Building -> School -> Primary School, or Cultural  Attraction -> Museum -> Art Museum.  POINT OF INTEREST CLASSIFICATION MEMBERSHIP does not have to be disjoint, i.e. the same category may appear in more than one classification.

## POINT OF INTEREST COMPONENT ##

**Source:** Transmodel

**Definition:** Specialisation of SITE COMPONENT for COMPONENT of POINT OF INTEREST. Usually used for POINT OF INTEREST SPACEs.

## POINT OF INTEREST ENTRANCE ##

**Source:** Transmodel

**Definition:** Specialisation of ENTRANCE to enter/exit a POINT OF INTEREST.

## POINT OF INTEREST SPACE ##

**Source:** Transmodel

**Definition:** Specialisation of POINT OF INTEREST COMPONENT for SPACEs. A physical area within the POINT OF INTEREST, such as a concourse.

## POINT OF INTEREST VEHICLE ENTRANCE ##

**Source:** Transmodel

**Definition:** A physical entrance or exit to/from a POINT OF INTEREST for vehicles .

## POINT ON LINK ##

**Source:** Transmodel

**Definition:** A POINT on a LINK which is not needed for LINK definition, but may be used for other purposes, e.g. for purposes of automatic vehicle monitoring, passenger information or for driver information.

## POINT ON ROUTE ##

**Source:** Transmodel

**Definition:** A ROUTE POINT used to define a ROUTE with its order on that ROUTE.

## POINT PROJECTION ##

**Source:** Transmodel

**Definition:** An oriented correspondence from one POINT of a source layer, onto a entity in a target layer: e.g. POINT, LINK, LINK SEQUENCE, COMPLEX FEATURE, within a defined TYPE OF PROJECTION.

## POSTAL ADDRESS ##

**Source:** Transmodel

**Definition:** A specification of ADDRESS refining it by using the attributes used for conventional identification for mail. Comprises variously a building Identifier, Street name, Post code and other descriptors.

## PRE-ASSIGNED FARE PRODUCT ##

**Source:** Transmodel

**Definition:** A FARE PRODUCT consisting of one or several VALIDABLE ELEMENTs, specific to a CHARGING MOMENT.

## PRICE GROUP ##

**Source:** Transmodel

**Definition:** A grouping of prices, allowing the grouping of numerous possible consumption elements into a limited number of price references, or to apply grouped increase, in value or percentage.

## PRICE UNIT ##

**Source:** Transmodel

**Definition:** A unit to express prices: amount of currency, abstract fare unit, ticket unit or token etc.

## PRICEABLE OBJECT ##

**Source:** Transmodel

**Definition:** An element which may have a FARE PRICE.

## PRICING PARAMETER SET ##

**Source:** Transmodel

**Definition:** A set of parameters controlling pricing calculations.

## PRICING RULE ##

**Source:** Transmodel

**Definition:** A rule used for the calculation of FARE PRICE, determined either by a set of parameters to be applied to a reference price or by a more complex algorithm. PRICING RULEs may be chained together.

## PRICING SERVICE ##

**Source:** Transmodel

**Definition:** A web service used to provide prices dynamically at time of booking or purchase.

## PRODUCTION PLAN ##

**Source:** Transmodel

**Definition:** A reference version of production activities (service journeys, dead runs, duties...). CONTROL ACTIONs are described with reference to the PRODUCTION PLAN they amend.

## PROFILE REQUIREMENTS ##

**Source:** Transmodel

**Definition:** The number and characteristics of the persons wishing to travel.

## PROPERTY OF DAY ##

**Source:** Transmodel

**Definition:** A property which a day may possess, such as school holiday, weekday, summer, winter etc.

## PSYCHOSENSORY NEED ##

**Source:** Transmodel

**Definition:** A specific USER NEED, i.e. a constraint of a passenger as regards his psycho-sensory impairments, such as visual impairment, auditory impairment, averse to confined spaces, etc.

## PT CONNECTION LEG ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN corresponding to the movement of a passenger transferring from one SERVICE JOURNEY to another, made over a CONNECTION from one SCHEDULED STOP POINT to another, and possibly following a specific NAVIGATION PATH.

## PT FARE OFFER ##

**Source:** Transmodel

**Definition:** An available fare for a specific PT RIDE LEG in a PT TRIP or for the whole PT TRIP, or for the whole TRIP PATTERN.  The fare may be restricted to particular products and conditions as described by SPECIFIC PARAMETER ASSIGNMENTS.

## PT RIDE LEG ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN corresponding to the movement of a user (passenger, driver) on one and only one public transport vehicle, from one SCHEDULED STOP POINT to another, on one JOURNEY PATTERN.

## PT SCOPE ##

**Source:** Transmodel

**Definition:** An extent consisting of public transport entities or combinations of entities such as OPERATORs, NETWORKs, LINEs, SCHEDULED STOP POINTs, STOP PLACEs, PLACEs, etc.

## PT SITUATION ##

**Source:** Transmodel

**Definition:** An incident or deviation affecting the planned PT operation.

## PT SITUATION AFFECTED SCOPE ##

**Source:** Transmodel

**Definition:** An extent directly involved in the PT SITUATION expressed using entities such as OPERATORs, NETWORKs, LINEs, SCHEDULED STOP POINTs, STOP PLACEs, PLACEs etc.

## PT SITUATION CONSEQUENCE ##

**Source:** Transmodel

**Definition:** A description of the consequences of the PT SITUATION generally or in relation to involved or indirectly impacted public transport elements.

## PT SITUATION CONSEQUENCE SCOPE ##

**Source:** Transmodel

**Definition:** An extent impacted by the PT SITUATION CONSEQUENCE expressed using entities such as LINEs, SERVICE JOURNEYs etc.

## PT SITUATION GENERAL CONSEQUENCE ##

**Source:** Transmodel

**Definition:** A parameter describing a general consequence of a PT SITUATION.

## PT SITUATION MESSAGE ##

**Source:** Transmodel

**Definition:** An information communicated concerning a certain PT SITUATION.

## PT TRIP ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN starting from the first boarding of a public transport vehicle to the last alighting . A PT TRIP consist of one or more PT RIDEs and the movement, usually walks, necessary to cover the corresponding CONNECTIONs, described as PT CONNECTION LEGs.

## PUBLICATION APPROVER ROLE ##

**Source:** Transmodel

**Definition:** A ROLE dedicated to decide if a MESSAGE fulfils relevant criteria to be published in a certain PUBLICATION SCOPE.

## PUBLICATION DECISION ##

**Source:** Transmodel

**Definition:** An approval or disapproval regulating if a MESSAGE can be published in a certain PUBLICATION SCOPE.

## PUBLICATION SCOPE ##

**Source:** Transmodel

**Definition:** An extent in which it is relevant to publish a MESSAGE expressed using entities such as LINEs, SCHEDULED STOP POINTs and VEHICLE JOURNEYs etc.

## PUBLICATION WINDOW ##

**Source:** Transmodel

**Definition:** A period during which the MESSAGE should be published.

## PUBLISHING ACTION ##

**Source:** Transmodel

**Definition:** A guidance to processing options such as through which channels a MESSAGE should be disseminated.

## PUBLISHING CHANNEL ##

**Source:** Transmodel

**Definition:** Specifies through which channels a MESSAGE should be disseminated.

## PURCHASE FULFILMENT ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the delivery of a TRAVEL DOCUMENT to a TRANSPORT CUSTOMER by any means, for example by email, SMS or download

## PURCHASE WINDOW ##

**Source:** Transmodel

**Definition:** Period in which the FARE PRODUCT must be purchased.

## PURCHASER ROLE ##

**Source:** Transmodel

**Definition:** The role of the party who pays for a travel service for one or more TRANSPORT CUSTOMERs..

## PURPOSE OF EQUIPMENT PROFILE ##

**Source:** Transmodel

**Definition:** A functional purpose which requires a certain set of equipment of different types put together in a VEHICLE EQUIPMENT PROFILE.

## PURPOSE OF GROUPING ##

**Source:** Transmodel

**Definition:** Functional purpose for which GROUPs of elements are defined. The PURPOSE OF GROUPING may be restricted to one or more types of the given object.

## PURPOSE OF JOURNEY PARTITION ##

**Source:** Transmodel

**Definition:** An operational purpose changing within a JOURNEY PATTERN and with this subdividing the SERVICE JOURNEY into JOURNEY PARTs.

## QUALIFICATION ##

**Source:** Transmodel

**Definition:** A specific knowledge or ability or experience, or a certified skill or education, which may be possessed by an EMPLOYEE and which may be necessary to work a DUTY.

## QUALITY STRUCTURE FACTOR ##

**Source:** Transmodel

**Definition:** A factor influencing access rights definition or calculation of prices, based on the quality: traffic congestion threshold, early/late reservation etc.

## QUALITY STRUCTURE FACTOR PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a QUALITY STRUCTURE FACTOR , e.g. default total price etc.

## QUAY ##

**Source:** Transmodel

**Definition:** A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi, cars or other means of transportation. A QUAY may serve one or more VEHICLE STOPPING PLACEs and be associated with one or more SCHEDULED STOP POINTS. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY.

## QUEUING EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT dedicated to queuing.

## RAILWAY ELEMENT ##

**Source:** Transmodel

**Definition:** A type of INFRASTRUCTURE LINK used to describe a railway network.

## RAILWAY JUNCTION ##

**Source:** Transmodel

**Definition:** A type of INFRASTRUCTURE POINT used to describe a railway network.

## RAMP EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT for ramps (provides ramp characteristics like length, gradient, etc.).

## REBATING ##

**Source:** Transmodel

**Definition:** Parameters indicating whether and how a rebate may be offered for the product, for example if performance targets are not met or an inferior replacement service is run

## RECORDED LEG ##

**Source:** Transmodel

**Definition:** The recording of the actual LEG followed by a passenger on an OPERATING DAY

## RECORDED STOP ##

**Source:** Transmodel

**Definition:** The recorded stop at a STOP POINT during actual service operation to possibly let passengers board or alight the vehicle.

## RECORDED TRIP ##

**Source:** Transmodel

**Definition:** The actual TRIP undertaken by a passenger from an origin to a destination.

## REFUNDING ##

**Source:** Transmodel

**Definition:** Parameters indicating whether and how the FARE PRODUCT may be refunded.

## REGISTRAR ROLE ##

**Source:** Transmodel

**Definition:** The ADMINISTRATIVE ORGANISATION ROLE of coordinating the issue of unique registration codes for  Organisations, Products, Travel Documents etc. etc. The Registrar , A function may issues unique identifiers directly or devise rules  for generating unique identifiers

## RELATED SITUATION ##

**Source:** Transmodel

**Definition:** A partial or alternate view of the same SITUATION.

## RELIEF OPPORTUNITY ##

**Source:** Transmodel

**Definition:** A time in a BLOCK where a vehicle passes a RELIEF POINT. This opportunity may or may not be actually used for a relief.

## RELIEF POINT ##

**Source:** Transmodel

**Definition:** A TIMING POINT where a relief is possible, i.e. a driver may take on or hand over a vehicle. The vehicle may sometimes be left unattended.

## REMEDY ##

**Source:** Transmodel

**Definition:** A general or planned counter-measure to compensate a deviating FACILITY CONDITION.

## REPEATED TRIP FARE REQUEST ##

**Source:** Transmodel

**Definition:** A TRIP FARE REQUEST about the best fare products to use for repeated similar trips.

## REPEATED TRIP FARE REQUIREMENTS ##

**Source:** Transmodel

**Definition:** The characteristics of a repeated trip â€“ number of trips per day, etc

## REPLACING ##

**Source:** Transmodel

**Definition:** Parameters indicating whether and how the access right may be replaced.

## REQUESTED TRAVEL SPECIFICATION ##

**Source:** Transmodel

**Definition:** A set of parameters giving details of an intended consumption of access rights requested by a TRANSPORT CUSTOMER  (e.g. origin and destination of a travel, class of travel, etc.).

## RESELLING ##

**Source:** Transmodel

**Definition:** Parameters indicating whether common resale conditions (i.e. for exchange or refund) attached to an access right.product.

## RESELLING MOMENT ##

**Source:** Transmodel

**Definition:** A classification of moment at which a booking or reservation may be made, e.g. in advance, at stop, on boarding, on board, etc.

## RESERVATION MOMENT ##

**Source:** Transmodel

**Definition:** A classification of moment at which a booking or reservation may be made, e.g. in advance, at stop, on boarding, on board, etc.

## RESERVING ##

**Source:** Transmodel

**Definition:** Parameters indicating whether the access right requires reservation.

## RESIDENTIAL ELIGIBILITY ##

**Source:** Transmodel

**Definition:** Parameters indicating whether a specific TRANSPORT CUSTOMER is eligible for an access right with a specific RESIDENTIAL PROFILE as a validity parameter.

## RESIDENTIAL QUALIFICATION ##

**Source:** Transmodel

**Definition:** A parameter providing an authorisation to consider a user as being characterised by a USER PROFILE.

## RESORPTION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in progressively resorbing a delay on one DATED VEHICLE JOURNEY by rescheduling the departure times at one POINT of the following journeys. It is a way of maintaining regular intervals after a disturbance on a particular journey.

## RESOURCE FRAME ##

**Source:** Transmodel

**Definition:** A set of resource data to which the same VALIDITY CONDITIONs have been assigned.

## RESPACING ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION consisting in respacing departure times at one POINT after a journey or a vehicle has been added or canceled, in order to preserve the regularity of intervals.

## RESPONSIBILITY ROLE ##

**Source:** Transmodel

**Definition:** A particular role an ORGANISATION or an ORGANISATION PART is playing as regards certain data, for example data origination, data augmentation, data aggregation, data distribution, planning, operation, control, ownership etc).

## RESPONSIBILITY ROLE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of one or more roles to an ORGANISATION or an ORGANISATION PART as regards the responsibility it will have as regards specific data (e.g. ownership, planning, etc.) and the management of this data (e.g. distribution, updates, etc.).

## RESPONSIBILITY SET ##

**Source:** Transmodel

**Definition:** A list of possible responsibilities over one or more ENTITies IN VERSION., resulting from the process of the assignment of RESPONSIBILITY ROLEs (such as data origination, ownership, etc) on specific data (instances) to ORGANISATIONs or ORGANISATION PARTs.

## REST ##

**Source:** Transmodel

**Definition:** A REST is a representation of a day off for a driver.

## RESTORE CUSTOMER ACCOUNT ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER ACCOUNT ENTRY recording the restoration of an CUSTOMER ACCOUNT.

## RESTORE CUSTOMER ACCOUNT EVENT ##

**Source:** Transmodel

**Definition:** The reinstallation to replacement media of an electronic travel document by a TRANSPORT CUSTOMER on a MEDIA DEVICE, usually as a MEDIA APPLICATION, possibly with recovered stored value.

## RETAIL CONSORTIUM ##

**Source:** Transmodel

**Definition:** A group of ORGANISATIONs formally incorporated as a retailer of FARE PRODUCTS.

## RETAIL DEVICE ##

**Source:** Transmodel

**Definition:** An equipment used to sell FARE PRODUCTs. Its identity can be used to record fulfilment and support security processes.

## RETAIL DEVICE SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of an specific RETAIL DEVICE on a SECURITY LIST.

## RETAIL SERVICE ##

**Source:** Transmodel

**Definition:** Specialisation of LOCAL SERVICE dedicated to retail services.

## REVENUE PROTECTION ENTRY ##

**Source:** Transmodel

**Definition:** An abstract FARE CONTRACT ENTRY relating to measures to enforce revenue protection.

## RHYTHMICAL JOURNEY GROUP ##

**Source:** Transmodel

**Definition:** A group of VEHICLE JOURNEYS following the same JOURNEY PATTERN having the same rhythm" every hour (for example runs at xxh10, xxh25 and xxh45... ) between a specified start and end time."

## ROAD ADDRESS ##

**Source:** Transmodel

**Definition:** Specialization of ADDRESS refining it by using the characteristics such as road number, and name used for conventional identification of along a road.

## ROAD ELEMENT ##

**Source:** Transmodel

**Definition:** A type of INFRASTRUCTURE LINK used to describe a road network.

## ROAD JUNCTION ##

**Source:** Transmodel

**Definition:** A type of INFRASTRUCTURE POINT used to describe a road network.

## ROSTER CYCLE ##

**Source:** Transmodel

**Definition:** A ROSTER CYCLE is a sequence pattern of days of work and days of rest where the days of work may be further specified by a particular DUTY TYPE.

## ROSTER CYCLE ELEMENT ##

**Source:** Transmodel

**Definition:** A ROSTER CYCLE ELEMENT is an element of a ROSTER CYCLE which represents a day of work or rest for a theoretically available driver in the ordered sequence of days for that cycle.

## ROSTER DESIGN ##

**Source:** Transmodel

**Definition:** A ROSTER DESIGN is roster building unit made up of a particular number of DESIGN WEEKs to each of which a different sequence pattern of DUTY TYPEs and days of rest will be assigned.

## ROSTER DESIGN IN MATRIX ##

**Source:** Transmodel

**Definition:** A ROSTER DESIGN IN MATRIX describes the order in which different ROSTER DESIGNs are applied to construct a certain ROSTER MATRIX.

## ROSTER DESIGN TYPE ##

**Source:** Transmodel

**Definition:** A ROSTER DESIGN TYPE is a classification of a ROSTER DESIGN which may describe the number of weeks that are covered, the proportion of work to free days or other characteristics.

## ROSTER ELEMENT ##

**Source:** Transmodel

**Definition:** A ROSTER ELEMENT is a cell in a ROSTER MATRIX where the individual DUTY to be performed by a theoretically available driver on a certain OPERATING DAY is entered or it is marked that it is a day of rest.

## ROSTER MATRIX ##

**Source:** Transmodel

**Definition:** A ROSTER MATRIX is a table showing the duty plan for a period of days and for a number of theoretically available drivers.

## ROUGH SURFACE ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT for rough surfaces, giving properties of surface texture, mainly for impaired person information.

## ROUND TRIP ##

**Source:** Transmodel

**Definition:** Parameters relating to single or return trip use of an access right.

## ROUNDING ##

**Source:** Transmodel

**Definition:** Parameters directing the rounding of values that are the result of calculations.

## ROUNDING METHOD ##

**Source:** Transmodel

**Definition:** A classification of PRICING RULES.

## ROUNDING STEP ##

**Source:** Transmodel

**Definition:** Parameters to determine the rounding value to be used for a given calculation result. If a rounding step table is used, any value equal to or larger than the step key and smaller that the next step key should be rounded to the value indicated for the step value.

## ROUTE ##

**Source:** Transmodel

**Definition:** An ordered list of located POINTs defining one single path through the road (or rail) network. A ROUTE may pass through the same POINT more than once.

## ROUTE LINK ##

**Source:** Transmodel

**Definition:** An oriented link between two ROUTE POINTs allowing the definition of a unique path through the network.

## ROUTE POINT ##

**Source:** Transmodel

**Definition:** A POINT used to define the shape of a ROUTE through the network.

## ROUTING ##

**Source:** Transmodel

**Definition:** Parameters expressing limitations on routing of an access right.

## ROUTING CONSTRAINT ZONE ##

**Source:** Transmodel

**Definition:** A ZONE defining a ROUTING CONSTRAINT. The ZONE may be defined by its contained SCHEDULED STOP POINTS or by its boundary points.  Examples of routing constraints are : If you board in this ZONE, you can't alight in the same ZONE"."

## ROUTING VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** A type of VALIDITY PARAMETER linked to specific routing.

## ROW/DRIVER ##

**Source:** Transmodel

**Definition:** A ROW/DRIVER is a row in a ROSTER MATRIX which is related to a theoretically available driver.

## RUBBISH DISPOSAL ##

**Source:** Transmodel

**Definition:** Specialization of EQUIPMENT for Rubbish disposal, describing rubbish types, etc.

## SALE DISCOUNT RIGHT ##

**Source:** Transmodel

**Definition:** A FARE PRODUCT allowing a customer to benefit from discounts when purchasing SALES OFFER PACKAGEs.

## SALES EVENT ##

**Source:** Transmodel

**Definition:** The purchase of a product by a CUSTOMER.

## SALES NOTICE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of a NOTICE to a SALES OFFER PACKAGE or a GROUP OF SALES OFFER PACKAGEs.

## SALES OFFER PACKAGE ##

**Source:** Transmodel

**Definition:** A package to be sold as a whole, consisting of one or several FARE PRODUCTs materialised thanks to one or several TRAVEL DOCUMENTs. The FARE PRODUCTs may be either directly attached to the TRAVEL DOCUMENTs, or may be reloadable on the TRAVEL DOCUMENTs.

## SALES OFFER PACKAGE ELEMENT ##

**Source:** Transmodel

**Definition:** The assignment of a FARE PRODUCT to a TYPE OF TRAVEL DOCUMENT in order to define a SALES OFFER PACKAGE, realised as a fixed assignment (printing, magnetic storage etc.) or by the possibility for the FARE PRODUCT to be reloaded on the TYPE OF TRAVEL DOCUMENT.

## SALES OFFER PACKAGE PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a SALES OFFER PACKAGE: default total price etc.

## SALES OFFER PACKAGE SUBSTITUTION ##

**Source:** Transmodel

**Definition:** Information on the preferred substitution of a SALES OFFER PACKAGE by another (or a set of others) if a quota restricted FARE PRODUCT is no longer available.

## SALES TRANSACTION ##

**Source:** Transmodel

**Definition:** A sale of a SALES OFFER PACKAGE

## SALES TRANSACTION FRAME ##

**Source:** Transmodel

**Definition:** A set of SALES TRANSACTION data elements to which the same VALIDITY CONDITIONs have been assigned.

## SANITARY EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PASSENGER EQUIPMENT for sanitary facilities.

## SCHEDULE DELIVERY ##

**Source:** Transmodel

**Definition:** A specialization of PI DELIVERY to make one or more SCHEDULE REQUESTs.

## SCHEDULE REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST about public timetables.

## SCHEDULE REQUEST CONTENT FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the results of the SCHEDULE REQUEST.

## SCHEDULE REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used to when computing and decorating SCHEDULE REQUEST results.

## SCHEDULED STOP POINT ##

**Source:** Transmodel

**Definition:** A POINT where passengers can board or alight from vehicles.

## SCHEMATIC MAP ##

**Source:** Transmodel

**Definition:** A map representing schematically the layout of the topographic structure of PLACEs (e.g. a set of SITEs) or the public transport network (a set of LINEs). It can include a pixel projection of a set of ENTITies onto a bitmap image so as to support hyperlinked interactions.

## SCOPING VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** A grouping of parameters (different from time-related validity parameters) defining the scope of access rights validity, e. g on a part of the network, on certain services, etc.

## SEATING EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT describing the properties of seating

## SECTION ##

**Source:** Transmodel

**Definition:** A reusable and ordered sequence of POINTs or LINKs.

## SECTION IN LINK SEQUENCE ##

**Source:** Transmodel

**Definition:** A SECTION embedded in a LINK SEQUENCE. A LINK SEQUNCE can contain several SECTIONS (ordered).

## SECURITY LIST ##

**Source:** Transmodel

**Definition:** A list of items whose status is to be accepted or denied for a process such as purchase or validation.

## SECURITY LIST ALLOW ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the granting of access to the network by the addition to a WHITE LIST or removal from a BLACK LIST of a token that identifies of an ENTITY such as a TRANSPORT CUSTOMER, CUSTOMER ACCOUNT, FARE CONTRACT, TRAVEL DOCUMENT, etc.

## SECURITY LIST DENY ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the denying of access to the transport network by the addition to a BLACK LIST or removal from a WHITE LIST of a token that identifies a TRANSPORT CUSTOMER, CUSTOMER ACCOUNT, FARE CONTRACT, TRAVEL DOCUMENT, etc

## SECURITY LIST ENTRY ##

**Source:** Transmodel

**Definition:** An abstract FARE CONTRACT ENTRY relating to measures to enforce Revenue Protection.

## SECURITY LISTABLE ##

**Source:** Transmodel

**Definition:** A entity capable of being placed on a SECURITY LIST.

## SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of an identified Entity on a SECURITY LIST..

## SECURITY MANAGER ROLE ##

**Source:** Transmodel

**Definition:** The ADMINISTRATIVE ORGANISATION ROLE of establishing and coordinating a security policy across the provider organisations, and of the certifying and auditing of Organisations, Applications, etc for their conformance to the security policy.

## SERIES CONSTRAINT ##

**Source:** Transmodel

**Definition:** An extension of a DISTANCE MATRIX ELEMENT (a cell of an origin-destination matrix for TARIFF ZONEs or SCHEDULED STOP POINTs) expressing a fare distance for the corresponding trip (value in km, number of fare units etc.), constrained to specific routes. SERIES CONSTRAINTs are mainly used for rail fares.

## SERIES CONSTRAINT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a SERIES CONSTRAINT: default total price etc.

## SERVICE ACCESS RIGHT ##

**Source:** Transmodel

**Definition:** An immaterial marketable element dedicated to accessing some services.

## SERVICE CALENDAR ##

**Source:** Transmodel

**Definition:** A collection of DAY TYPE ASSIGNMENTs.

## SERVICE CALENDAR FRAME ##

**Source:** Transmodel

**Definition:** A coherent set of assignments of OPERATING DAYS to DAY TYPES.

## SERVICE EXCLUSION ##

**Source:** Transmodel

**Definition:** A constraint expressing the fact that the service, on a specific JOURNEY PATTERN (usually a flexible transport service JOURNEY PATTERN) cannot operate when another (regular) service operates. This may occur only on a subpart of the JOURNEY PATTERN, or only on one or some specific SCHEDULED STOP POINTS.

## SERVICE FACILITY SET ##

**Source:** Transmodel

**Definition:** Set of FACILITies available for a specific VEHICLE TYPE (e.g. carriage equipped with low floor) possibly only for a service (or for a SERVICE JOURNEY or a JOURNEY).

## SERVICE FRAME ##

**Source:** Transmodel

**Definition:** A set of network service data (and other data logically related to these) to which the same VALIDITY CONDITIONs has been assigned.

## SERVICE JOURNEY ##

**Source:** Transmodel

**Definition:** A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN.

## SERVICE JOURNEY DELIVERY ##

**Source:** Transmodel

**Definition:** A specialisation of PI DELIVERY to respond to one or more SERVICE JOURNEY REQUESTs.

## SERVICE JOURNEY INTERCHANGE ##

**Source:** Transmodel

**Definition:** The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different SCHEDULED STOP POINTs.

## SERVICE JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY.

## SERVICE JOURNEY PATTERN INTERCHANGE ##

**Source:** Transmodel

**Definition:** A recognised/organised possibility for passengers to change public transport vehicles using two SCHEDULED STOP POINTs (which may be identical) on two particular SERVICE JOURNEY PATTERNs, including the maximum wait duration allowed and the standard to be aimed at. These may supersede the times given for the DEFAULT INTERCHANGE. Schedulers may use this entity for synchronisation of journeys.

## SERVICE JOURNEY REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST to find information about a specific SERVICE JOURNEY.

## SERVICE JOURNEY REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Criteria to be used to when computing and decorating results for a SERVICE JOURNEY REQUEST

## SERVICE LINK ##

**Source:** Transmodel

**Definition:** A LINK between an ordered pair of SCHEDULED STOP POINTs.

## SERVICE OPERATOR ROLE ##

**Source:** Transmodel

**Definition:** The role of an organisation that provides a service to the customer who uses a product - in particular the carrier role for public transport, but also possibly ancillary services such as catering, baggage handling, parking, etc.

## SERVICE PATTERN ##

**Source:** Transmodel

**Definition:** The subset of a JOURNEY PATTERN made up only of STOP POINTs IN JOURNEY PATTERN.

## SERVICE RESTRICTION ##

**Source:** Transmodel

**Definition:** Parameters describing the limitations as regards the use of equipment or service.

## SERVICE SITE ##

**Source:** Transmodel

**Definition:** A sub-type of SITE which is of specific interest for the operator (e.g. where a joint service or a joint fee is proposed)., other than a STOP PLACE.

## SERVICE VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** A type of VALIDITY PARAMETER related to service characteristics (e.g. class).

## SERVICED ORGANISATION ##

**Source:** Transmodel

**Definition:** A public or private organisation for which public transport services are provided on specific days, e.g. a school, univesirty or works.

## SHELTER EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of WAITING EQUIPMENT for a shelter.

## SIGN EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT for signs (heading signs, etc.).

## SIMPLE FEATURE ##

**Source:** Transmodel

**Definition:** An abstract representation of elementary objects related to the spatial representation of the network. POINTs (0-dimensional objects), LINKs (1-dimensional objects) and ZONEs (2-dimensional objects) may be viewed as SIMPLE FEATUREs.

## SINGLE TRIP FARE REQUEST ##

**Source:** Transmodel

**Definition:** A TRIP FARE REQUEST about fares for a single trip or return trip.

## SITE ##

**Source:** Transmodel

**Definition:** A well known PLACE to which passengers may refer to indicate the origin or a destination of a trip.

## SITE COMPONENT ##

**Source:** Transmodel

**Definition:** An element of a SITE describing a part of its structure. SITE COMPONENTs share common properties for data management, accessibility and other features.

## SITE CONNECTION ##

**Source:** Transmodel

**Definition:** The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip, determined by physical locations, such as SITEs and/or its components and/or ENTRANCEs, in particular STOP PLACEs and/or its components. Different times may be necessary to cover the resulting distance, depending on the kind of passenger.

## SITE CONNECTION END ##

**Source:** Transmodel

**Definition:** One end of a SITE CONNECTION.

## SITE ELEMENT ##

**Source:** Transmodel

**Definition:** A type of ADRESSABLE PLACE specifying common properties of a SITE or a SITE COMPONENT to describe it, including accessibility.

## SITE EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT for SITEs (e.g. LUGGAGE LOCKER, WAITING EQUIPMENT, TROLLEY STAND, etc.)

## SITE FACILITY SET ##

**Source:** Transmodel

**Definition:** Set of FACILITies available for a SITE ELEMENT .

## SITE FRAME ##

**Source:** Transmodel

**Definition:** A set of SITE data to which the same VALIDITY CONDITIONs have been assigned.

## SITE OPERATIONAL EVENT ##

**Source:** Transmodel

**Definition:** An OPERATIONAL EVENT applying to a SITE.

## SITUATION ##

**Source:** Transmodel

**Definition:** An incident or deviation affecting traffic or travel circumstances.

## SITUATION AUTHOR ROLE ##

**Source:** Transmodel

**Definition:** A ROLE dedicated to provide relevant content of SITUATION.

## SITUATION CAUSE ##

**Source:** Transmodel

**Definition:** An event or set of events inducing a change in public transport or traffic operation.

## SITUATION DELIVERY ##

**Source:** Transmodel

**Definition:** The result returned by an SITUATION REQUEST.

## SITUATION REASON ##

**Source:** Transmodel

**Definition:** A classification of what caused the SITUATION.

## SITUATION REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST to find extant SITUATIONs.

## SITUATION REQUEST FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the results of the SITUATION REQUEST.

## SITUATION REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used to when finding SITUATIONs.

## SITUATION SOURCE ##

**Source:** Transmodel

**Definition:** A description of the origin of the incident or deviation information.

## SMARTCARD ##

**Source:** Transmodel

**Definition:** A smart card with the necessary facilities (hardware and software) are) to host a MEDIUM APPLICATION INSTANCE and communicate with a control device.

## SPARE DUTY ##

**Source:** Transmodel

**Definition:** A SPARE DUTY is a DUTY to which specific timed work has not yet been assigned.

## SPECIAL SERVICE ##

**Source:** Transmodel

**Definition:** A work of a vehicle that is not planned in a classical way, i.e. that is generally not based on VEHICLE JOURNEYs using JOURNEY PATTERNs. It involves specific characteristics (such as specific access rights) and/or may be operated under specific circumstances.

## SPECIFIC OBSERVER ROLE ##

**Source:** Transmodel

**Definition:** The role of observing passenger information for the trip of a specific PASSENGER or GROUP OF PASSENGERs

## SPECIFIC PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A VALIDITY PARAMETER ASSIGNMENT specifying practical parameters during a TRAVEL SPECIFICATION, within a given fare structure (e.g. the origin or destination zone in a zone-counting system).

## SPELL ##

**Source:** Transmodel

**Definition:** A SPELL is a continuous period in a STRETCH, when a driver is on duty on one vehicle or performing one other type of work.

## SPLIT DUTY ##

**Source:** Transmodel

**Definition:** A SPLIT DUTY is a classification of a DUTY, in terms of working hours comprising several time bands separated in different DUTY PARTs by periods of unpaid time.

## STAIR EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT for stairs (stair, escalator, staircase, etc.).

## STAIRCASE EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of STAIR EQUIPMENT for stair cases.

## STAND-BY ##

**Source:** Transmodel

**Definition:** A STAND-BY is a non-driving period of a driver's DUTY when the driver must wait ready to take on any specified piece of work instantly.

## START TIME AT STOP POINT ##

**Source:** Transmodel

**Definition:** A time at which a fare time band (peak, off peak, etc ) is deemed to begin for trips starting at a particular station.

## STATION EMPLOYEE ROLE ##

**Source:** Transmodel

**Definition:** The STATION STAFF ROLE is to provide services at a station or other interchange.

## STEP LIMIT ##

**Source:** Transmodel

**Definition:** Geographical parameter limiting the access rights by counts of stops, sections or zones.

## STOP AREA ##

**Source:** Transmodel

**Definition:** A group of SCHEDULED STOP POINTs close to each other.

## STOP ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The allocation of a SCHEDULED STOP POINT (i.e. a SCHEDULED STOP POINT of a SERVICE PATTERN or JOURNEY PATTERN) to a specific STOP PLACE, for either a SERVICE JOURNEY or VEHICLE SERVICE.

## STOP EVENT DELIVERY ##

**Source:** Transmodel

**Definition:** A specialization of PI DELIVERY to make one or more STOP EVENT REQUESTs.

## STOP EVENT REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST about arrivals and departures from a given stop and/or LOGICAL DISPLAY at that stop.

## STOP EVENT REQUEST CONTENT FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters used to limit the results of the STOP EVENT REQUESTs.

## STOP EVENT REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used to when computing and decorating STOP EVENT REQUEST results.

## STOP FARE DELIVERY ##

**Source:** Transmodel

**Definition:** A specialization of PI DELIVERY that returns the tariff zones for a stop.

## STOP FARE REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST to find the tariff zones for a stop.

## STOP PLACE ##

**Source:** Transmodel

**Definition:** A place comprising one or more locations where vehicles may stop and where passengers may board or leave vehicles or prepare their trip. A STOP PLACE will usually have one or more wellknown names.

## STOP PLACE COMPONENT ##

**Source:** Transmodel

**Definition:** An element of a STOP PLACE describing part of its structure. STOP PLACE COMPONENTs share common properties for data management, accessibility and other features.

## STOP PLACE ENTRANCE ##

**Source:** Transmodel

**Definition:** A physical entrance or exit to/from a STOP PLACE for a Passenger. May be a door, barrier, gate or other recognizable point of access.

## STOP PLACE SPACE ##

**Source:** Transmodel

**Definition:** A physical area within a STOP PLACE, for example, a QUAY, BOARDING POSITION, ACCESS SPACE or EQUIPMENT PLACE.

## STOP PLACE VEHICLE ENTRANCE ##

**Source:** Transmodel

**Definition:** A physical entrance or exit to/from a STOP PLACE for a vehicle.

## STOP POINT IN JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** A POINT in a JOURNEY PATTERN which is a SCHEDULED STOP POINT.

## STRETCH ##

**Source:** Transmodel

**Definition:** A STRETCH is a period of a driver's DUTY during which the driver is continuously working without a BREAK but that may include PAUSEs during which the driver remains responsible for the vehicle.

## SUBMODE ##

**Source:** Transmodel

**Definition:** A variant of a MODE, as for instance international or domestic rail (rail being the MODE).

## SUITABILITY ##

**Source:** Transmodel

**Definition:** A statement of whether a particular USER NEED can be met. It can be used to state whether a SITE can be accessed by a passenger with a particular USER NEED.

## SUPPLEMENT PRODUCT ##

**Source:** Transmodel

**Definition:** A PRE-ASSIGNED FARE PRODUCT that will provide additional right when used with (as a complement of) another (reserved seat, second to first class upgrade, etc.). SUPPLEMENT PRODUCT also usually means supplement price.

## SUSPICIOUS BEHAVIOUR ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION EVENT recording the detection of suspicious behaviour.

## TARGET PASSING TIME ##

**Source:** Transmodel

**Definition:** Time data about when a public transport vehicle should pass a particular POINT IN JOURNEY PATTERN on a particular DATED VEHICLE JOURNEY, in order to match the latest valid plan.

## TARIFF ##

**Source:** Transmodel

**Definition:** A particular tariff, described by a combination of parameters.

## TARIFF ZONE ##

**Source:** Transmodel

**Definition:** A ZONE used to define a zonal fare structure in a zone-counting or zone-matrix system.

## TARIFF ZONE IN AREA ##

**Source:** Transmodel

**Definition:** Association of a Stop with a tariff Zone.

## TASK ##

**Source:** Transmodel

**Definition:** A TASK is any continuous piece of non-driving work, performed by a driver.

## TECHNOLOGY ORGANISATION ROLE ##

**Source:** Transmodel

**Definition:** The role of an ORGANISATION that provides some aspect of electronic fare or information services and products.

## TEMPLATE SERVICE JOURNEY ##

**Source:** Transmodel

**Definition:** A passenger carrying TEMPLATE SERVICE JOURNEY. As TEMPLATE SERVICE JOURNEY, it may represent multiple journeys.

## TEMPLATE VEHICLE JOURNEY ##

**Source:** Transmodel

**Definition:** A repeating VEHICLE JOURNEY for which a frequency has been specified, either as a HEADWAY JOURNEY GROUP (e.g. every 20 minutes) or a RHYTHMICAL JOURNEY GROUP (e.g. at 15, 27 and 40 minutes past the hour). It may thus represent multiple journeys.

## TEMPORAL VALIDITY PARAMETER ##

**Source:** Transmodel

**Definition:** Grouping of time-related parameters defining the validity of access rights.

## THIRD PARTY PRODUCT ##

**Source:** Transmodel

**Definition:** A FARE PRODUCT that is marketed together with a Public Transport FARE PRODUCT.

## TICKET SCOPE ##

**Source:** Transmodel

**Definition:** Scope of ticket.

## TICKET VALIDATOR EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PASSENGER EQUIPMENT (PLACE EQUIPMENT) describing ticket validators.

## TICKETING BASED PASSENGER COUNT ##

**Source:** Transmodel

**Definition:** Possible implementation of LOGGABLE OBJECT designed for passenger counting based on ticketing (validations)

## TICKETING EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialization of PASSENGER EQUIPMENT for ticketing.

## TICKETING SERVICE ##

**Source:** Transmodel

**Definition:** Specialization of LOCAL SERVICE for ticketing, providing ticket counter and online purchase information, also associated with payment method and TYPE OF TICKET.

## TIME ALLOWANCE ##

**Source:** Transmodel

**Definition:** A TIME ALLOWANCE is a fixed paid time allowed to perform certain activities to prepare for or to complete the work assigned either to a BLOCK, a DUTY , a DUTY PART, a STRETCH or a SPELL.

## TIME BAND ##

**Source:** Transmodel

**Definition:** A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category.

## TIME DEMAND TYPE ##

**Source:** Transmodel

**Definition:** An indicator of traffic conditions or other factors which may affect vehicle run or wait times. It may be entered directly by the scheduler or defined by the use of TIME BANDs.

## TIME DEMAND TYPE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment of a TIME DEMAND TYPE to a TIME BAND depending on the DAY TYPE and GROUP OF TIMING LINKS.

## TIME INTERVAL ##

**Source:** Transmodel

**Definition:** A time-based interval specifying access rights for the FARE STRUCTURE ELEMENTs within the range of this interval: 0-1 hour, 1-3 days etc.

## TIME INTERVAL PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a TIME INTERVAL, e.g. default total price etc.

## TIME STRUCTURE FACTOR ##

**Source:** Transmodel

**Definition:** The value of a TIME INTERVAL expressed by a TIME UNIT.

## TIME UNIT ##

**Source:** Transmodel

**Definition:** A unit for calculating time-based graduated fares.

## TIME UNIT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a TIME UNIT: default total price etc.

## TIMETABLE FRAME ##

**Source:** Transmodel

**Definition:** A set of timetable data to which the same VALIDITY CONDITIONs have been assigned.

## TIMETABLED PASSING TIME ##

**Source:** Transmodel

**Definition:** Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE.

## TIMING LINK ##

**Source:** Transmodel

**Definition:** An ordered pair of TIMING POINTs for which run times may be recorded.

## TIMING LINK IN JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** The position of a TIMING LINK in a JOURNEY PATTERN. This entity is needed if a TIMING LINK is repeated in the same JOURNEY PATTERN, and separate information is to be stored about each iteration of the TIMING LINK.

## TIMING PATTERN ##

**Source:** Transmodel

**Definition:** The subset of a JOURNEY PATTERN made up only of TIMING POINTs IN JOURNEY PATTERN.

## TIMING POINT ##

**Source:** Transmodel

**Definition:** A POINT against which the timing information necessary to build schedules may be recorded.

## TIMING POINT IN JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** A POINT in a JOURNEY PATTERN which is a TIMING POINT.

## TOPOGRAPHIC PLACE ##

**Source:** Transmodel

**Definition:** A type of PLACE providing the topographical context when searching for or presenting travel information, for example as the origin or destination of a trip. It may be of any size (e.g. County,City, Town, Village) and of different specificity (e.g. Greater London, London, West End, Westminster, St James s).

## TRACE ##

**Source:** Transmodel

**Definition:** A way to record the context of the changes occurred in a given ENTITY instance, as regards the authors, the causes of the changes, etc., possibly accompanied by a descriptive text.

## TRAFFIC CONTROL POINT ##

**Source:** Transmodel

**Definition:** A POINT where the traffic flow can be influenced. Examples are: traffic lights (lanterns), barriers.

## TRAFFIC INFORMATION OFFICER ROLE ##

**Source:** Transmodel

**Definition:** A ROLE dedicated to provide PASSENGERs and CUSTOMERs with traffic information.

## TRAIN ##

**Source:** Transmodel

**Definition:** A VEHICLE TYPE composed of TRAIN ELEMENTs in a certain order, i.e. of wagons assembled together and propelled by a locomotive or one of the wagons.

## TRAIN COMPONENT ##

**Source:** Transmodel

**Definition:** A specification of the order of TRAIN ELEMENTs in a TRAIN.

## TRAIN COMPONENT LABEL ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The allocation of an advertised designation for a vehicle or vehicle element for passengers.

## TRAIN ELEMENT ##

**Source:** Transmodel

**Definition:** An elementary component of a TRAIN (e.g. wagon, locomotive).

## TRAIN IN COMPOUND TRAIN ##

**Source:** Transmodel

**Definition:** The specification of the order of TRAINs in a COMPOUND TRAIN.

## TRAIN NUMBER ##

**Source:** Transmodel

**Definition:** Specification of codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs or COMPOUND TRAINs according to a functional purpose (passenger information, operation follow-up, etc)

## TRAIN STOP ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The association of a TRAIN COMPONENT at a SCHEDULED STOP POINT with a specific STOP PLACE and also possibly a QUAY and BOARDING POSITION.

## TRANSFER ##

**Source:** Transmodel

**Definition:** A couple of POINTs located sufficiently near that it may represent for a passenger a possibility to reach one of these POINTs when starting at the other one in a timescale which is realistic when carrying out a trip, e.g. ACCESS.

## TRANSFER END ##

**Source:** Transmodel

**Definition:** End point of a TRANSFER.

## TRANSFER RESTRICTION ##

**Source:** Transmodel

**Definition:** A constraint that can be applied on a CONNECTION or INTERCHANGE between two SCHEDULED STOP POINT, preventing or forbidding the passenger to use it.

## TRANSFER TIME ##

**Source:** Transmodel

**Definition:** The time needed to make an TRANSFER given a specific ACCESSIBILITY ASSESSMENT.

## TRANSFERABILITY ##

**Source:** Transmodel

**Definition:** The number and characteristics of persons entitled to use the public transport service instead of the original TRANSPORT CUSTOMER.

## TRANSPORT CUSTOMER ##

**Source:** Transmodel

**Definition:** An specific person or organisation involved in a fare process. There may be a FARE CONTRACT between the TRANSPORT CUSTOMER and the OPERATOR or the AUTHORITY ruling the consumption of services.

## TRANSPORT USER ROLE ##

**Source:** Transmodel

**Definition:** General user ROLE for consuming travel services, including information services.

## TRAVEL ##

**Source:** Transmodel

**Definition:** A sequence of TRIP PATTERNs made by a passenger.

## TRAVEL AGENT ##

**Source:** Transmodel

**Definition:** Specialisation of ORGANISATION for TRAVEL AGENT

## TRAVEL COMPENSATION ENTRY ##

**Source:** Transmodel

**Definition:** A SALES TRANSACTION recording the payment to the TRANSPORT CUSTOMER of compensation for some service shortcoming.

## TRAVEL DOCUMENT ##

**Source:** Transmodel

**Definition:** A particular physical evidence to be held by a passenger, (ticket, card, etc..) allowing the determination of the right to travel or to consume joint-services. May comprise just a token associated with an online account, or some form of representation of the access rights.

## TRAVEL DOCUMENT ANNULMENT ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the annulment of a TRAVEL DOCUMENT so that it may no longer be used.

## TRAVEL DOCUMENT COLLECTION ENTRY ##

**Source:** Transmodel

**Definition:** A FULFILMENT ENTRY recording the physical delivery of a TRAVEL DOCUMENT to a TRANSPORT CUSTOMER, for example from a ticket on demand machine at a station, or internet self service.

## TRAVEL DOCUMENT CONFISCATION ENTRY ##

**Source:** Transmodel

**Definition:** A REVENUE PROTECTION ENTRY recording the confiscation of a TRAVEL DOCUMENT from a TRANSPORT CUSTOMER because of an OFFENCE.

## TRAVEL DOCUMENT CONTROLLER ROLE ##

**Source:** Transmodel

**Definition:** The EMPLOYEE ROLE to check travel documents. Often, but not necessarily, the same as a CONDUCTOR ROLE.

## TRAVEL DOCUMENT CONTROLLING ORGANISATION ROLE ##

**Source:** Transmodel

**Definition:** The role of organisation to providing the services of checking the validity of passenger's travel documents to check they have sufficient access rights for the journey that they are making

## TRAVEL DOCUMENT SECURITY LISTING ##

**Source:** Transmodel

**Definition:** The presence of an specific TRAVEL DOCUMENT on a SECURITY LIST.

## TRAVEL FLOW ##

**Source:** Transmodel

**Definition:** A summary of the TRAVELs made by many passengers

## TRAVEL ORGANISATION ROLE ##

**Source:** Transmodel

**Definition:** The role of an ORGANISATION in providing any kind of travel related service.

## TRAVEL SPECIFICATION ##

**Source:** Transmodel

**Definition:** A set of parameters giving details of an intended consumption of access rights by a TRANSPORT CUSTOMER (e.g. origin and destination of a travel, class of travel, etc.).

## TRAVEL SPECIFICATION EVENT ##

**Source:** Transmodel

**Definition:** The selection of a set of travel options by a TRANSPORT CUSTOMER.

## TRAVELATOR EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE ACCESS EQUIPMENT for travelators (provides travelator properties like speed, etc.).

## TRAVELLING ENTITY ##

**Source:** Transmodel

**Definition:** A moving person pr object following a TRIP PATTERN.

## TRIP ##

**Source:** Transmodel

**Definition:** A part of a TRIP PATTERN describing the movement of a passenger from one PLACE of any sort to another. A TRIP may consist of one or more consecutive LEGs having some common characteristics.

## TRIP ACCESS CONSTRAINT ##

**Source:** Transmodel

**Definition:** Parameters limiting the time and nature of the access leg used to reach the PT stop. For example, to be able to specify, â€˜Walk 5 minutes, cycle 20 minutesâ€™ drive 30 minutesâ€™.

## TRIP DEBIT ##

**Source:** Transmodel

**Definition:** A log entry providing data for a debiting action in case of post-payment for a specific trip.

## TRIP DELIVERY ##

**Source:** Transmodel

**Definition:** A specialisation of PI DELIVERY to make one or more TRIP REQUESTs.

## TRIP DESTINATION PLACE ##

**Source:** Transmodel

**Definition:** A destination location for a TRIP REQUEST.

## TRIP FARE DELIVERY ##

**Source:** Transmodel

**Definition:** A specialization of PI DELIVERY make one or more FARE REQUESTs.

## TRIP FARE REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST about fares.

## TRIP FARE REQUEST FILTER ##

**Source:** Transmodel

**Definition:** Parameters controlling the type of fares returned by a TRIP FARE REQUEST.

## TRIP FARE REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used when computing and decorating TRIP FARE REQUEST results.

## TRIP MOBILITY FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters determined by accessibility criteria.

## TRIP ORIGIN PLACE ##

**Source:** Transmodel

**Definition:** An origin location for a TRIP REQUEST.

## TRIP PATTERN ##

**Source:** Transmodel

**Definition:** A movement of a passenger (or another person, e.g. driver) from an origin to a destination PLACE, done for a specific TRIP REASON.   A TRIP PATTERN may consist of one or more consecutive TRIPs.

## TRIP PATTERN MONITORING ##

**Source:** Transmodel

**Definition:** Real-time monitoring of a passenger movement to provide progress information for a passenger.

## TRIP PURCHASE ENTRY ##

**Source:** Transmodel

**Definition:** A CUSTOMER PURCHASE ENTRY recording the purchase of a single trip FARE PRODUCT by a TRANSPORT CUSTOMER..

## TRIP REASON ##

**Source:** Transmodel

**Definition:** A classification of a passenger's reason for undertaking a TRIP PATTERN, e.g. work commute, school pick up, shopping, etc..

## TRIP REQUEST ##

**Source:** Transmodel

**Definition:** A PI REQUEST concerning an optimal trip proposal, according to a specified TRIP REQUEST POLICY.

## TRIP REQUEST FILTER ##

**Source:** Transmodel

**Definition:** Filter parameters common to TRIP REQUESTs.

## TRIP REQUEST PLACE ##

**Source:** Transmodel

**Definition:** Origin, destination or via locations of a trip subject of a TRIP REQUEST.

## TRIP REQUEST POLICY ##

**Source:** Transmodel

**Definition:** Optimisation criteria to be used to when computing and decorating trip plans.

## TRIP VIA PLACE ##

**Source:** Transmodel

**Definition:** A routing location used to constrain the journeys returned. Only VEHICLE JOURNEYs whose JOURNEY PATTERNs do or do not pass through the specified points will be returned.

## TROLLEY STAND EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of STOP PLACE EQUIPMENT for trolley stands.

## TURN STATION ##

**Source:** Transmodel

**Definition:** A place (often a terminus)where a vehicle can reverse its direction (from a ROUTE to another of opposite DIRECTION).

## TURNAROUND TIME LIMIT ##

**Source:** Transmodel

**Definition:** The maximum time for which a vehicle may be scheduled to wait at a particular TIMING POINT (often included in a TURN STATION) without being returned to a PARKING POINT. A minimum time for a vehicle to turn its direction may also be recorded. This may be superseded by a DEAD RUN.

## TYPE OF ABSENCE ##

**Source:** Transmodel

**Definition:** A TYPE OF ABSENCE is a classification that indicates the reason why an EMPLOYEE is absent from work and if it is a planned or un-planned absence.

## TYPE OF ACCESS FEATURE ##

**Source:** Transmodel

**Definition:** A Classification of ACCESS FEATURE for CHECK CONSTRAINT (e.g. barrier, narrow entrance, confined space, queue management, etc.)

## TYPE OF ACCESS RIGHT ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A classification of ACCESS RIGHT ASSIGNMENT to indicate the purpose of the assignment.

## TYPE OF ACCESS RIGHT RESTRICTION ##

**Source:** Transmodel

**Definition:** Classification of access right restrictions for specifying EASEMENTs.

## TYPE OF ACCESSIBILITY LIMITATION ##

**Source:** Transmodel

**Definition:** A classification for ACCESSIBILITY LIMITATIONs, e.g. audio, visual, step free, etc.

## TYPE OF ACCESSIBILITY TOOLS ##

**Source:** Transmodel

**Definition:** A classification of ACCESSIBILITY TOOLS used by or available from ASSISTANCE SERVICE (e.g.wheelchair, walking stick, audio navigator, visual navigator, etc.)

## TYPE OF ACTIVATION ##

**Source:** Transmodel

**Definition:** A classification of real-time processes that are activated when vehicles passes an ACTIVATION POINT or an ACTIVATION LINK.

## TYPE OF ALLOWANCE ##

**Source:** Transmodel

**Definition:** A TYPE OF ALLOWANCE is a classification of additional paid times, including the information whether the allowance is given before or after the main activity.

## TYPE OF ASSISTANCE SERVICE ##

**Source:** Transmodel

**Definition:** A classification of ASSISTANCE SERVICE (e.g. boarding assistance, onboard assistance, porterage, foreign language, sign language translation, etc.).

## TYPE OF AUDIENCE ##

**Source:** Transmodel

**Definition:** A classification of the categories a MESSAGE is intended for, e.g. staff or passengers.

## TYPE OF BAGGAGE ##

**Source:** Transmodel

**Definition:** A classification of TYPE OF BAGGAGE, eg suitcase, push-chair, bicycle, sports gear.

## TYPE OF BAGGAGE USE ##

**Source:** Transmodel

**Definition:** A classification of how baggage may be used, for example carry on, check in, luggage van etc

## TYPE OF BOARDING POSITION ##

**Source:** Transmodel

**Definition:** A classification for BOARDING POSITIONs.

## TYPE OF CATERING SERVICE ##

**Source:** Transmodel

**Definition:** A classification of CATERING SERVICE (e.g. beverage vending machine, buffet, food vending machine, restaurant, snacks, trolley service, no beverages available, no food available).

## TYPE OF CHECK CONSTRAINT ##

**Source:** Transmodel

**Definition:** A classification of CHECK CONSTRAINT (e.g. ticket collection, ticket purchase, baggage check-in, incoming customs, outgoing customs, tax refunds, etc.)

## TYPE OF COMMUNICATION SERVICE ##

**Source:** Transmodel

**Definition:** A classification of COMMUNICATION SERVICE (e.g. free wifi, public wifi, phone, mobile coverage, internet, video entertainment ,audio entertainment, post box, post office, business services).

## TYPE OF CONCESSION ##

**Source:** Transmodel

**Definition:** A classification of USER PROFILE by type of person eligible to use it.

## TYPE OF CONGESTION ##

**Source:** Transmodel

**Definition:** A typology of congestions resulting from CHECK CONSTRAINT (e.g. no waiting, queue, crowding, full).

## TYPE OF COUPLING ##

**Source:** Transmodel

**Definition:** A classification for COUPLING of BLOCK PARTs.

## TYPE OF CREDIT POLICY ##

**Source:** Transmodel

**Definition:** A classification of CREDIT POLICY, to apply if user runs out of funds on account or stored value card.

## TYPE OF CUSTOMER ACCOUNT ##

**Source:** Transmodel

**Definition:** A classification of CUSTOMER ACCOUNT.

## TYPE OF CYCLE STORAGE EQUIPMENT ##

**Source:** Transmodel

**Definition:** A classification of CYCLE STORAGE EQUIPMENT (e.g. racks, bars, railings, etc.)

## TYPE OF DELAY ##

**Source:** Transmodel

**Definition:** A classification of the delay.

## TYPE OF DELIVERY VARIANT ##

**Source:** Transmodel

**Definition:** A classification of a DELIVERY VARIANT. The way of delivering a NOTICE: by vocal announcement, by visual display, issuing printed material

## TYPE OF DIRECTION OF USE ##

**Source:** Transmodel

**Definition:** Direction in which EQUIPMENT. can be used. (e.g. up, down, level, one way, both way, etc.).

## TYPE OF DISTRIBUTION ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A classification of DISTRIBUTION ASSIGNMENTs.

## TYPE OF DISTRIBUTION CHANNEL ##

**Source:** Transmodel

**Definition:** A classification of DISTRIBUTION CHANNEL, e.g. operator ticket office, onboard, self-service, third-party agent, etc.

## TYPE OF DISTRIBUTION RIGHT ##

**Source:** Transmodel

**Definition:** A classification of DISTRIBUTION RIGHTS, e.g. to sell, to exchange, to accept, etc.

## TYPE OF EMERGENCY SERVICE ##

**Source:** Transmodel

**Definition:** A typology of emergency services (e.g police, first aid, sos point, cctv).

## TYPE OF ENTITLEMENT ##

**Source:** Transmodel

**Definition:** A classification of ENTITLEMENT by type of person eligible to use it.

## TYPE OF ENTITY ##

**Source:** Transmodel

**Definition:** Classification of ENTITies, for instance according to the domain in which they are defined or used.

## TYPE OF EQUIPMENT ##

**Source:** Transmodel

**Definition:** A classification of equipment items to be installed at stop points or onboard vehicles, for instance.

## TYPE OF EVENT ##

**Source:** Transmodel

**Definition:** A classification of EVENTs (e.g. ALARMs, INCIDENTs) according to their cause of effect.

## TYPE OF FACILITY ##

**Source:** Transmodel

**Definition:** A classification of a FACILITY or a FACILITY SET.

## TYPE OF FARE CLASS ##

**Source:** Transmodel

**Definition:** A classification for fare classes (e.g. first class, second class, business class, etc).

## TYPE OF FARE CONTRACT ##

**Source:** Transmodel

**Definition:** A classification of FARE CONTRACT.

## TYPE OF FARE CONTRACT ENTRY ##

**Source:** Transmodel

**Definition:** A classification of FARE CONTRACT ENTRY.

## TYPE OF FARE PRODUCT ##

**Source:** Transmodel

**Definition:** A classification of FARE PRODUCTs .

## TYPE OF FLEXIBLE SERVICE ##

**Source:** Transmodel

**Definition:** A typology of flexible services:  Â· Virtual line service  Â· Flexible service with main route  Â· Corridor service  Â· Fixed stop area-wide flexible service  Â· Free area-wide flexible service  Â· Mixed types of flexible service (not at POINT level)  The type of flexibility can be defined at JOURNEY PATTERN level or at POINT IN JOURNEY PATTERN level in case of mixed types of flexible service inside the same JOURNEY PATTERN.

## TYPE OF FRAME ##

**Source:** Transmodel

**Definition:** A classification of VERSION FRAMEs according to a common purpose. E.g. line descriptions for line versions, vehicle schedules, operating costs. A TYPE OF FRAME is ruled by a unique TYPE OF VALIDITY.

## TYPE OF FREQUENCY OF USE ##

**Source:** Transmodel

**Definition:** A classification of FREQUENCY OF USE .

## TYPE OF FULFILMENT METHOD ##

**Source:** Transmodel

**Definition:** A classification of FULFILMENT METHOD, e.g. email, print from online, collect, etc

## TYPE OF GENDER LIMITATION ##

**Source:** Transmodel

**Definition:** A classification for GENDER LIMITATIONSs (mainly for SANITARY EQUIPMENT, e.g. male only, female only, both).

## TYPE OF GUARANTEE ##

**Source:** Transmodel

**Definition:** A classification of the type of guarantee offered for a given leg.

## TYPE OF HANDRAIL ##

**Source:** Transmodel

**Definition:** A classification of HANDRAIL (one side, both sides).

## TYPE OF HIRE SERVICE ##

**Source:** Transmodel

**Definition:** A classification of HIRE SERVICEs (e.g. car hire, motor cycle hire, cycle hire, recreational device hire).

## TYPE OF JOURNEY PATTERN ##

**Source:** Transmodel

**Definition:** A classification of JOURNEY PATTERNs used to distinguish other categories of JOURNEY PATTERN than SERVICE JOURNEY PATTERN and DEAD RUN PATTERN.

## TYPE OF LINE ##

**Source:** Transmodel

**Definition:** A classification for LINEs.

## TYPE OF LINK ##

**Source:** Transmodel

**Definition:** A classification of LINKs to express the different functional roles of a LINK.

## TYPE OF LINK SEQUENCE ##

**Source:** Transmodel

**Definition:** A classification of LINK SEQUENCEs used to define the different functions a LINK SEQUENCE may be used for.  E.g. ROUTE, road, border line etc.

## TYPE OF LOCAL SERVICE ##

**Source:** Transmodel

**Definition:** A generic (abstract) classification of LOCAL SERVICEs.

## TYPE OF LUGGAGE LOCKER ##

**Source:** Transmodel

**Definition:** A classification for LUGGAGE LOCKER EQUIPMENT (e.g. left luggage, lockers, bike carriage, porterage, free trolleys, paid trolleys)

## TYPE OF MACHINE READABILITY ##

**Source:** Transmodel

**Definition:** A classification of methods of machine reading travel documents, for example ocr, magnetic strip, nfc, etc

## TYPE OF MEDIUM ACCESS DEVICE ##

**Source:** Transmodel

**Definition:** A classification of MEDIUM ACCESS DEVICEs.

## TYPE OF MESSAGE ##

**Source:** Transmodel

**Definition:** A classification of MESSAGEs.

## TYPE OF MESSAGE PART CONTENT ##

**Source:** Transmodel

**Definition:** A classification of the content type e.g. Header, summary, detail etc.

## TYPE OF MINIMUM STAY ##

**Source:** Transmodel

**Definition:** A classification of MINIMUM STAY requirements.

## TYPE OF MONEY SERVICE ##

**Source:** Transmodel

**Definition:** A classification of MONEY SERVICE (e.g. cash machine, bank, insurance, bureau de change)

## TYPE OF NOTICE ##

**Source:** Transmodel

**Definition:** A classification for a NOTICE.

## TYPE OF OFFENCE ##

**Source:** Transmodel

**Definition:** A classification of OFFENCE, for example wrong CLASS OF SEAT, not valid for PRODUCT CATEGORY, etc.

## TYPE OF OPERATION ##

**Source:** Transmodel

**Definition:** A classification of OPERATIONs to express the different functional roles of a DEPARTMENT.

## TYPE OF ORGANISATION ##

**Source:** Transmodel

**Definition:** A classification for the ORGANISATIONs according to their activity, e.g. a public transport company, an IT company, etc).

## TYPE OF PASSAGE ##

**Source:** Transmodel

**Definition:** A classification for spaces to express how the space can be used as a passage (e.g. pathway, corridor, overpass, underpass, tunnel, etc.).

## TYPE OF PASSENGER ##

**Source:** Transmodel

**Definition:** A classification of passenger,

## TYPE OF PASSENGER INFORMATION EQUIPMENT ##

**Source:** Transmodel

**Definition:** A classification for PASSENGER INFORMATION EQUIPMENT (e.g. next stop indicator, stop announcements, passenger information facility).

## TYPE OF PAYMENT METHOD ##

**Source:** Transmodel

**Definition:** A classification for payment method (e.g. cash, credit card, debit card, travel card, contactless travel card, mobile phone, token, etc.).

## TYPE OF PENALTY POLICY ##

**Source:** Transmodel

**Definition:** A classification of PENALTY POLICY, for example no fare, excess fare, etc.

## TYPE OF PLACE ##

**Source:** Transmodel

**Definition:** A classification for PLACEs.

## TYPE OF POINT ##

**Source:** Transmodel

**Definition:** A classification of POINTs according to their functional purpose.

## TYPE OF POINT OF INTEREST SPACE ##

**Source:** Transmodel

**Definition:** A classification for POINT OF INTEREST SPACEs.

## TYPE OF PRICING RULE ##

**Source:** Transmodel

**Definition:** A classification of a PRICING RULE.

## TYPE OF PRODUCT CATEGORY ##

**Source:** Transmodel

**Definition:** A classification for VEHICLE JOURNEYs to express some common properties of journeys for marketing and fare products

## TYPE OF PROJECTION ##

**Source:** Transmodel

**Definition:** A classification of the projections according to their functional purpose, the source and target layers.

## TYPE OF PROOF REQUIRED ##

**Source:** Transmodel

**Definition:** A classification of TYPEs of PROOF needed to prove eligibility for a USER PROFILE .

## TYPE OF QUALIFICATION ##

**Source:** Transmodel

**Definition:** A classification of a QUALIFICATION possessed by an EMPLOYEE.

## TYPE OF QUAY ##

**Source:** Transmodel

**Definition:** A classification for QUAYs.

## TYPE OF RE-ENTRY POLICY ##

**Source:** Transmodel

**Definition:** A classification of RE ENTRY POLICY, if user renters a station within a specified time limit. no fare, max fare, etc.

## TYPE OF RELATION TO VEHICLE ##

**Source:** Transmodel

**Definition:** A classification of the way a VEHICLE STOPPING POSITION is used (e.g. front left, front right, back left, back right, driver left, driver right).

## TYPE OF REQUEST ##

**Source:** Transmodel

**Definition:** A classification of PI REQUESTs.

## TYPE OF RESALE ##

**Source:** Transmodel

**Definition:** Classification of after sale condition.

## TYPE OF RESERVATION FEE ##

**Source:** Transmodel

**Definition:** Classification of Fee basis for making a reservation, e.g. per group, per leg, per change, per person, etc.

## TYPE OF RESERVATION NEEDED ##

**Source:** Transmodel

**Definition:** Classification of type of reservation needed.

## TYPE OF RESERVATION RULE ##

**Source:** Transmodel

**Definition:** Classification of requirement for making a reservation, e.g. required, required for groups,

## TYPE OF RESPONSIBILITY ROLE ##

**Source:** Transmodel

**Definition:** A classification of RESPONSIBILITY ROLEs, e.g. data ownership.

## TYPE OF RETAIL DEVICE ##

**Source:** Transmodel

**Definition:** A classification of RETAIL DEVICEs.

## TYPE OF RETAIL SERVICE ##

**Source:** Transmodel

**Definition:** A classification of RETAIL SERVICE (e.g. food, newspaper tobacco, health hygiene beauty, fashion accessories, bank finance insurance, tourism, photo booth)

## TYPE OF ROUTING ##

**Source:** Transmodel

**Definition:** A classification of the ROUTING, e.g. direct, indirect; may be used to choose pricing criteria.

## TYPE OF SALES OFFER PACKAGE ##

**Source:** Transmodel

**Definition:** A classification of SALES OFFER PACKAGEs.

## TYPE OF SANITARY FACILITY ##

**Source:** Transmodel

**Definition:** A classification for SANITARY EQUIPMENT (e.g. toilet, wheelchair access toilet, shower, baby change, wheelchair baby change)

## TYPE OF SEATING EQUIPMENT ##

**Source:** Transmodel

**Definition:** A classification for SEATING EQUIPMENT.

## TYPE OF SECURITY LIST ##

**Source:** Transmodel

**Definition:** A classification of a SECURITY LIST.

## TYPE OF SERIES CONSTRAINT ##

**Source:** Transmodel

**Definition:** A classification of a SERIES CONSTRAINT.

## TYPE OF SERVICE ##

**Source:** Transmodel

**Definition:** A classification for VEHICLE JOURNEYs and SPECIAL SERVICEs to express some common properties of journeys to be taken into account in the scheduling and/or operations control process.

## TYPE OF SERVICE NATURE ##

**Source:** Transmodel

**Definition:** A classification for service available for a CHECK CONSTRAINT (e.g. self-service machine, counter service).

## TYPE OF SHELTER ##

**Source:** Transmodel

**Definition:** A classification for SHELTERs

## TYPE OF SITUATION SOURCE ##

**Source:** Transmodel

**Definition:** A classification of the SITUATION SOURCE.

## TYPE OF STAFFING ##

**Source:** Transmodel

**Definition:** A classification for the availability of the STAFF associated with an ASSISTANCE SERVICE (e.g. full time, part time)

## TYPE OF STAY ##

**Source:** Transmodel

**Definition:** A classification of the type of parking stay, e.g. long term, short term; may be used to choose pricing criteria.

## TYPE OF STOP PLACE ##

**Source:** Transmodel

**Definition:** A classification for STOP PLACEs (e.g. complex, simple, multimodal, etc).

## TYPE OF STOP POINT ##

**Source:** Transmodel

**Definition:** A classification of SCHEDULED STOP POINTs, used for instance to characterize the equipment to be installed at stops (post, shelter, seats, etc.).

## TYPE OF SUITABILITY ##

**Source:** Transmodel

**Definition:** A classification for SUITABILITY, i.e. assessments as regards a possible SUITABILITY of access according to USER NEEDS.

## TYPE OF SURFACE ##

**Source:** Transmodel

**Definition:** A classification for ROUGH SURFACE types.

## TYPE OF TARIFF ##

**Source:** Transmodel

**Definition:** A classification of TARIFFs to express the different classes of fares.

## TYPE OF TASK ##

**Source:** Transmodel

**Definition:** A TYPE OF TASK is a classification of TASKs.

## TYPE OF TICKET ##

**Source:** Transmodel

**Definition:** A classification for tickets available at a TICKETING EQUIPMENT (e.g. standard, concession, promotion, group, season, travel card, etc.)

## TYPE OF TICKETING ##

**Source:** Transmodel

**Definition:** A classification for ticketing available at a TICKETING EQUIPMENT (e.g. purchase, collection, card top up, reservations).

## TYPE OF TRAFFIC CONTROL POINT ##

**Source:** Transmodel

**Definition:** A classification of TRAFFIC CONTROL POINTs.

## TYPE OF TRAIN ELEMENT ##

**Source:** Transmodel

**Definition:** A classification of TRAIN ELEMENTs.

## TYPE OF TRANSFER ##

**Source:** Transmodel

**Definition:** A classification for TRANSFER.

## TYPE OF TRAVEL DOCUMENT ##

**Source:** Transmodel

**Definition:** A classification of TRAVEL DOCUMENTs expressing their general functionalities and local functional characteristics specific to the operator.

## TYPE OF TRAVELLING ENTITY ##

**Source:** Transmodel

**Definition:** A classification of a TRAVELLING ENTITY, e.g. person, family, cyclist, driver inc ar, tracked mobile phone, etc.

## TYPE OF USAGE PARAMETER ##

**Source:** Transmodel

**Definition:** A classification of USAGE PARAMETERs to express the nature of parameters.

## TYPE OF USAGE TRIGGER ##

**Source:** Transmodel

**Definition:** A classification of the events that may start or end a USAGE VALIDITY PERIOD, for example, 'purchase' 'start of ride', 'end of ride', 'end of day', 'end of period', etc.

## TYPE OF USAGE VALIDITY PERIOD ##

**Source:** Transmodel

**Definition:** A classification of TYPE OF USAGE VALIDITY PERIOD.

## TYPE OF USER NEED ##

**Source:** Transmodel

**Definition:** A classification of USER NEEDS.

## TYPE OF VALIDITY ##

**Source:** Transmodel

**Definition:** A classification of the validity of TYPEs OF FRAME. E.g. frames for schedules designed for DAY TYPEs, for specific OPERATING DAYs.

## TYPE OF VALUE ##

**Source:** Transmodel

**Definition:** An ENTITY that serves to classify another entry, using as a list of simple code values, each with a name.

## TYPE OF VEHICLE DETECTING ##

**Source:** Transmodel

**Definition:** A characterisation of the detection activity.

## TYPE OF VEHICLE MONITORING ##

**Source:** Transmodel

**Definition:** The aspect (type of situation) addressed by the monitoring activity.

## TYPE OF VERSION ##

**Source:** Transmodel

**Definition:** A classification of VERSIONs. E.g shareability of ENTITies between several versions.

## TYPE OF WAGE ##

**Source:** Transmodel

**Definition:** A TYPE OF WAGE is a classification used for wage accounting, which associates sums of work time recorded in ACCOUNT ENTRies to TIME BANDs relevant for accounting.

## TYPE OF WAITING ROOM ##

**Source:** Transmodel

**Definition:** A classification for WAITING ROOM EQUIPMENT.

## TYPE OF ZONE ##

**Source:** Transmodel

**Definition:** A classification of ZONEs. E.g. TARIFF ZONE, ADMINISTRATIVE ZONE.

## TripPointUsageType ##

**Source:** Transmodel

**Definition:** Usage of Point

## UNMATCHED TRAVEL ENTRY ##

**Source:** Transmodel

**Definition:** A PASSENGER TRAVEL ENTRY recording the detection that an incompletely recorded trip has been detected.

## USAGE DISCOUNT RIGHT ##

**Source:** Transmodel

**Definition:** A FARE PRODUCT allowing a customer to benefit from discounts when consuming VALIDABLE ELEMENTs.

## USAGE PARAMETER ##

**Source:** Transmodel

**Definition:** A parameter used to specify the use of a SALES OFFER PACKAGE or a FARE PRODUCT.

## USAGE PARAMETER PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a USAGE PARAMETER: discount in value or percentage, etc.

## USAGE VALIDITY PERIOD ##

**Source:** Transmodel

**Definition:** A time limitation for validity of a FARE PRODUCT or a SALES OFFER PACKAGE. It may be composed of a standard duration (e.g. 3 days, 1 month) and/or fixed start/end dates and times.

## USER NEED ##

**Source:** Transmodel

**Definition:** A user's need for a particular SUITABILITY.

## USER PROFILE ##

**Source:** Transmodel

**Definition:** The social profile of a passenger, based on age group, education, profession, social status, sex etc., often used for allowing discounts: 18-40 years old, graduates, drivers, unemployed, women, etc.

## USER PROFILE ELIGIBILITY ##

**Source:** Transmodel

**Definition:** Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a specific USER PROFILE as a validity parameter.

## VALIDABLE ELEMENT ##

**Source:** Transmodel

**Definition:** A sequence or set of FARE STRUCTURE ELEMENTs, grouped together to be validated in one go.

## VALIDABLE ELEMENT PRICE ##

**Source:** Transmodel

**Definition:** A set of all possible price features of a VALIDABLE ELEMENT: default total price, discount in value or percentage etc.

## VALIDATED ACCESS ##

**Source:** Transmodel

**Definition:** A validated use of a VALIDABLE ELEMENT, composed of ACCESSED FARE STRUCTURE ELEMENTs.

## VALIDATION ENTRY ##

**Source:** Transmodel

**Definition:** The result of the comparison between one or several CONTROL ENTRies and the theoretical access rights attached to the TRAVEL DOCUMENT controlled, validating the right to consume and possibly providing a DEBIT or one or more OFFENCEs.

## VALIDATION PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** An ACCESS RIGHT PARAMETER ASSIGNMENT relating a fare collection parameter to a VALIDATED ACCESS or one of its components.

## VALIDITY CONDITION ##

**Source:** Transmodel

**Definition:** Condition used in order to characterise a given VERSION of a VERSION FRAME. A VALIDITY CONDITION consists of a parameter (e.g. date, triggering event, etc.) and its type of application (e.g. for, from, until, etc.).

## VALIDITY PARAMETER ASSIGNMENT ##

**Source:** Transmodel

**Definition:** An ACCESS RIGHT PARAMETER ASSIGNMENT relating a fare collection parameter to a theoretical FARE PRODUCT (or one of its components) or a SALES OFFER PACKAGE.

## VALIDITY RULE PARAMETER ##

**Source:** Transmodel

**Definition:** A user defined VALIDITY CONDITION used by a rule for selecting versions. E.g. river level > 1,5 m and bad weather.

## VALIDITY TRIGGER ##

**Source:** Transmodel

**Definition:** External event defining a VALIDITY CONDITION. E.g exceptional flow of a river, bad weather, road closure for works.

## VEHICLE ##

**Source:** Transmodel

**Definition:** A public transport vehicle used for carrying passengers.

## VEHICLE ACCESS EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of VEHICLE EQUIPMENT dedicated to access vehicles providing information such as low floor, ramp, access area dimensions, etc.

## VEHICLE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment, or the cancellation of an assignment, of a physical VEHICLE to a LOGICAL VEHICLE. This assignment may be overridden by a further assignment.

## VEHICLE CHARGING EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of PLACE EQUIPMENT for vehicle charging.

## VEHICLE CONTROL ACTION ##

**Source:** Transmodel

**Definition:** A CONTROL ACTION affecting the LOGICAL VEHICLE.

## VEHICLE DETECTING ##

**Source:** Transmodel

**Definition:** An activity consisting in the identification of a vehicle at a certain time by a detection device and of collecting crude data such as an absolute location of the vehicle.

## VEHICLE DETECTING LOG ENTRY ##

**Source:** Transmodel

**Definition:** A record of detected crude real time data that is recognized to be related with a certain VEHICLE.

## VEHICLE ENTRANCE ##

**Source:** Transmodel

**Definition:** A physical entrance or exit to/from a STOP PLACE for a VEHICLE. May be a door, barrier, gate or other recognizable point of access.

## VEHICLE EQUIPMENT PROFILE ##

**Source:** Transmodel

**Definition:** Each instantiation of this entity gives the number of items of one TYPE OF EQUIPMENT a VEHICLE MODEL should contain for a given PURPOSE OF EQUIPMENT PROFILE. The set of instantiations for one VEHICLE MODEL and one purpose gives one complete 'profile'.

## VEHICLE INCIDENT ##

**Source:** Transmodel

**Definition:** An INCIDENT concerning LOGICAL VEHICLEs.

## VEHICLE JOURNEY ##

**Source:** Transmodel

**Definition:** The planned movement of a public transport vehicle on a DAY TYPE from the start point to the end point of a JOURNEY PATTERN on a specified ROUTE.

## VEHICLE JOURNEY HEADWAY ##

**Source:** Transmodel

**Definition:** Headway interval information that is available for a VEHICLE JOURNEY (to be understood as the delay between the previous and the next VEHICLE JOURNEY). This information must be consistent with HEADWAY JOURNEY GROUP if available (HEADWAY JOURNEY GROUP being a more detailed way of describing headway services).

## VEHICLE JOURNEY LAYOVER ##

**Source:** Transmodel

**Definition:** A time allowance at the end of a specified VEHICLE JOURNEY. This time supersedes any global layover or JOURNEY PATTERN LAYOVER.

## VEHICLE JOURNEY RUN TIME ##

**Source:** Transmodel

**Definition:** The time taken to traverse a specified TIMING LINK IN JOURNEY PATTERN on a specified VEHICLE JOURNEY. This gives the most detailed control over times and overrides the DEFAULT SERVICE JOURNEY RUN TIME and JOURNEY PATTERN RUN TIME and the DEFAULT DEAD RUN RUN TIME.

## VEHICLE JOURNEY WAIT TIME ##

**Source:** Transmodel

**Definition:** The time for a vehicle to wait at a particular TIMING POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY. This wait time will override the JOURNEY PATTERN WAIT TIME.

## VEHICLE MODE ##

**Source:** Transmodel

**Definition:** A characterisation of the public transport operation according to the means of transport (bus, tram, metro, train, ferry, ship).

## VEHICLE MODEL ##

**Source:** Transmodel

**Definition:** A classification of public transport vehicles of the same VEHICLE TYPE, e.g. according to equipment specifications or model generation.

## VEHICLE MONITORING ##

**Source:** Transmodel

**Definition:** An activity consisting in the assignment, at a certain time, of operational data to a monitored LOGICAL VEHICLE (e.g. that the vehicle is operating a certain MONITORED VEHICLE JOURNEY, or has passed at a certain OBSERVED PASSING TIME at a POINT).

## VEHICLE MONITORING LOG ENTRY ##

**Source:** Transmodel

**Definition:** A record of computed information describing some aspect of how a certain LOGICAL VEHICLE performs in relation to the latest operation plan based on comparing information from detection devices with operational data.

## VEHICLE POSITION ALIGNMENT ##

**Source:** Transmodel

**Definition:** The alignment of a particular BOARDING POSITION with the entrance of a VEHICLE as the result of positioning the VEHICLE at a particular VEHICLE STOPPING PLACE.

## VEHICLE QUAY ALIGNMENT ##

**Source:** Transmodel

**Definition:** The alignment of a particular QUAY with a vehicle as the result of positioning a VEHICLE at a particular VEHICLE STOPPING PLACE.

## VEHICLE SCHEDULE FRAME ##

**Source:** Transmodel

**Definition:** A coherent set of BLOCKS, COMPOUND BLOCKs, COURSEs of JOURNEY and VEHICLE SCHEDULEs to which the same set of VALIDITY CONDITIONs have been assigned.

## VEHICLE SERVICE ##

**Source:** Transmodel

**Definition:** A workplan for a vehicle for a whole day, planned for a specific DAY TYPE.

## VEHICLE SERVICE PART ##

**Source:** Transmodel

**Definition:** A part of a VEHICLE SERVICE composed of one or more BLOCKs and limited by periods spent at the GARAGE managing the vehicle in question.

## VEHICLE STOPPING PLACE ##

**Source:** Transmodel

**Definition:** A place on the vehicle track where vehicles stop in order for passengers to board or alight from a vehicle.  A vehicle track is located on the respective INFRASTUCTURE LINK for the MODE (RAILWAY ELEMENT of rail network, ROAD ELEMENT of road network, etc). A VEHICLE STOPPING PLACE may be served by one or more QUAYs.

## VEHICLE STOPPING POSITION ##

**Source:** Transmodel

**Definition:** The stopping position of a vehicle or one of its components as a location. May be specified as a ZONE corresponding to the bounding polygon of the vehicle, or one or more POINTs corresponding to parts of the vehicle such as a door.  If given as a single point, indicates the position for the door relative to an indicated side of the vehicle.

## VEHICLE TYPE ##

**Source:** Transmodel

**Definition:** A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g. standard bus, double-deck, ...).

## VEHICLE TYPE AT POINT ##

**Source:** Transmodel

**Definition:** The number of vehicles of a specified VEHICLE TYPE which may wait at a specified POINT at any one time. If the capacity is 0, then that type of vehicle may not stop there.

## VEHICLE TYPE PREFERENCE ##

**Source:** Transmodel

**Definition:** The preference for the use of a particular VEHICLE TYPE for a SERVICE JOURNEY PATTERN, depending on the DAY TYPE and TIME DEMAND TYPE. The rank of preferences must be recorded. Different VEHICLE TYPEs may be given the same rank.

## VEHICLE TYPE STOP ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The allocation of a VEHICLE STOPPING POSITION of a VEHICLE TYPE for a particular VEHICLE JOURNEY.

## VEHICLE WORK ASSIGNMENT ##

**Source:** Transmodel

**Definition:** The assignment, or the cancellation of an assignment, of a LOGICAL VEHICLE to a planned work, represented as DATED BLOCKs or as DATED VEHICLE JOURNEYs. This assignment may be overridden by a further assignment.

## VERSION ##

**Source:** Transmodel

**Definition:** A group of operational data instances which share the same VALIDITY CONDITIONs. A version belongs to a unique VERSION FRAME and is characterised by a unique TYPE OF VERSION.

## VERSION FRAME ##

**Source:** Transmodel

**Definition:** A set of VERSIONS referring to a same DATA SOURCE and belonging to the same TYPE OF FRAME. A FRAME may be restricted by VALIDITY CONDITIONs.

## VIA ##

**Source:** Transmodel

**Definition:** A secondary heading relevant for a certain part of the JOURNEY PATTERN advertising an onward intermediate destination to supplement the advertised (final) destination of DESTINATION DISPLAY.

## VIEW ##

**Source:** Transmodel

**Definition:** A VIEW assembles selected properties of one or more ENTITIEs into a separate named structure for read only use, usually to simplify an implementation. For example a CALL assembles POINT in JOURNEY PATTERN with PASSING TIMEs and other data describing a visit to an individual a STOP POINT by a SERVICE JOURNEY. A view may have a persistent identity and version, but all its attributes are derived through existing relationship to other ENTITIES and its data values can be considered as copies of the normalised data from which is derived.

## WAGE INCREASE ##

**Source:** Transmodel

**Definition:** a WAGE INCREASE is an indication to the accountancy software that the performed work was affected by aggravating circumstances to such a degree that additional payment should be allotted.

## WAGE TYPE ASSIGNMENT ##

**Source:** Transmodel

**Definition:** A WAGE TYPE ASSIGNMENT is an assignment of a TYPE OF WAGE to a DAY TYPE and a TIME BAND.

## WAITING EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of STOP PLACE EQUIPMENT for WAITING EQUIPMENTs (shelter, waiting room, etc.).

## WAITING ROOM EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of WAITING EQUIPMENT for waiting rooms, classified by TYPE OF WAITING ROOM.

## WHEELCHAIR VEHICLE EQUIPMENT ##

**Source:** Transmodel

**Definition:** Specialisation of VEHICLE EQUIPMENT for wheel chair accessibility on board a VEHICLE providing information such as the number of wheel chair areas and the access dimensions.

## WHITELIST ##

**Source:** Transmodel

**Definition:** A list of items ( TRAVEL DOCUMENTs, CONTRACTs, etc) explicitly approved for processing.

## WIRE ELEMENT ##

**Source:** Transmodel

**Definition:** A type of INFRASTRUCTURE LINK used to describe a wire network.

## WIRE JUNCTION ##

**Source:** Transmodel

**Definition:** A type of INFRASTRUCTURE POINT used to describe a wire network.

## WORK ##

**Source:** Transmodel

**Definition:** A WORK is a representation of a day on duty for a driver.

## ZONE ##

**Source:** Transmodel

**Definition:** A two-dimensional PLACE within the service area of a public transport operator (administrative zone, TARIFF ZONE, ACCESS ZONE, etc.).

## ZONE PROJECTION ##

**Source:** Transmodel

**Definition:** An oriented correspondence:  from one ZONE in a source layer, onto a target entity : e.g. POINT, COMPLEX FEATURE, within a defined TYPE OF PROJECTION.

