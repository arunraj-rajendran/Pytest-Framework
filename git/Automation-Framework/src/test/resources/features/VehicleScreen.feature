@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to Choose vehicle after verifying the details
  
  
  @Android @VehicleScreen @Member
  Scenario Outline: Vehicle Screen - POS US
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	And verify location name "<LocationName>" is displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details is not displayed in vehicle screen
  	And verify electric car is displayed in the top in vehicle screen
  	And verify vehicle details in the vehicle card is displayed in vehicle screen
  	And verify per day price and est total is displayed in the vehicle card in vehicle screen
  	When user click on back navigation in the vehicle screen
  	Then verify Home screen is displayed
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	And verify EV planner in vehicle screen
  	And verify recommended vehicle is available for the member in vehicle screen
  	
  	Examples: 
      | username |	password	|	location	|	LocationName										 		 |
      | 29289797 |	Test#123	|	LOS				|	Los Angeles International Airport		 |
      
      
  @Android @VehicleScreen @Member
  Scenario Outline: Vehicle Screen - POS CA
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	And verify location name "<LocationName>" is displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details is not displayed in vehicle screen
  	And verify vehicle details in the vehicle card is displayed in vehicle screen
  	And verify per day price is not displayed and est total is displayed in the vehicle card in vehicle screen
  	And verify recommended vehicle is available for the member in vehicle screen
  	
  	Examples: 
      | username |	password	|	location	|	LocationName										 		 |
      | 29299283 |	Test#123	|	YYZ				|	Toronto Pearson International Airport|
      
  @Android @VehicleScreen @Member
  Scenario Outline: Vehicle Screen - POS AU
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	And verify location name "<LocationName>" is displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details is not displayed in vehicle screen
  	And verify vehicle details in the vehicle card is displayed in vehicle screen
  	And verify per day price is not displayed and est total is displayed in the vehicle card in vehicle screen
  	And verify recommended vehicle is available for the member in vehicle screen
  	
  	Examples: 
      | username |	password	|	location	|	LocationName			|
      | 15508606 |	Test#123	|	Perth			|	Perth Airport 		|
      
  @Android @VehicleScreen @Member
  Scenario Outline: Vehicle Screen - POS NZ
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	And verify location name "<LocationName>" is displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details displayed in vehicle screen
  	When user clicks on location name in vehicle screen
  	Then verify location details is not displayed in vehicle screen
  	And verify vehicle details in the vehicle card is displayed in vehicle screen
  	And verify per day price is not displayed and est total is displayed in the vehicle card in vehicle screen
  	And verify recommended vehicle is available for the member in vehicle screen
  	
  	Examples: 
      | username |	password	|	location	|	LocationName										 		 |
      | 15508765 |	Test#123	|	AKL				|	Auckland Airport								 		 |