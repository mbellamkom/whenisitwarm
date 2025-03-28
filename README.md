# Description 
A weather query app that asks a weather database when the temperature will be 72°F or above within a certain range of time. 

## Example
Query: When will the weather be warm in March?

Answer: It'll warm up starting March 10 and continue to be warm until March 20.

## End Goal
I want to be able to ask my Google Home Mini "when will it be warm in March" and have it give me an answer.

#Phases
## Phase 1: Build User Interface
- Initial interaction of user through interface
	- Initially a terminal
 - create GUI (future)
- Receive and display user input


## Phase 2: Link API
- link [Open-Meto API ](https://open-meteo.com/)to interface
- Have API pull info related to user query 
- Have API send info related to user query back to the interface
	- parse JSON data 


## Phase 3: Display Output
- Display information related to user query in plain text in interface

## Phase 4: Input Validation and Error Handling 
- Handle edge cases like no input received from user, API connection issues, ect...
- Validate both user and API input
- Display error messages if program encounters an error
	- ex. "Please specify a date range" if no date range is entered (no input received)

## Phase 5: Link Program to Google Home Mini (Future)
- Link program to Home Mini so input and output can be auditory
