@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to See and select/Deselect the VAS Extras
  
  @Android @VehicleScreen @Member
  Scenario Outline: Improve your trip - POS US
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	When user clicks edit button for discounts in Home screen
  	Then verify Add Discount Codes screen is displayed
  	When user enters incorrect CDP "<incorrectCDP>" in Add Discount Codes screen
  	Then verify invalid CDP format error is displayed in Add Discount Codes screen
  	When user enters invalid CDP "<invalidCDP>" in Add Discount Codes screen
  	Then verify CDP error pop up displayed in Add Discount Codes screen
  	When user enters the non travel purpose cdp "<nonTravelPurposeCDP>" in Add Discount Codes screen
  	Then verify travel purpose section is not displayed in Add Discount Codes screen
  	When user enters the travel Purpose CDP "<travelPurposeCDP>" in Add Discount Codes screen
  	Then verify travel purpose section is displayed in Add Discount Codes screen 
  	And verify saved codes dropdown is displayed in Add Discount Codes screen
  	When user selects the CDP "<CDPName>" from saved codes dropdown in Add Discount Codes screen
  	Then verify travel purpose section is displayed in Add Discount Codes screen
  	When user selects the CDP "<CDPName1>" from saved codes dropdown in Add Discount Codes screen
  	Then verify travel purpose section is not displayed
  	When user enters the invalid PC code "<invalidPCCode>" in Add Discount Codes screen
  	Then verify invalid PC format error is displayed in Add Discount Codes screen
  	When user enters the valid PC code "<valid PC code>" in Add Discount Codes screen
  	Then verify invalid PC format error is not displayed
  	When user enters the invalid RQ code "<invalidRQCode>" in Add Discount Codes screen
  	Then verify invalid RQ format error is displayed in Add Discount Codes screen
  	When user enters the valid RQ code "<valid RQ code>" in Add Discount Codes screen
  	Then verify invalid RQ format error is not displayed
  	When user click on Discount code information link in Add Discount Codes screen
  	Then verify Discount code information screen
  	When user click back in Discount code information screen
  	Then verify Add Discount Codes screen is displayed
  	When user click on back navigation in Add Discount Codes screen
  	Then verify Home screen is displayed
  	
  	Examples: 
      | username |	password	|	location	|	VehicleName		|
      | 29289797 |	Test#123	|	LOS				|	Medium Sedan	|