@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to Search and Select Locations for Pick up and Drop off
  
  @Android @LocationSearch
  Scenario Outline: Verify Pickup Location search 
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	Then verify location search results are displayed for Airport Locations, Neighborhood Locations and Rail Locaitons in Location Search screen
  	And verify location address is displayed in Location Search screen
  	When user clicks on clear location search in Location Search screen
  	Then verify the location search is cleared in Location Search screen
  	When user clicks on back Navigation in Location Search screen
  	Then verify Home screen is displayed
  	And verify Add Different Drop off location link is not displayed in Home screen
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	Then verify location: "<selectedLocation>" is populated in Pick up location field in Home screen
  	And verify Add Different Drop off location link is displayed in Home screen
    
    Examples: 
      | username |	password	|	location	|	selectedLocation								 |
      | 29289797 |	Test#123	|	LOS				|	Los Angeles International Airport|
      
      
  @Android @LocationSearch
  Scenario Outline: Verify DropOff Location search 
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<pickUpLocation>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	Then verify location: "<pickUpSelectedLocation>" is populated in Pick up location field in Home screen
  	And verify Add Different Drop off location link is displayed in Home screen
  	When user clicks on Add Different Drop Off location link in Home screen
  	Then Drop Off Location Search screen is displayed
  	When user enters the location: "<pickUpLocation>" in Location Search screen
  	Then verify location search results are displayed for Airport Locations, Neighborhood Locations and Rail Locaitons in Location Search screen
  	And verify location address is displayed in Location Search screen
  	When user clicks on clear location search in Location Search screen
  	Then verify the location search is cleared in Location Search screen
  	When user clicks on back Navigation in Location Search screen
  	Then verify Home screen is displayed
  	When user clicks on Add Different Drop Off location link in Home screen
  	And user enters the location: "<dropOffLocation>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	Then verify location: "<dropOffSelectedLocation>" is populated in Drop off location field in Home screen
  	And  verify Return at pickup location link is displayed in Home screen
  	When user clicks on Drop Off location input field in Home screen
  	And user enters the location: "<pickUpLocation>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	Then verify Return at pickup location link is not displayed in Home screen
    
    Examples: 
      | username |	password	|	pickUpLocation	|	pickUpSelectedLocation					 |	dropOffLocation	|	dropOffSelectedLocation							|
      | 29289797 |	Test#123	|	LOS							|	Los Angeles International Airport|	SFO							|	San Francisco International Airport	|