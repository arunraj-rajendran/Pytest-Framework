@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to See and select/Deselect the Protection plans
  
  @Android @ChooseYourCoverageScreen @Member
  Scenario Outline: Choose Your Coverage - POS US
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	When user select vehicle "<VehicleName>" in the Vehicles Screen
  	Then verify Choose Your Coverage Screen is displayed
  	And verify Protect the car title, short description and included is displayed in choose your coverage screen
  	And verify social proofing is displayed for protect the car in choose your coverage screen
  	And verify info screen is displayed for Protect the car
  	And verify Liability Protection title, short description is displayed and included is not displayed in choose your coverage screen
  	And verify social proofing is displayed for Liability Protection in choose your coverage screen
  	And verify info screen is displayed for Liability Protection
  	And verify Personal Protection Package title, short description and included is displayed in choose your coverage screen
  	And verify social proofing is displayed for Personal Protection Package  in choose your coverage screen
  	And verify info screen is displayed with add button for Personal Protecion Package
  	And verify Drive with total peace of mind title, short description is displayed and included is not displayed in choose your coverage screen
  	And verify social proofing is not displayed for Drive with total peace of mind in choose your coverage screen
  	And verify info screen is displayed with added button if Drive with peace of mind is added in choose your coverage screen
  	
  	Examples: 
      | username |	password	|	location	|	VehicleName		|
      | 29289797 |	Test#123	|	LOS				|	Medium Sedan	|
    
   @Android @ChooseYourCoverageScreen @Member  
   Scenario Outline: Choose Your Coverage - POS CA
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	When user select vehicle "<VehicleName>" in the Vehicles Screen
  	Then verify Choose Your Coverage Screen is displayed
  	And verify continue button is disabled when no VAS is selected
  	And verify Loss Damage Waiver title, short description is displayed in choose your coverage screen
  	And verify social proofing is not displayed for Loss Damage Waiver in choose your coverage screen
  	And verify info screen is displayed for Loss Damage Waiver
  	And verify continue without proptection card and its info screen
  	
  	Examples: 
      | username |	password	|	location	|	VehicleName		|
      | 29299283 |	Test#123	|	YYZ				|	Fullsize			|