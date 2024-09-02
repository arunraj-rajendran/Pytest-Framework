@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to See and select/Deselect the VAS Extras
  
  @Android @VehicleScreen @Member
  Scenario Outline: Improve your trip - POS US
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	When user select vehicle "<VehicleName>" in the Vehicles Screen
  	When user add Liability Protection in choose your coverage screen
  	And user click on Continue button in Choose Your Coverage Screen
  	Then verify Improve Your Trip Screen is displayed
  	And verify FPO VAS card in Improve Your Trip Screen
  	And verify SiriusXM VAS card in Improve Your Trip Screen
  	And verify Unlimitied Wi-Fi stay connected VAS card in Improve Your Trip Screen
  	And verify Booster Seat VAS card in Improve Your Trip Screen
  	And verify Child Seat VAS card in Improve Your Trip Screen
  	And verify Infant Child Seat VAS card in Improve Your Trip Screen
  	And verify Wheel Chair VAS card in Improve Your Trip Screen
  	
  	
  	Examples: 
      | username |	password	|	location	|	VehicleName		|
      | 29289797 |	Test#123	|	LOS				|	Medium Sedan	|