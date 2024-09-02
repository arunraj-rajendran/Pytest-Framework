@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to Make Reservation for Member
  
  @Android @MemberReservation
  Scenario Outline: Member Reservations with POS US 
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	When user clicks on Pick up location input field in Home screen
  	Then Location Search screen is displayed
  	When user enters the location: "<location>" in Location Search screen
  	And user selects the first location from the search result in Location Search screen
  	When user clicks on the View Results button in the Home Screen
  	Then verify Vehicles Screen is displayed
  	When user select vehicle "<Vehicle>" in the Vehicles Screen
  	Then verify Choose Your Coverage Screen is displayed
  	When user click on Continue button in Choose Your Coverage Screen
  	Then verify Improve Your Trip Screen is displayed
  	When user click on Continue button in Improve Your Trip Screen is displayed
  	Then verify Review Details Screen is displayed
  	When user click on Book Now button in Review details screen
  	Then on successful reservation confirmation screen is displayed 
  	And print Reservation Number
    
    Examples: 
      | username |	password	|	location	|	Vehicle			|
      | 29289797 |	Test#123	|	LOS				|	Medium Sedan|